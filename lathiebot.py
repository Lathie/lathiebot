
import discordbot
import asyncio

bot = discordbot.DiscordBot()

if __name__ == '__main__':
  bot.load_cogs()
  bot.run()
