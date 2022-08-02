from xmlrpc.client import TRANSPORT_ERROR
import discord
import json

config = dict()
global skip
skip = False
try:
    with open('config.json') as con_file:
        config = json.load(con_file)
except:
    print('Uh oh!')
    exit(42)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if 'whitelist' in message.content:
            temp = message.content.replace('whitelist', '')
            temp = temp.replace('<@', '')
            temp = temp.replace('>', '')
            temp = temp.strip()
            with open('config.json', 'r+') as con_file:
                config['whitelist'].append(temp)
                con_file.seek(0)
                json.dump(config, con_file, indent=4)
                con_file.truncate()
            print('Added ' + temp + ' to whitelist')
        if (message.content == "clear"):
            async for msg in message.channel.history(limit=None):
                if not msg.attachments:
                    await msg.delete()
        if str(message.channel.id) == "1003962153268695140":
            try:
                if message.attachments[0]:
                    print("Image")
            except:
                print("No image, deleting: {0}".format(message.content))
                if message.author.guild_permissions.manage_guild:
                    print("admin")
                else:
                    global skip
                    for id in config['whitelist']:
                        if str(message.author.id) == id:
                            print("whitelisted")
                            skip = True
                            break
                    if skip is not True:
                        skip = False
                        await message.delete()
                        await message.author.send("Your message has been removed for not containing an image. Please use <#1003962153268695140> for chatting.")


client = MyClient()
client.run(config['token'])
