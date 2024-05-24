from subprocess import PIPE, run
import discord
from discord.ext import tasks

class DiscordClient(discord.Client):
    async def setup_hook(self) -> None:
        self.checkXTask.start()

    async def on_ready(self):
        print(f"Logged on as {self.user}")

    @tasks.loop(seconds=60)
    async def checkXTask(self):
        for target in targets:
            # https://github.com/HoloArchivists/twspace-dl
            result = run(f"twspace_dl --skip-download --input-cookie-file cookie.co --user-url {target['url']} --url", stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

            if result.stderr != '':
                print(f"[{target['name']}] {result.stderr}")

            elif result.stdout != '':
                print(f"[{target['name']}] {result.stdout}")

                if result.stdout.rstrip().endswith('.m3u8') and target['lastMessage'] != result.stdout:
                    target['lastMessage'] = result.stdout

                    embed = discord.Embed(colour=int(1053978))
                    embed.set_author(name=target['name'])
                    embed.title = 'XSpaceNotifier'
                    embed.description = result.stdout
                    
                    channel = self.get_channel(int(target['channelID']))
                    await channel.send(embed=embed)

    @checkXTask.before_loop
    async def before_checkXTask(self):
        await self.wait_until_ready()

intents = discord.Intents.default()
intents.message_content = True

targets = [];
with open('discord.auth', 'r') as handle:
    discordAuth = handle.readline()
    
    while True:
        line = handle.readline()
        if not line:
            break
        
        line = line.strip().split(' ')
        targets.append(dict(url = line[0], name = line[1], channelID = line[2], lastMessage = '' ))

client = DiscordClient(intents=intents)
client.run(discordAuth)
