from selenium import webdriver  # selenium must be 3.0
from urllib import parse
import time
import random

def chineseToGbk(a):  # used by Baidu
    return parse.quote(a.encode("gbk"))


def chineseToUtf(a):
    return parse.quote(a.encode("utf-8"))


def getBaiduScreenShoot(search):
    page = webdriver.PhantomJS(executable_path=r'C:\Users\sai\Desktop\screenshot-searchresults-main\phantomjs.exe')
    page.get("https://www.baidu.com/s?wd=" + chineseToGbk(search) + "&usm=3&rsv_idx=2&rsv_page=1")
    time.sleep(random.randint(1, 3))
    page.set_window_size(1200, 800)
    time.sleep(random.randint(1, 3))
    page.set_window_size(1000, 800)
    time.sleep(random.randint(1, 3))
    page.maximize_window()

    for i in range(0, 10):
        page.save_screenshot(search + "_Baidu" + str(i) + ".png")
        try:
            next = page.find_element_by_link_text("下一页 >")
        except:
            break
        next.click()
        time.sleep(5)

    page.close()

def getGoogleScreenShoot(search):
    page = webdriver.PhantomJS(executable_path=r'C:\Users\sai\Desktop\screenshot-searchresults-main\phantomjs.exe')
    page.get("https://www.google.com/search?q=" + chineseToUtf(search) + "&tbs=qdr:y3" + "&num=100")
    page.set_window_size(1200, 800)
    time.sleep(random.randint(1, 3))
    page.maximize_window()
    time.sleep(random.randint(1, 3))
    page.save_screenshot(search + "_Google" + ".png")
    page.close()

text = open("list.txt", encoding = "utf-8")
listName = [x.strip('\n') for x in text]

for i in listName:
    #getBaiduScreenShoot(i)
    getGoogleScreenShoot(i)
