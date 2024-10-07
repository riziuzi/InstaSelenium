from email.quoprimime import header_check
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from Required import t_unfollow
import datetime as dt
from chatBot import chat_ID
from chatBot import bot_ID
import requests
from Required import Max_Follow
import random


import random
from secret import pw
from user import usr1
from Required import followB
from Required import scrollN









def login(us,pswd,head):
    
    
    
    # *********************************************************initialize driver
    if head == 0:
        
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)  #headless chrome

    elif head == 1:

        driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')               #with Head Chrome
    
    
    
    
    
    
    # driver.get('https://www.instagram.com/')
    driver.get('https://www.instagram.com/accounts/login/')
    # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= Insta3Unfollower.py file started Sir!'
    # requests.post(url)
    # accepting the cookies
    try:
        cookies_accept= driver.find_element(By.XPATH,'//button[text()="Accept"]')
        cookies_accept.click()
        driver.implicitly_wait(10)
    except:
        pass
    
    driver.implicitly_wait(10)
    username = driver.find_element(By.NAME,'username')
    username.click()
    username.send_keys(us)
    
    password = driver.find_element(By.NAME,'password')
    password.click()
    password.send_keys(pswd)
    

    log_in = driver.find_element(By.XPATH,'//div[text()="Log In"]')
    log_in.click()
    
    driver.implicitly_wait(10)
    # credential storage
    try:
        credentials= driver.find_element(By.XPATH,'//button[text()="Not Now"]')
        credentials.click()
        driver.implicitly_wait(10)
    except:
        pass

    #  notifications
    try:
        notifications = driver.find_element(By.XPATH,'//button[text()="Not Now"]')
        notifications.click()
        driver.implicitly_wait(10)
    except:
        pass
    
    
    #****** SEARCH   ********
    
    # search1 = driver.find_element_by_xpath('//span[text()="Search"]')
    # search1.click()
    # time.sleep(1)
    # search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
    # search_2.send_keys(usr1)
    
    
    #        *********** Count of Scrolls **************** List of Accounts +++++++++++++++++++++++
    
    
    count = 0
    # while count <3:
    #     search_2.send_keys(Keys.ENTER)
    #     count +=1 # count = count +1
    #     time.sleep(1)  
    driver.get(f"https://www.instagram.com/{usr1}/")
    driver.implicitly_wait(10)
    following = driver.find_element(By.XPATH,'(//a)[3]')
    following.click()
    driver.implicitly_wait(10)
    
    
    check = 0
    i = 0
    p = 1
    Flag = 1
    stack = 1
    # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= While loop entered successfully!'
    # requests.post(url)
    
    error_sol1 = 0               #it resets all the previous error actions
    while check < Max_Follow:   
        driver.implicitly_wait(10)
     
        try:
            driver.implicitly_wait(10)
            time.sleep(2)
            following = driver.find_element(By.XPATH,'(//a)[3]')
            following.click()
            time.sleep(5)
        except:
            pass
        
        try:
            fBody  = driver.find_element(By.XPATH,"//div[@class='_aano']")
            print("\nfBody found!\n")
        except:
            driver.get(f"https://www.instagram.com/{usr1}/")
            print(f"\nfBody NOT found! Page reloaded to {usr1}\n")
            break
        scroll = 0
        while scroll < scrollN : # scroll N times
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            scroll += 1
            print(f"scrolled no. {scroll} ")
            time.sleep(1)

        fList  = driver.find_elements(By.XPATH,"//div[@class='_aano']//li")
        # print("fList len is {}".format(len(fList)))   
        # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= fList len is {len(fList)}'
        # requests.post(url) 
        driver.implicitly_wait(10)
        
        
        
        #*************************** CLick UnFollow***************************
        stack = 1
        error1 = 1                  #error for not following in consecutive for loops
        error2 = 1                  #error related to unable to get inside loop
        
        for i in range(i+1, len(fList)+1):
            
            if error2 == 1:
                print("\nEntered the for loop of lists after while\n")
                error2 = 0
                
            try:
                ele = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li[{}]/div/div[2]/button/div'.format(i))
                print('\n\n"Following" element found')
            except:
                driver.get(f"https://www.instagram.com/{usr1}/")
                print(f'Following element not found. Your page {usr1} reloaded')
                # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text=div is 5!!!!! '
                # requests.post(url)b
                break
                
            if ele.text == "Following":
                time.sleep(t_unfollow)
                unfollow = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li[{}]/div/div[2]/button'.format(i))
                unfollow.click()
                time.sleep(t_unfollow)
                count = count+1
                try:
                    unfollow2 = driver.find_element(By.XPATH , '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
                    driver.implicitly_wait(10)
                    unfollow2.click()
                    check += 1
                    print("Unfollowed : ", check)
                    t=random.randint(10,40)
                    print(f"Sleep : {t} seconds\n\n")
                    time.sleep(t)
                    error1 =0
                    error_sol1 = 0          #previous error solved

                except:
                    driver.get(f"https://www.instagram.com/{usr1}/")
                    print("Unable to unFollow, Page Reloaded")
                    break
                
            if count >= followB:
                print("Ended Stack No. : ", stack)
                
                
                # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text=Ended Stack No. : {stack}, Time left = {t} '
                # requests.post(url)
                stack = stack+1
                b = dt.datetime.now()
                
                print('Time  : ', b)
                time.sleep(600)
                b = dt.datetime.now()
                print('Time  : ', b)
                count =0
                
        print("Number of programm completed : ", p)
        # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= No. of while loops = {p} and Flag is {Flag}'
        # requests.post(url)
        
        if error1==1 or error2==1:
            
            error_sol1 -=1
            print(f"{-error_sol1}. Entered error resolve checker (granted if >= 3)")
            if error_sol1 == -3:
                
                if error1 == 1:
                    print("Error1 : Not entering for loop")
                if error2 == 1:
                    print("Error2 : Not clicking 'Follow'")
                print(f"error_sol1 activated, reopening the page {usr1}")
                driver.get(f"https://www.instagram.com/{usr1}/")
                driver.implicitly_wait(10)
                error_sol1 = 0               #it resets all the previous error actions
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
    # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text=Successfully Completed the Insta3Unfollower.py file execution!'
    # requests.post(url)
    p = p+1
    
    
    
    
    
    
def unfollow_main(head):
    login(usr1,pw,head)
    
    
if __name__ == "__main__":
    unfollow_main(1)