import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

# 디스코드 봇 토큰을 사용하여 봇 로그인
# 여기에는 본인이 발급받은 디스코드 봇 토큰을 입력해야 합니다.
client.run('your key')