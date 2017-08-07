import discordbot

class Lathie:
    """BE NICE TO LATHIE

    TODO: Random Time function - Bubbles

    """

    def __init__(self, bot):
        self.bot = bot

    @discordbot.commands.command(pass_context=True, aliases=["spellcheck"])
    async def bugreport(self):
        """Lathie fucked up"""
        try:
            owner = self._owner
        except AttributeError:
            owner = self._owner = await self.bot.get_user_info(self.bot.config.get('meta', {}).get('owner', "129335628998508545"))
        return await self.bot.say(owner.mention + " you fucked up")

    @discordbot.commands.command(pass_context=True)
    async def be_nice(self, ctx):
        """Be nice to Lathie ):"""
        usr = ctx.message.author
        return await self.bot.say("Hey! be nice to " + usr.mention + " ):")

def setup(bot):
    bot.add_cog(Lathie(bot))
