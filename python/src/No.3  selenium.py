import os
import time
from hashlib import md5
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

#设置查询内容
fond = '旅游'

#打开浏览器
driver = webdriver.Chrome()
#设置等待
wait = WebDriverWait(driver,10)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

def init(text):
    try:
        driver.get('https://www.toutiao.com/search/?keyword='+text)
        button = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                'body > div > div.y-box.container > div.y-left.index-middle > div.tabBar > ul > li:nth-child(3)'
            ))
        )
        button.click()
        upDown(5)
    except Exception:
        print('打开连接失败')

def upDown(t):
    js="var q=document.documentElement.scrollTop=100000"
    for i in range(0,t):
        driver.execute_script(js)
        time.sleep(1)

#解析出页面链接
def getProducts():
    wait.until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            'body > div > div.y-box.container > div.y-left.index-middle > div.feedBox.child-style > div > div'
        ))
    )
    html = driver.page_source
    doc = pq(html)
    items = doc('.feedBox .sections .articleCard').items()
    for item in items:
        src = 'https://www.toutiao.com/'+\
              item.find('.title-box .link').attr('href')
        print('正在打开'+src)
        initOnePage(src)

#打开每个小页面
def initOnePage(src):
    try:
        driver.get(src)
        wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                '.J_imageList'
            ))
        )
        html = driver.page_source
        pageDoc = pq(html)
        pageItems = pageDoc('.image-list .image-item').items()
        for item in pageItems:
            imgSrc = item.find('.image-item-inner .image-origin').attr('href')
            print(imgSrc)
            saveImg(requests.get(imgSrc,headers = headers).content)
    except Exception:
        print(src+'页面打开失败')

#保存图片
def saveImg(imgSrc):
    filePath = '{0}/{1}.{2}'.format('M:\img',md5(imgSrc).hexdigest(),'jpg')
    if not os.path.exists(filePath):
        with open(filePath,'wb') as f:
            f.write(imgSrc)
            f.close()

def main():
    init(fond)
    getProducts()
    driver.close()

if __name__ == '__main__':
    main()