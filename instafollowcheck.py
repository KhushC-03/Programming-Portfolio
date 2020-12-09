import random, json, time, os, keyboard, re, sys, itertools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
numbers = ['0','1','2','3','4','5','6','7','8','9']
def login():
    I1 = input('Instagram profile link: ')
    email = input('Instagram Email: ')
    password = input('Instagram Password: ')
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'   
    options.add_argument('user-agent={0}'.format(user_agent))
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_driver = "C:\\webdrivers\\chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
    driver.get('https://www.instagram.com/') 
    time.sleep(2)
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]")))
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').click()
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(email)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').click()
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    time.sleep(1)    
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(1)
    element1 = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/div[1]/div/span')))
    time.sleep(1)
    driver.get(I1)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    metatag = (soup.find_all('meta')[13])
    metasplit = str(metatag).split(',')[0]
    following  = str(metatag).split(',')[1]
    numberlist = []
    for letters in metasplit:
        if letters in numbers:
            numberlist.append(letters)
        else:
            pass
    a1 = (str(numberlist).replace(',',''))
    a2 = a1.replace('[','')
    a3 = a2.replace(']','')
    a4 = a3.replace("'",'')
    followcount = int(re.sub(r"\s+", "", a4, flags=re.UNICODE)) 
# loop followers 
    element2 = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    time.sleep(1)
    element3 = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[1]/div/h1')))
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.perform()
    print(f'You have {followcount} followers')
    while True:
        print('Looping through followers', end='\r')
        if len(driver.find_elements_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{followcount}]')) > 0:
            break
        else:        
            actions.send_keys(Keys.END)
            actions.perform()
    soup1 = BeautifulSoup(driver.page_source,'html.parser')
    div = soup1.find_all("div", class_="enpQJ")
    first_follower = (div[0].text.split('<')[0])
    i = -1
    loop_tags = []
    for i in range(len(div) - 1):
        i = i + 1
        followers = (div[i].text.split()[0])
        loop_tags.append(followers)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
    time.sleep(1)
# loop following 
    element4 = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')))
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    element5 = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[1]/div/h1')))    
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.perform()
    following  = str(metatag).split(',')[1]
    followingcount = int(following.split()[0])
    print(f'You are following {followingcount} accounts')
    while True:
        print('Looping through following',end='\r')  
        if len(driver.find_elements_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{followingcount}]')) > 0:
            break
        else:       
            actions.send_keys(Keys.END)
            actions.perform()
    soup2 = BeautifulSoup(driver.page_source,'html.parser')
    div = soup2.find_all("div", class_="enpQJ")
    first_following = (div[0].text.split('<')[0])
    new_session  = 'New Session {}\n'.format(I1)
    loop_following_tags = []
    for i,e in enumerate(range(len(div) - 1),start=0):
        following = div[i].text.split()[0]
        loop_following_tags.append(following)
    if followcount > followingcount:
        for following in loop_following_tags:
            if following in loop_tags:
                print(f'You follow {following} and they follow you back')
                txt = ('You follow {} and they follow you back\n'.format(following))
            else:
                print(f"You follow {following} and they don't follow you back")
                txt1 = ("You follow {} and they don't follow you back\n".format(following))
    else:
        for following in loop_tags:
            if following in loop_following_tags:
                print(f'You follow {following} and they follow you back')
                txt1 = ('You follow {} and they follow you back\n'.format(following))
            else:
                print(f"You follow {following} and they don't follow you back")
                txt1 = ("You follow {} and they don't follow you back\n".format(following))
    driver.quit()

try:
    login()
except Exception as ex:
    print(ex)
