import discordbot
import datetime

class Events:
    """Event Scheduling and other cool stuff :^)"""
    def __init__(self, bot):
        self.bot = bot
        self.config = discordbot.config.Config("events.json", loop=bot.loop, directory="data")

    @discordbot.commands.command(pass_context=True)
    async def create_event(self, ctx, event_name=''):
        """Create an event interactively"""

        data = self.config.get('data', {})
        server_data = data.get(ctx.message.server.id, {})

        if not event_name:
            await self.bot.say("What do you want to call your event?")
            event_name = await self.bot.wait_for_message(author=ctx.message.author)
            event_name = event_name.content

        await self.bot.say("Enter a description for your event!")
        desc = await self.bot.wait_for_message(author=ctx.message.author)
        desc = desc.content

        await self.bot.say("When is your event taking place?")
        await self.bot.say("Please enter the time as MM/DD/YYYY HH:MM, ie. 10/01/2017 23:59")

        time_string = await self.bot.wait_for_message(author=ctx.message.author)
        time_string = time_string.content
        # try:
        #     time = datetime.datetime.strptime(time_string, '%m/%d/%Y %H:%M')
        # except ValueError:
        #     return await self.bot.say("Failed to parse your time ):")

        self.bot.say
        await self.bot.say("Is this a recurring event? [y/n]")
        recur = await self.bot.wait_for_message(author=ctx.message.author)
        if recur.content.lower() == 'y':
            recurring = True
        else:
            recurring = False

        server_data["event_name"] = event_name
        server_data["desc"] = desc
        server_data["time"] = time_string
        server_data["recurring"] = recurring
        #May have to give a channel tooooo

        data[ctx.message.server.id] = server_data
        await self.config.put('data', data)

        return await self.bot.say("Your event has been saved!")

    @discordbot.commands.command(pass_context=True)
    async def delete_all_events(self, ctx):
        """Delete all the created events"""

        data = self.config.get('data', {})
        data[ctx.message.server.id] = {}
        await self.config.put('data', data)

        return await self.bot.say("Your events have been deleted")


def setup(bot):
    bot.add_cog(Events(bot))
