def double_letter (str):
    result = ''
    for letter in str:
        result += letter * 2
    return result


def secret_function (a, b):
    # Tulis kode Kamu di sini!
    return " "


print(double_letter("Hello"))
print(secret_function(1, 2))
print(secret_function("Hello, ", "world!"))

import discord

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

client.run("MTM0ODYzODUyNzI4OTU1NzA2NA.GYQ7Rq.rxEPK7zYupNTJ4FPEqhU62yHPMX3QBCt18u7Zc")