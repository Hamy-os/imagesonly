import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if (message.content == "clear"):
            async for msg in message.channel.history(limit=None):
                if not msg.attachments:
                    await msg.delete()
        if str(message.channel.id) == "1003812018987475144":
            try:
                if message.attachments[0]:
                    print("Image")
            except:
                print("No image, deleting: {0}".format(message.content))
                if message.author.guild_permissions.manage_guild:
                    print("admin")
                else: 
                    await message.delete()
                    await message.author.send("Your message has been removed for not containing an image. Please use <#1003962153268695140> for chatting.")

client = MyClient()
client.run('MTAwMzk2MTAxODcwMTA2NjI3Mg.GT6tcG.jVb_gWrnaTaw8R87sSJ0cU5d6ejFUvRLIWoJjc')
