import time 
import sys 
import os 
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
  
# The text that you want to convert to audio 
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 

  
# Saving the converted audio in a mp3 file named 
# welcome  

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def run():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    sys.stdin = open('auth.txt','r')
        
    # Getting username, password and product to be searched
    USER = input()
    PWD = input()
    product = input()


    # Navigating to Amazon's site 
    driver.get("https://amazon.in")

    # Seaching for the product
    search = driver.find_element_by_id("twotabsearchtextbox")
    search.send_keys(product)
    search.send_keys(Keys.RETURN)

    # print(driver.page_source)

    try:
        main = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]"))
        )

        # Seaching for the product
        st = driver.find_element_by_id("high-price")
        st.send_keys("5000")
        driver.find_element_by_xpath("//*[@id='a-autoid-1']/span/input").click()
        #st.send_keys(Keys.RETURN)
        
        # Selecting the best selling item
        item = driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[3]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")
        price = driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[3]/div/span/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/a/span[1]/span[2]/span[2]")
        print(item.text,price.text)

        mytext = item.text + "Cost is " + price.text
        speak(mytext) 
        
        item.click()
        driver.switch_to.window(driver.window_handles[1])
        
        # Adding to cart 
        cart = driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()
        # print(driver.window_handles)
        cart = driver.find_element_by_xpath("//*[@id='nav-cart-count']").click()
        cart = driver.find_element_by_xpath("//*[@id='sc-buy-box-ptc-button']/span/input").click()
        
        # Checkout
        username = driver.find_element_by_xpath("//*[@id='ap_email']")
        username.send_keys(USER)
        username.send_keys(Keys.RETURN)
        
        pwd = driver.find_element_by_xpath("//*[@id='ap_password']")
        pwd.send_keys(PWD)
        pwd.send_keys(Keys.RETURN)
        
        time.sleep(15)
        driver.find_element_by_xpath("//*[@id='address-book-entry-0']/div[2]/span/a").click()
        driver.find_element_by_xpath("//*[@id='shippingOptionFormId']/div[1]/div[2]/div/span[1]/span/input").click()
        
        try:
            driver.find_element_by_xpath("//*[@id='pp-bqBjaZ-121']").click()
            driver.find_element_by_xpath("//*[@id='pp-bqBjaZ-124']/span/input").click()
            driver.find_element_by_xpath("//*[@id='placeYourOrder']/span/input").click()
        except:
            print("Thank You ¯\◉◡◉/¯")
            # driver.quit()
        # //*[@id="pp-F7J0XO-121"]
        # //*[@id="pp-F7J0XO-121"]

    except:
        driver.quit()


    # print(main.text)
    # print(driver.current_window_handle)
        
    # time.sleep(5)
    # driver.quit()
# run()
