from subprocess import PIPE, run
import discord
from discord.ext import tasks

USER_URL = 'https://twitter.com/airikannakr'
USER_NAME = 'AiriKanna'

class DiscordClient(discord.Client):
    async def setup_hook(self) -> None:
        self.lastMessage = ''

        self.checkXTask.start()

    async def on_ready(self):
        print(f'Logged on as {self.user}')

    @tasks.loop(seconds=60)
    async def checkXTask(self):
        channel = self.get_channel(int(channelID))

        # https://github.com/HoloArchivists/twspace-dl
        result = run(f'twspace_dl --skip-download --input-cookie-file cookie.co --user-url {USER_URL} --url', stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

        if result.stderr != '':
            print(result.stderr)

        elif result.stdout != '':
            print(result.stdout)

            if result.stdout.rstrip().endswith('.m3u8') and self.lastMessage != result.stdout:
                self.lastMessage = result.stdout

                embed = discord.Embed(colour=int(1053978))
                embed.set_author(name=USER_NAME)
                embed.title = 'XSpaceNotifier'
                embed.description = result.stdout
                await channel.send(embed=embed)

    @checkXTask.before_loop
    async def before_checkXTask(self):
        await self.wait_until_ready()

intents = discord.Intents.default()
intents.message_content = True

handle = open('discord.auth', 'r')
discordAuth = handle.readline()
channelID = handle.readline()
handle.close()

client = DiscordClient(intents=intents)
client.run(discordAuth)
