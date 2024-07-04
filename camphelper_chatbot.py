import discord
import asyncio
from openai import OpenAI
import os
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
oaclient = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(message)

    if message.author == client.user:
        return

    text = message.content
    if text.startswith('!chat'):
        prompt = text[6:]

        bot_response = oaclient.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ],
            temperature=0,
        )
        
        bot_answer = bot_response.choices[0].message.content
        #print('bot response:', bot_response)
        #bot_text = '\n'.join([choice.text for choice in bot_response.choices])
        await message.channel.send(f"> Your prompt is: {prompt}\nAnswer: {bot_answer}")
        
#    if message.content.startswith('!chat'):
#        await message.channel.send('Hello!')

# 디스코드 봇 토큰을 사용하여 봇 로그인
# 여기에는 본인이 발급받은 디스코드 봇 토큰을 입력해야 합니다.
client.run('')