import discord, os, json, datetime, time, lib.logo as logo, asyncio, colorama
from colorama import Fore
with open('config.json') as f:
    config = json.load(f)
    
os.system("clear")
token = config.get('token')
date_format = "%a, %d %b %Y %I:%M %p"
Ghoul = discord.Client()


@Ghoul.event
async def on_ready():
    hit = 0
    f = open("../return/ID.txt", "r")
    fw = open("../return/Target.txt", "w")
    lines = f.readlines()
    print(logo.logo)
    for Id_acc in lines:
        
        Username = await Ghoul.fetch_user(Id_acc)
        Register = Username.created_at.strftime(date_format)
        try:
            join_date = Username.joined_at.strftime(date_format)
        except:
            join_date = "Unknown"
        Username = str(Username)
        print(f"ID : {Id_acc.strip()}          Create : {Register}          Join : {join_date}          Username : {Username.strip()}")
        #fw.write(f"ID : {Id_acc.strip()}          Create : {Register}          Join : {join_date}          Username : {Username.strip()}\n")
        fw.write(f"<@{Id_acc.strip()}>\n")
        hit = hit + 1
    fw.close()
    print("\nHit : ", hit)
    input()
    exit()
Ghoul.run(token, bot=False, reconnect=True) 