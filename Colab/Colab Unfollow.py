!pip install kora -q
from kora.selenium import wd as driver

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
t_unfollow = 0.6
import datetime as dt

chat_ID = ''

bot_ID = ''
import requests


import random
pw = ''
usr1 =''
followB = 16
scrollN = 10

# initialize driver

def login(us,pswd):
    
    driver.get('https://www.instagram.com/')
    url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= Unfollower.py file started Sir!'
    requests.post(url)
    # accepting the cookies
    try:
        cookies_accept= driver.find_element_by_xpath('//button[text()="Accept"]')
        cookies_accept.click()
        time.sleep(3)
    except:
        pass
    
    time.sleep(3)
    username = driver.find_element_by_name('username')
    username.click()
    username.send_keys(us)
    
    password = driver.find_element_by_name('password')
    password.click()
    password.send_keys(pswd)
    

    log_in = driver.find_element_by_xpath('//div[text()="Log In"]')
    log_in.click()
    time.sleep(3)
    driver.implicitly_wait(10)
    # credential storage
    try:
        credentials= driver.find_element_by_xpath('//button[text()="Not Now"]')
        credentials.click()
        time.sleep(1)
    except:
        pass

    #  notifications
    try:
        notifications = driver.find_element_by_xpath('//button[text()="Not Now"]')
        notifications.click()
        time.sleep(3)
    except:
        pass
    
    
    #****** SEARCH   ********
    
    search1 = driver.find_element_by_xpath('//span[text()="Search"]')
    search1.click()
    time.sleep(1)
    search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
    search_2.send_keys(usr1)
    
    
    #        *********** Count of Scrolls **************** List of Accounts +++++++++++++++++++++++
    
    
    count = 0
    while count <3:
        search_2.send_keys(Keys.ENTER)
        count +=1 # count = count +1
        time.sleep(1)  

    time.sleep(2)
    following = driver.find_element(By.XPATH,'(//a)[3]')
    following.click()
    time.sleep(5)
    
    
    a = dt.datetime(2022, 4, 28, 12, 0, 0, 0)   # datetime(year, month, day, hour, minute, second, microsecond)
    b = dt.datetime.now()
    t = a - \
        b
    print( "Time left : ", t)
    check = t.total_seconds()
    i = 0
    p = 1
    Flag = 1
    stack = 1
    
    
    
    while check > 0:
        
        try:
            time.sleep(2)
            following = driver.find_element(By.XPATH,'(//a)[3]')
            following.click()
            time.sleep(5)
        except:
            pass
        
        b = dt.datetime.now()
        t = a - \
            b
        url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= While loop entered successfully!'
        requests.post(url)
        
        fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < scrollN : # scroll N times
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(2)
            scroll += 1

        fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
        print("fList len is {}".format(len(fList)))    
        time.sleep(2)
        if Flag == 1:
            count = 0
        
        
        
        #*************************** CLick UnFollow***************************
        
        
        for i in range(i+1, len(fList)+1):
            
            try:
                j = 6
                ele = driver.find_element(By.XPATH, '/html/body/div[{}]/div/div/div/div[3]/ul/div/li[{}]/div/div[2]/button/div'.format(j,i))
                print('div is 6')
            except:
                j = 5 
                ele = driver.find_element(By.XPATH, '/html/body/div[{}]/div/div/div/div[3]/ul/div/li[{}]/div/div[2]/button/div'.format(j,i))
                print('div is 5')
                url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text=div is 5!!!!! '
                requests.post(url)
                
            if ele.text == "Following":
                time.sleep(t_unfollow)
                unfollow = driver.find_element(By.XPATH, '/html/body/div[{}]/div/div/div/div[3]/ul/div/li[{}]/div/div[2]/button'.format(j,i))
                unfollow.click()
                time.sleep(t_unfollow)
                count = count+1
                try:
                    unfollow2 = driver.find_element(By.XPATH , '/html/body/div[7]/div/div/div/div[3]/button[1]')
                    driver.implicitly_wait(30)
                    unfollow2.click()
                    Flag = 1
                except:
                    driver.get(f"https://www.instagram.com/{usr1}/")
                    Flag = 0
                    i = 0
                    break
                print(count)
            if count >= followB:
                print("Ended Stack No. : ", stack)
                
                b = dt.datetime.now()
                t = a - \
                    b
                url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text=Ended Stack No. : {stack}, Time left = {t} '
                requests.post(url)
                print('Time left : ', t)
                stack = stack+1
                time.sleep(600)
                b = dt.datetime.now()
                t = a - \
                    b
                print('Time left : ', t)
                count =0
                url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text=Ended Stack No. : {stack}, Time left = {t} '
                requests.post(url)
        print("Number of programm completed : ", p)
        url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= No. of while loops = {p} and Flag is {Flag}'
        requests.post(url)
        t = a - \
            b
        print("Time left : ", t)
        check = t.total_seconds()
        print(count)
        check = t.total_seconds()
        p = p+1
        
        # for i in range(1, len(fList)+1):
            
        #     ele = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul/div/li[{}]/div/div[2]/button/div'.format(i))
                                                
        #     if ele.text == "Follow":
        #         follow = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul/div/li[{}]/div/div[2]/button'.format(i))
        #         follow.click()
        #         time.sleep(0.5)
        #         count = count+1
        #     if count == followB:
        #         break
        # print(count)
    url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text=Successfully Completed the Unfollower.py file execution!'
    requests.post(url)
login(usr1,pw)