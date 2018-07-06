
# No.3  selenium

### 备注：调用的包
```
import os
import time
from hashlib import md5
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
```

### 1.打开浏览器驱动的
```
driver = webdriver.Chrome()
```

也可以用
```
driver = webdriver.PhantomJS()    //PhantomJS 可以解决掉Chrome每次都要调用出浏览器的缺点
driver.set_window_size(1400,900)  //使用PhantomJS 要设置一个窗口的大小，否则容易被发现是爬虫
```
 
### 2.设置一个等待（等待需要加载的东西加载出来）
```
wait = WebDriverWait(driver,10)
```
### 3.模拟浏览器的头
```
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
```
### 4.通过selenium打开页面
```
driver.get('https://www.toutiao.com/search/?keyword='+text)
```
### 5.等待按钮被加载出来

``` 
button = wait.until(	        	//之前wait中放入了driver所以可以获取到元素
    EC.element_to_be_clickable((    //等待按钮可以被点击
        By.CSS_SELECTOR,			//通过css来查找元素
        '<标签里面的class属性>'		//此处写css代码
        ))
    )
button.click()						//点击这个按钮
```



### 6.拖到底方法
```
js="var q=document.documentElement.scrollTop=100000"
for i in range(0,t):
    driver.execute_script(js)
    time.sleep(1)
```
### 7.等待页面需要读取的信息被加载出来
```
wait.until(
    EC.presence_of_element_located((    //等待页面加载完
        By.CSS_SELECTOR,
        '<标签里面的class属性> '
    ))
)
```
### 8.拿到html内容并放入PyQuery
```
html = driver.page_source //拿到页面
doc = pq(html)
```
### 9.PyQuery解析
```
items = doc('.feedBox .sections .articleCard').items() //此处的class不用从头写，且因为这个class里面是多个重复的所以用items来取得集合
    for item in items:
        src = 'https://www.toutiao.com/'+\
              item.find('.title-box .link').attr('href')//在单个的item里面查询到.title-box .link这个div 然后通过attr获取到href的值
```

### 10.通过url将图片下载
```
·······
imgSrc = item.find('.image-item-inner .image-origin').attr('href')
saveImg(requests.get(imgSrc,headers = headers).content)//requests中的方法
```

### 11.保存图片
```
def saveImg(imgSrc):
    filePath = '{0}/{1}.{2}'.format('M:\img',md5(imgSrc).hexdigest(),'jpg')
    if not os.path.exists(filePath):
        with open(filePath,'wb') as f:
            f.write(imgSrc)
            f.close()
```

> 源码:https://github.com/shutter-cp/notebook/blob/master/python/src/No.3%20%20selenium.py
