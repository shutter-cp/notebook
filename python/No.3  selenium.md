


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
9.PyQuery解析
