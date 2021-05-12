import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib import parse
import time
import random

def chineseToGbk(a):  # used by Baidu
    return parse.quote(a.encode("gbk"))


def chineseToUtf(a):
    return parse.quote(a.encode("utf-8"))


def getBaiduScreenShoot(search):
    page = webdriver.PhantomJS(executable_path="/Users/sai/Desktop/Screenshot-Google-Baidu-Search-Results-main/phantomjs.exe")
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
    page = webdriver.PhantomJS(executable_path="/Users/sai/Desktop/Screenshot-Google-Baidu-Search-Results-main/phantomjs.exe")
    page.get("https://www.google.com/search?q=" + chineseToUtf(search) + "&tbs=qdr:y3" + "&num=100")
    page.set_window_size(1200, 800)
    time.sleep(random.randint(1, 3))
    page.maximize_window()
    time.sleep(random.randint(1, 3))
    page.save_screenshot(search + "_Google" + ".png")
    page.close()

def getSogouScreenShoot(search):
    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    baseUrl = "http://m.sogou.com/"
    page = webdriver.Chrome(executable_path="/Users/sai/Desktop/Screenshoot/chromedriver.exe", options=chromeOptions)
    page.get(baseUrl)
    time.sleep(random.randint(1, 5))
    page.find_element_by_tag_name("input").send_keys(search)
    page.find_element_by_class_name("qbtn-box").click()
    time.sleep(random.randint(1, 5))
    page.maximize_window()
    page.save_screenshot(search + "_Sogou" + ".png")
    page.close()

listName = ["eBeauty Holdings (Cayman) Limited",
            "悠可集团",
            "Chang Che Hang",
            "Liu Jiaqi",
            "Zhao Hanxi",
            "Zhang Liyang",
            "Wei Chun-Hsien",
            "Chow Lok Mei Ki",
            "Wong Long Yeung",
            "Guo Xiaorong",
            "Wang Genping",
            "Wang Yew-Ton",
            "Liu Jing",
            "Ni Min",
            "CITIC Capital Holdings Limited",
            "Hangzhou UCO Cosmetics Co., Ltd",
            "Hangzhou Youmei Beauty Co., Ltd",
            "Hangzhou Meiba Technology Co., Ltd",
            "Hangzhou Youyue Brands Management Co., Ltd",
            "张子恒",
            "刘佳琦",
            "赵涵曦",
            "张立阳",
            "韦俊贤",
            "周骆美琪",
            "黄朗阳",
            "郭晓蓉",
            "汪艮平",
            "刘竞",
            "倪敏",
            "中信资本",
            "杭州悠可化妆品有限公司",
            "杭州悠美美妆有限公司",
            "杭州美巴科技有限公司",
            "杭州悠悦品牌管理有限公司"]

listName2 = [
            "杭州美巴科技有限公司",
            "杭州悠悦品牌管理有限公司"]

for i in listName2:
    getBaiduScreenShoot(i)
