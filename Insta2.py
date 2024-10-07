from ast import If
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime as dt
from selenium.webdriver.chrome.options import Options
import random

from sqlalchemy import true


# from chatBot import chat_ID
# from chatBot import bot_ID

from secret import pw
from user import usr1
from Required import followB
from Required import scrollN
from Required import pg
from Required import Max_Follow









#****************************************************************login Definition


def login(us,pswd,head):
    
    def wait(wait_time = 10):
        driver.implicitly_wait(wait_time)

    def get_login_page():
        driver.get('https://www.instagram.com/accounts/login/')

    def get_chrome_setting():
        driver.get('chrome://settings/')

    def cache_clear():
        driver.get('chrome://settings/resetProfileSettings?origin=userclick')
        wait()
        try: 
            wait()
            reset_button = driver.find_element(By.ID,'reset')
            wait()
            reset_button.send_keys(Keys.ENTER)
            wait()
            reset_button.click()
            reset_button = driver.find_element(By.XPATH,'//button[@id="reset"]')
            wait()
            reset_button.click()
            reset_button = driver.find_element(By.XPATH,'//button[@id="reset"]')
            wait()
            reset_button.click()
            wait()
            reset_button.click()
            wait()
            reset_button.click()
        except:
            time.sleep(10000)
            cache_clear()
        print("Reset Completed!")



    print('''Shortcut to pages : 
                                1  - @ghantaa
                                2  - @trolls_Official
                                3  - @tedthestoner
                                4  - @idiotic_sperm
                                5  - @error69
                                6  - @filtercopy
                                7  - @allindiabakchod
                                8  - @_dekhBhai_
                                9  - @fuddu_sperm
                                10 - @adultfamily
                                11 - @rvcjinsta
                                12 - OTHER_PAGE''')
    while(true):
        user_input = int(input("\nENTER THE OPTION NO. : "))
        if user_input == 1:
            pg = 'ghantaa'
            break
        elif user_input == 2:
            pg = 'trolls_Official'
            break
        elif user_input == 3:
            pg = 'tedthestoner'
            break
        elif user_input == 4:
            pg = 'idiotic_sperm'
            break
        elif user_input == 5:
            pg = 'error69'
            break
        elif user_input == 6:
            pg = 'filtercopy'
            break
        elif user_input == 7:
            pg = 'allindiabakchod'
            break
        elif user_input == 8:
            pg = '_dekhBhai_'
            break
        elif user_input == 9:
            pg = 'fuddu_sperm'
            break
        elif user_input == 10:
            pg = 'adultfamily'
            break
        elif user_input == 11:
            pg = 'rvcjinsta'
            break
        elif user_input == 12:
            pg = input('''  \n"OTHER_PAGE" option selected! Enter the page's ID - @''')
            break
        else:
            print("\nPlease Enter valid number!\n")

    print(f"\nTarget page selected is : @{pg}\n")
        
        # ***************************************************************initialize driver


    if head == 0:
        
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)  #headless chrome

    elif head == 1:

        driver = webdriver.Chrome()               #with Head Chrome


    
    
    
    get_login_page()
    # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= Insta2.py file started Sir!'
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
        
    except:
        pass
    
    
    #****** SEARCH   ********
    
    # search1 = driver.find_element_by_xpath('//span[text()="Search"]')
    # search1.click()
    # time.sleep(1)
    # search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
    # search_2.send_keys(pg)
    
    
    #        *********** Count of Scrolls **************** List of Accounts +++++++++++++++++++++++
    
    
    # count = 0
    # while count <3:
    #     search_2.send_keys(Keys.ENTER)
    #     count +=1 # count = count +1
    #     time.sleep(1)  
    
    driver.get(f"https://www.instagram.com/{pg}/")
    driver.implicitly_wait(10)

    
    followers = driver.find_element(By.XPATH,'(//a)[1]')
    followers.click()
   
    i = 0
    p = 1
    stack = 1
    check = 0
    count = 0
    error_sol1 = 0               #it resets all the previous error actions
    error3 = 0
    while check < Max_Follow:
    
       
        # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= While Loop entered successfully!'
        # requests.post(url)
        
        try:
            fBody  = driver.find_element(By.XPATH,"//div[@class='_aano']")
            print("\nfBody found!\n")
        except:
            if error3 <= -3:
                print("Error3 found! fBody is unable to be found.\nStarting the chrome driver reset function (to clear all cache!) and then trying again the program from Login page!")
                cache_clear()
                login()
            driver.get(f"https://www.instagram.com/{usr1}/")
            error3 -= 1
            print(f"\n{-error3}. fBody NOT found! Page reloaded to {usr1}\n")
            continue        
        
        scroll = 0
        while scroll < scrollN : # scroll N times
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            scroll += 1
            print(f"scrolled no. {scroll} ")
            time.sleep(2)
            

        fList  = driver.find_elements(By.XPATH,"//div[@class='_aano']//li")
        print("fList len is {}".format(len(fList)))    
        driver.implicitly_wait(10)
        # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= fList len is {len(fList)}'
        # requests.post(url)
        
        
        #*************************** CLick Follow***************************
        
        
        # for i in range(1, len(fList)+1):
            
            
        #     follow = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul/div/li[{}]/div/div[2]/button'.format(i))
        #     follow.click()
        #     time.sleep(0.5)
        #     try: 
        #         time.sleep(1)
        #         driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[1]').click()
        #     except:
        #         pass
        #     count = count+1
        #     if count == followB:
        #         break
        # print(count)
        
        
        stack = 1
        error1 = 1                  #error for not following in consecutive for loops
        error2 = 1                  #error related to unable to get inside loop

        for i in range(i+1, len(fList)+1):
            
            if error2 == 1:
                print("\nEntered the for loop of lists after while\n")
                error2 = 0
                
                
            try:
                ele = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button/div')
                print('\n\n"Follow" element found')
            except:
                driver.get(f"https://www.instagram.com/{pg}/")
                print(f'Following element not found. Page {pg} reloaded')
                driver.implicitly_wait(10)


                followers = driver.find_element(By.XPATH,'(//a)[1]')
                followers.click()
   
                print(f"Element 'Follow' Not found, loading the page {pg} again")
                # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text=div is 5!!!!! '
                # requests.post(url)b
                break
                                                
            if ele.text == "Follow":
                
                try:
                    follow = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button')
                    follow.click()
                    check = check + 1
                    print("Followed : ",check)
                    t=random.randint(10,40)
                    print(f"Sleep : {t} seconds\n\n")
                    time.sleep(t)
                    error1 =0
                    error_sol1 = 0          #previous error solved

                except:
                    print("Not followed")
                    pass
                
                count = count+1
            if count >= followB:
                print("Ended Stack No. : ", stack)
                # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text=Ended Stack No. : {stack} of program : {p} & followed : {check}'
                # requests.post(url)
                print(dt.datetime.now())
                stack = stack+1
                time.sleep(600)
                
                count =0
        print("Number of programm completed : ", p)
        
        
        if error1==1 or error2==1:
            
            error_sol1 -=1
            print(f"{-error_sol1}. Entered error resolver")
            if error_sol1 == -3:
                print(f"error_sol1 activated, reopening the page {pg}")
                if error1 == 1:
                    print("Error1 : Not entering for loop")
                if error2 == 1:
                    print("Error2 : Not clicking 'Follow'")
                driver.get(f"https://www.instagram.com/{pg}/")
                driver.implicitly_wait(10)
                followers = driver.find_element(By.XPATH,'(//a)[1]')
                followers.click()
                error_sol1 = 0               #it resets all the previous error actions

            
        
        
        
        
        # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= No. of programs Ended = {p} '
        # requests.post(url)
    # url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text= Successfully Followed : {check}. Porgram Terminates Here.'
    # requests.post(url)
        p = p+1
    


def follow_main(head):
    login(usr1,pw,head)