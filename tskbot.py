# TO BE RUNNED ON PYTHON3.8
# MADE BY ERIC ROY (github/royalmo)

# Read README.md first, and be sure to enter your TOKEN and GUILD ID

# Importing stuff
import json
import discord

def get_path(): # Returns main.py file path
    return str(Path(__file__).parent.absolute()) + "/"

class TskBot(discord.Client):
    async def on_ready(self):
        # Gets guild info (discord server)
        self.guild = discord.utils.get(self.guilds, id=DISCORD_GUILD)

        # Print info message.
        print(f'Connected to Discord!\n\nBot username: {self.user}\n\nServer: {self.guild.name}\nServer id: {self.guild.id}')

        # Setting Watching status
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Telecinco"))

    async def on_message(self, message):

        # Checks if message isn't from the bot itself, is from the correct server, and it is plain text. 
        if message.author == self.user or message.guild != self.guild or message.type != discord.MessageType.default:
            return

        if ('http://' in message.content or 'https://' in message.content) and message.author.roles[0].position == 0:
            await message.delete()

    
if __name__ == "__main__":

    # Welcome message
    print("*"*55 + "\n" + " "*11 + "TSK BOT - Discord server manager\n" + "*"*55 + "\n\nLoading settings and connecting to Discord...")

    # Loads settings
    with open(get_path() + 'bot_settings.json', 'r') as json_token:
        filein = json.loads(json_token.read())
        DISCORD_TOKEN = filein['token']
        DISCORD_GUILD = filein['guild']

    # Runs bot loop
    mainbot = TskBot()
    mainbot.run(DISCORD_TOKEN)