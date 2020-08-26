import discord

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Mööp möp")

    #Wenn nachrichten geschrieben werden kommt es in den Log
    async def on_typing(self, channel, user, when):
        print(str(user) + " tippt gerade in " + str(channel) + " channel seit " + str(when))

    #Gelöschte nachrichten loggen
    async def on_message_delete(self, message):
        print("Gelöschte Nachticht " + message.content)

    #Editierte nachrichten loggen
    async def on_message_edit(self, before, after):
        print("Changed message " + before.content + " to " + after.content)


    #Wenn Nachrichten Persöhnlich gepostet werden
    async def on_message(self, message):
       if message.author == client.user:
           return
       if message.content.startswith("Hi"): #ausgabe des benutzers
           await message.channel.send("Ne oder?") #ausgabe des bot's
           else
       if message.content.startwith("Moin"):
           await message.channel.send("Moin moin!")



client = MyClient()
client.run("12345679")
