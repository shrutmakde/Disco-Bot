import discord
import asyncio
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

keywords = ['susu']

@client.event
async def on_message(message):
    if message.content.startswith('!mention me'):
        await message.channel.send(message.author.mention)
    if message.content.startswith("Who is my creator?"):
        await message.channel.send("Prometheus#2874 made me in 2020. I initially started out as a bot for jokes but now he works on me part time.")
    if message.content.startswith("I love you"):
        await message.channel.send("I love you too!")
    for i in range(len(keywords)):
        if keywords[i] in message.content:
         for j in range(1):
                await message.channel.send("susu")
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server! I am a bot made by shivansh entirely in python. Nice to meet you!')

@client.command(help='pings phoenix')
async def pingphoenix(ctx):
    pingfarhan = get(ctx.guild.members, name ='phoenix_')
    await ctx.send(f"{pingfarhan.mention}")

@client.command(help='pings av')
async def pingav(ctx):
    pingadhvi = get(ctx.guild.members, name ='av')
    await ctx.send(f"{pingadhvi.mention}")

@client.command(help='pings nitta')
async def pingsenpai(ctx):
    pingsenpai = get(ctx.guild.members, name ='call me ˢᵉⁿᵖᵃᶦ')
    await ctx.send(f"{pingsenpai.mention}")

@client.command(help='joins users vc')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command(help='leaves current vc')
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.run('token')
