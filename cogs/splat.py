import datetime
from random import choice
from glob import glob
import discordbot

#Time Formatting Utility
def strfdelta(tdelta, fmt): #From Stack Overflow
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

class Splat:
    """Splatoon maymays :^)"""

    def __init__(self, bot):
        self.bot = bot

    @discordbot.commands.command(pass_context=True)
    async def marie(self):
        """Uploads a random picture of the best girl Marie :)"""
        return await self.bot.upload(choice(glob("./assets/pictures/marie/*")))

    @discordbot.commands.command(pass_context=True, aliases=['picture'])
    async def image(self, ctx, *, folder=""):
        """Uploads a random picture from a specified catagory"""
        picture_path = "./assets/pictures/"
        allowed_categories = ["marie", "splatmeme"]

        folder = folder.lower()

        if not folder or folder not in allowed_categories:
            await self.bot.responses.basic(message="Category not found, picking randomly!")
            folder = choice(allowed_categories)

        return await self.bot.upload(choice(glob(picture_path + folder + "/*")))

    @discordbot.commands.command(pass_context=True)
    async def splatdown(self):
        """Gives the time until the next splatfest begins"""
        #delta = datetime.datetime(2017, 8, 4, 23) - datetime.datetime.now()
        #return await self.bot.say(strfdelta(delta, "{hours} hours and {minutes} minutes to go :pray:"))
        return await self.bot.say("SPLATFEST IN PROGRESS!!!")

def setup(bot):
    bot.add_cog(Splat(bot))
