import os, discord
import asyncio
from discord.ext import commands

token = input("Enter Token: ")
client = commands.Bot(command_prefix=commands.when_mentioned_or(""))
os.system('Justice On top')
os.system(f'auto pressure fags')
os.system(f'mode 100,25')




@client.event
async def on_ready():
  print(f"hartted")
  
  print(f""" \u001b[31m
______________         _________            
___  __ )__  /_______________  /            
__  __  |_  /_  _ \  _ \  __  /             
_  /_/ /_  / /  __/  __/ /_/ /              
/_____/ /_/  \___/\___/\__,_/               
                                            
_________             __________            
______  /___  __________  /___(_)__________ 
___ _  /_  / / /_  ___/  __/_  /_  ___/  _ \
/ /_/ / / /_/ /_(__  )/ /_ _  / / /__ /  __/
\____/  \__,_/ /____/ \__/ /_/  \___/ \___/ 
                                             
                                                                           
  type "lets pack" in chat to start auto pressure
        
""")

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.endswith('sal'):
      while True: 
        await message.channel.send("<@724930648996970526> samacacpetn🥷") 
        await asyncio.sleep(3)
        await message.channel.send ("<@724930648996970526> sa mi bag pulan familia mati🤡 ;)))))))))))")
        await asyncio.sleep(3)
        await message.channel.send ('<@724930648996970526> te a abandonat ma ta😂😂 ;))))))))))))')
        await asyncio.sleep(3)
        await message.channel.send ('<@724930648996970526> dc taci fmmmm????? 🔪')
        await asyncio.sleep(3)
        
        
        
client.run(token, bot=False)