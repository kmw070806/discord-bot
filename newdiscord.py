import discord

client = discord.Client()

@client.event
async def on_ready();
   print(client.user.id)
   print("ready")



   @client.event
   async def on_message(message):
       if message.content.startswith("안녕")
       await message.channel.send("반갑다 ㅈ간")


       client.run("NjkzNjM2OTEzOTQwMTM1OTc2.Xn_96Q.eK7pmTpeYQn8JMX00OQDmbj283U")