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
    page = webdriver.PhantomJS(executable_path="/Users/sai/Desktop/Screenshoot/phantomjs.exe")
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
        time.sleep(random.randint(5, 9))

    page.close()

def getGoogleScreenShoot(search):
    page = webdriver.PhantomJS(executable_path="/Users/sai/Desktop/Screenshoot/phantomjs.exe")
    page.get("https://www.google.com/search?q=" + chineseToUtf(search) + "&num=100")
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

listName = ["杨德勇",
            "朱葛颖",
            "崔洪杰",
            "朱晓星",
            "郭杰",
            "薛军",
            "朱霖",
            "郭志宝",
            "杜新",
            "王立峰",
            "远洋集团控股有限公司",
            "耀胜发展有限公司",
            "远洋亿家物业服务股份有限公司",
            "中远酒店物业管理有限公司",
            "YANG Deyong",
            "ZHU Geying",
            "CUI Hongjie",
            "ZHU Xiaoxing",
            "GUO Jie",
            "XUE Jun",
            "ZHU Lin",
            "GUO Zhibao",
            "DU Xin",
            "WANG Lifeng",
            "Sino-Ocean Group Holding Limited",
            "Shine Wind Development Limited",
            "Ocean Homeplus Property Service Corporation Limited",
            "Zhongyuan Hotel Property Management Co Ltd"]

listName2 = ["杜新"]

for i in listName2:
    getSogouScreenShoot(i)
    time.sleep(random.randrange(5, 10))