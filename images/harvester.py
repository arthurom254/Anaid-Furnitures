
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
chrome="/home/blue/Downloads/chromedriver/chromedriver"

driv="/home/blue/Downloads/chrome-linux64/chrome"
service=Service(chrome)
options=Options()
options.binary_location=driv
driver=webdriver.Chrome(service=service, options=options)

driver.get("https://www.istockphoto.com/photos/office-chair")
# time.sleep(200)
x=driver.find_elements(by="xpath", value='//img')
urls=[]
for v in x:
    path=v.get_attribute("src")
    # path=path.split('.jpg')
    alt=v.get_attribute("alt")
    alt=alt.replace(" ", "-")
    string=f"wget {path} -O {alt}.jpg"
    urls.append(path)
    # try:
    # os.system(string)
    # except Exception as e:
    #     print(e)

print(urls)
