import  os,discum, json, datetime, time, lib.logo as logo, colorama
from colorama import Fore

os.system("ls")
with open('config.json') as f:
    config = json.load(f)

os.system("clear")
print(logo.logo)
token = config.get('token')

guild = input("Server ID : ")
channel = input("Channel ID : ")
ghoul = discum.Client(token= token, log=False)


ghoul.gateway.fetchMembers(guild, channel)
@ghoul.gateway.command
def memberTest(resp):
    if ghoul.gateway.finishedMemberFetching(guild):
        ghoul.gateway.close()
ghoul.gateway.run()

f = open('../return/ID.txt', 'w')
for memberID in ghoul.gateway.session.guild(guild).members:
    id = str(memberID)
    f.write(f'{id}\n')
f.close()
