import os
import time
import random
from fillout import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(THIS_FOLDER, "chromedriver.exe")

def main():
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.geoguessr.com/signin")
    driver.maximize_window()
    login(driver)

    while True:
        time.sleep(random.uniform(4,6)) # randomizing time to avoid potential detection
        loadGame(driver)
        time.sleep(random.uniform(0.1, 1))
        playGame(driver)

def click(wait, xpath):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    except:
        pass

def isVisible(wait, xpath):
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

def login(driver):
    wait = WebDriverWait(driver, 5)
    attempts = 0
    while attempts < 5:
        try:
            username_area = driver.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/main/div/div/form/div/div[1]/div[2]/input")
            username_area.send_keys(USERNAME)
            password_area = driver.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/main/div/div/form/div/div[2]/div[2]/input")
            password_area.send_keys(PASSWORD)
            click(wait, "//*[@id='__next']/div/div[2]/div[1]/main/div/div/form/div/div[3]/div/button/div")
            break
        except:
            attempts+=1
            time.sleep(0.5)

    isVisible(wait, "//*[@id='__next']/div/div[2]/div[1]/header/div[3]/div[2]/div")
    loadMap(driver)

def loadMap(driver):
    attempts = 0
    while attempts < 5:
        try:
            driver.get("https://www.geoguessr.com/maps/62786bdfa2262401fa60c0cb")
            break
        except:
            attempts+=1
            time.sleep(0.5)

def loadGame(driver):
    attempts = 0
    while attempts < 5:
        try:
            wait = WebDriverWait(driver, 5)
            click(wait, "//*[@id='__next']/div/div[2]/div[1]/main/div/div/div[1]/div[3]/div/div/button/div")
            click(wait, "//*[@id='__next']/div/div[2]/div[1]/main/div/div[2]/div/div/div[3]/button/div")
            break
        except:
            attempts+=1
            time.sleep(0.5)

def playGame(driver):
    for r in range(5):
        time.sleep(random.uniform(0.1, 1))
        navigateToMap(driver)

        time.sleep(random.uniform(0.1, 1))
        makeGuess(driver)

        time.sleep(random.uniform(0.1, 1))
        nextRound(driver)

    time.sleep(random.uniform(0.1, 1))
    viewSummary(driver)

    time.sleep(random.uniform(0.1, 1))
    playAgain(driver)
    
def navigateToMap(driver):
    attempts = 0
    while attempts < 5:
        try:
            l = driver.find_element_by_xpath("//*[@id='__next']/div/div/main/div/div/div[4]/div/div[3]/div/div/div/div/div[2]/div[2]")
            action = webdriver.common.action_chains.ActionChains(driver)
            action.move_to_element_with_offset(l, random.randint(5,50), random.randint(5,50)).click().perform()
            break
        except:
            attempts+=1
            time.sleep(0.5)

def makeGuess(driver):
    attempts = 0
    while attempts < 5:
        try:
            wait = WebDriverWait(driver, 5)
            click(wait, "//*[@id='__next']/div/div/main/div/div/div[4]/div/div[4]/button/div")
            break
        except:
            attempts+=1
            time.sleep(0.5)    

def nextRound(driver):
    attempts = 0
    while attempts < 5:
        try:
            wait = WebDriverWait(driver, 5)
            click(wait, "//*[@id='__next']/div/div/main/div[2]/div/div[2]/div/div[1]/div/div[4]/button/div")
            break
        except:
            attempts+=1
            time.sleep(0.5) 

def viewSummary(driver):
    attempts = 0
    while attempts < 5:
        try:
            wait = WebDriverWait(driver, 5)
            click(wait, "//*[@id='__next']/div/div/main/div[2]/div/div[2]/div/div[1]/div/div[4]/div/button/div")
            break
        except:
            attempts+=1
            time.sleep(0.5) 
    
def playAgain(driver):
    attempts = 0
    while attempts < 5:
        try:
            wait = WebDriverWait(driver, 5)
            click(wait, "//*[@id='__next']/div/div/main/div[2]/div/div[2]/div/div[1]/div/div[4]/div/a[1]/div")
            break
        except:
            attempts+=1
            time.sleep(0.5)

if __name__ == "__main__":
    main()