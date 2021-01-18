import selenium

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# time for pausing between navigation
import time
import itertools
import pandas as pd

	# Using Chrome to access web

driver = webdriver.Chrome(ChromeDriverManager().install())

	# Open the website
driver.get('https://pvpoke.com/team-builder/')

  # Determine the league the user is playing
league = input("What league are you playing in? (great, ultra or master): ")

if league == 'ultra':
    time.sleep(1)
    league_select_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".league-select")))
    league_select_button.click()
    
    ultra = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".league-select")))
    ultra.send_keys('ultra')

if league == 'master':
    time.sleep(1)
    league_select_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".league-select")))
    league_select_button.click()
    
    ultra = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".league-select")))
    ultra.send_keys('master')
    
  # Determine the desired format
premier = input("What format are you playing in? (premier, holiday, kanto, or normal: ")

if premier == 'premier':
    time.sleep(1)
    league_select_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".format-select")))
    league_select_button.click()
    
    ultra = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".format-select")))
    ultra.send_keys('premier')
    
    
if premier == 'holiday':
    time.sleep(1)
    league_select_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".format-select")))
    league_select_button.click()
    
    ultra = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".format-select")))
    ultra.send_keys('holiday')
    
if premier == 'kanto':
    time.sleep(1)
    league_select_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".format-select")))
    league_select_button.click()
    
    ultra = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".format-select")))
    ultra.send_keys('kanto')
    
    # Determine the number of pokemon and their names.
poke = []
n = int(input("Enter the number of Pokemon you have ready : "))
for i in range(0, n): 
    ele = (input()) 
  
    poke.append(ele) # adding the element 
      
  # Creating a list of all the conbinations of pokemon
permutations_list = list(itertools.combinations(poke, 3))

scoreboard = {
        "A" : 4,
        "B" : 3,
        "C" : 2,
        "D" : 1,
        "F" : 0
        }
  # This function controls the website. It enters in the names of three pokemon, determines their score and then returns the website to its original state. 
def threepoke(pokelist):
    time.sleep(1)
    add_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[3]/div/div/div/button")))
    add_button.click()
    time.sleep(1)
    add_pokemon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[5]/div/div[3]/div/input")))
    add_pokemon.send_keys(pokelist[0])
    #time.sleep(2)
    add = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".save-poke")))
    add.click()
            
    add_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[3]/div/div/div/button")))
    add_button.click()
    
    add_pokemon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[5]/div/div[3]/div/input")))
    add_pokemon.send_keys(pokelist[1])
    
    add = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".save-poke")))
    add.click()
    
    
    add_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[3]/div/div/div/button")))
    add_button.click()
    
    add_pokemon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[5]/div/div[3]/div/input")))
    add_pokemon.send_keys(pokelist[2])
    
    add = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".save-poke")))
    add.click()
    
    rate = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".rate-btn")))
    rate.click()
    time.sleep(1)
    
    
    score = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".coverage .grade")))
    
    coverage = driver.find_element(By.CSS_SELECTOR, ".coverage .grade").text
    bulk = driver.find_element(By.CSS_SELECTOR, ".bulk .grade").text
    safety = driver.find_element(By.CSS_SELECTOR, ".safety .grade").text
    consistency = driver.find_element(By.CSS_SELECTOR, ".consistency .grade").text
    

    score2 = scoreboard[coverage] + scoreboard[bulk] + scoreboard[safety] + scoreboard[consistency]
    
    time.sleep(1)
    remove = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".clear .remove")))
    remove.click()

    confirm = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".remove-poke-confirm:nth-child(1) .yes")))
    confirm.click()
    
    
    remove2 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".clear .remove")))
    remove2.click()
    confirm2 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".remove-poke-confirm:nth-child(1) .yes")))
    confirm2.click()
    
    remove3 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".clear .remove")))
    remove3.click()
    confirm3 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".remove-poke-confirm:nth-child(1) .yes")))
    confirm3.click()
    
    return score2

    
length = len(permutations_list)

print('Calculations Left ')   # This is optional, it helps let the user know how many calculations are remaining and that everything is still running smoothly

results = pd.DataFrame()

  # The wrapper function that collects all of the scores and puts the teams in order based on their score. 
for i in range(0, length): 
    print(length - i)
    string = (permutations_list[i][0] + ' ' + permutations_list[i][1] + ' ' + permutations_list[i][2])
    string2 = threepoke(permutations_list[i])
    coverage = driver.find_element(By.CSS_SELECTOR, ".coverage .grade").text
    bulk = driver.find_element(By.CSS_SELECTOR, ".bulk .grade").text
    safety = driver.find_element(By.CSS_SELECTOR, ".safety .grade").text
    consistency = driver.find_element(By.CSS_SELECTOR, ".consistency .grade").text
    string3 = (coverage + ' ' + bulk + ' ' + safety + ' ' + consistency)
    results = results.append({'Team' : string, 'Score' : string2, 'Rating' : string3}, ignore_index=True)

look = results.sort_values(by=['Score'], ascending=False)
print(look)
