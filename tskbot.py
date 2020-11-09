# TO BE RUNNED ON PYTHON3.8
# MADE BY ERIC ROY (github/royalmo)

# Read README.md first, and be sure to enter your TOKEN and GUILD ID

# Importing stuff
import json
import discord
from pathlib import Path
from time import sleep

def get_path(): # Returns main.py file path
    return str(Path(__file__).parent.absolute()) + "/"

class TskBot(discord.Client):
    async def on_ready(self):
        # Gets guild info (discord server)
        self.guild = discord.utils.get(self.guilds, id=DISCORD_GUILD)

        # Print info message.
        print(f'Connected to Discord!\n\nBot username: {self.user}\n\nServer: {self.guild.name}\nServer id: {self.guild.id}')

        # Make banning web role list.
        self.nw_role = [self.guild.get_role(EV_ROLE_ID), self.guild.get_role(NW_ROLE_ID)]

        # Setting Watching status
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Telecinco"))

    async def on_message(self, message):

        # Checks if message isn't from the bot itself, is from the correct server, and it is plain text. 
        if message.author == self.user or message.guild != self.guild or message.type != discord.MessageType.default:
            return

        if ('http://' in message.content or 'https://' in message.content) and message.author.roles == self.nw_role:
            await message.delete()

            response = await message.channel.send(f"{message.author.mention} casi crak, aun debes ascender.")
            await response.delete(delay=10)


if __name__ == "__main__":

    # Welcome message
    print("*"*55 + "\n" + " "*11 + "TSK BOT - Discord server manager\n" + "*"*55 + "\n\nLoading settings and connecting to Discord...")

    # Loads settings
    with open(get_path() + 'bot_settings.json', 'r') as json_token:
        filein = json.loads(json_token.read())
        DISCORD_TOKEN = filein['token']
        DISCORD_GUILD = filein['guild']
        EV_ROLE_ID = filein['everyone-role-id']
        NW_ROLE_ID = filein['newwie-role-id']

    # Runs bot after 30 seconds of delay. Why we do this? Because when raspi boots, network is ready some seconds after rc.local is executed, so if we don't wait the program crashes.
    sleep(30)

    # Starting the bot
    mainbot = TskBot()
    mainbot.run(DISCORD_TOKEN)