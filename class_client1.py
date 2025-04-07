#Kodland-Bot(client class)
import discord
# local own library
from bot_logic import gen_pass,coinflip,roll_dice
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

#read,add,divide,min,exp,write

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hi'):
        await message.channel.send("SERIOUS meeting you!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('pass'):
        await message.channel.send(f"Here's your SERIOUS password! {gen_pass(10)}")
    elif message.content.startswith('coin'):
        await message.channel.send(f"I'll give you a SERIOUS coinflip! {coinflip()}")
    elif message.content.startswith('dice'):
        await message.channel.send(f"Here comes a SERIOUS diceroll! {roll_dice()}")
        
            
    #elif message.content.startswith('write'):
        #await message.channel.send(f"Let me write something SERIOUS! {write()}")
   # elif message.content.startswith('add'):
        #await message.channel.send(f"Let me add something SERIOUS! {add()}")
    #elif message.content.startswith('min'):
       # await message.channel.send(f"Let me do some SERIOUS calculations! {min()}")
    #elif message.content.startswith('divide'):
        #await message.channel.send(f"Let me do some SERIOUS calculations! {divide()}")
    #elif message.content.startswith('exp'):
        #await message.channel.send(f"Let me do some SERIOUS calculations! {exp()}")
    #elif message.content.startswith('read'):
        #await message.channel.send(f"Let me do some SERIOUS reading! {read()}")

@client.event    
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
        await guild.system_channel.send("try to type $halo or $bye or pass")

client.run("MTM0ODYzODUyNzI4OTU1NzA2NA.GYQ7Rq.rxEPK7zYupNTJ4FPEqhU62yHPMX3QBCt18u7Zc")



