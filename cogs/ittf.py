import calendar, datetime
from bs4 import BeautifulSoup
import urllib
from urllib import request
import discordbot

class ITTF:
    """Looking up information on ITTF."""

    def __init__(self, bot):
        self.bot = bot

    @discordbot.commands.command(pass_context=True, aliases=['rank'])
    async def rankings(self, ctx, sex: str = "M", agegroup: int = 100, month: str = None, year: int = None):
        """Gets the world rankings

        Allows you to get the rankings of a specific gender, age group, month and year.
        This goes back to 2017 because that's how far the ITTF goes back.
        Genders: M, F
        Age groups: 100, 21, 18, 15
        Months: Jan-Dec
        Years: 2014-Present
        """

        sex_char = "M"
        if sex.lower().startswith(('f', 'w')):
            sex_char = 'W'

        months = {**{v.lower(): k for k, v in enumerate(calendar.month_abbr)},
                  **{v.lower(): k for k, v in enumerate(calendar.month_name)}}
        try:
            month_num = months[month.lower()]
        except (KeyError, AttributeError) as e:
            recent = BeautifulSoup(urllib.request.urlopen(
                "http://dr.ittf.com/ittf_ranking/WR_Table_3_A2.asp?Month1=5&Year1=2017&Gender=M&Category=100M").read(),
                                   "html.parser").find_all("table")[0].find_all("tr")[1].contents[1].find_all("a")[
                         5].get_text()[:3]
            month_num = months[recent.lower()]

        year_num = year
        if year_num is None or year_num < 2014:
            year_num = datetime.datetime.now().year

        age = agegroup
        if age not in (15, 18, 21, 100):
            age = 100

        soup = BeautifulSoup(urllib.request.urlopen(
            "http://dr.ittf.com/ittf_ranking/WR_Table_3_A2.asp?Month1={}&Year1={}&Gender={}&Category={}{}"
                .format(month_num, year_num, sex_char, age, sex_char)).read(), "html.parser")

        rows = soup.find_all("table")[0].find_all("tr")[1].contents[3]
        peeps = []
        for row in rows.find_all("tr")[6:156]:
            # print(row)
            blocks = row.find_all("td")[2:]
            info = []
            for block in blocks:
                info.append(block.get_text().strip())
            peeps.append(' | '.join(info))
        try:
            p = discordbot.Pages(self.bot, message=ctx.message, entries=peeps)
            p.embed.colour = 0x738bd7  # blurple

            title = ""
            if sex_char == "M":
                title += "Men's"
            else:
                title += "Women's"

            if age != 100:
                title += " U"+str(age)

            month_names = {v: k for v, k in enumerate(calendar.month_abbr)}
            title += " Rankings " + month_names[month_num] + " " + str(year_num)

            p.embed.set_author(name=title, icon_url="http://dr.ittf.com/Logos/logo_world_ranking.gif")
            await p.paginate()

        except Exception as e:
            await self.bot.say(e)

def setup(bot):
    bot.add_cog(ITTF(bot))