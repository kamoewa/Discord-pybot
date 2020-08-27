import discord

class MyClient(discord.Client):
    #Login Message 
    async def on_ready(self):
        print("welcome back, let's rock the discord")

    #Log when user starts to writes a message
    async def on_typing(self, channel, user, when):
        print(str(user) + " Is typing in " + str(channel) + " channel since " + str(when))

    #Log deleted messages
    async def on_message_delete(self, message):
        print("Deleted message " + message.content)

    #Log edited messages
    async def on_message_edit(self, before, after):
        print("Changed message " + before.content + " to " + after.content)


    #Bot respond to a users text or word
    async def on_message(self, message):
       if message.content.startswith("Hi"): #output what the user say's
           await message.channel.send("Hello") #output what the bot will say

client = MyClient()
client.run("my bot token")
