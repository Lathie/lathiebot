from random import choice
from glob import glob
import discordbot

class Splat:
    """Splatoon maymays :^)"""

    def __init__(self, bot):
        self.bot = bot

    @discordbot.commands.command(pass_context=True)
    async def spellcheck(self):
        """Lathie sucks at spelling"""
        try:
            owner = self._owner
        except AttributeError:
            owner = self._owner = await self.bot.get_user_info(self.bot.config.get('meta', {}).get('owner', "129335628998508545"))

        return await self.bot.say(owner.mention + " you fucked up")

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

def setup(bot):
    bot.add_cog(Splat(bot))
