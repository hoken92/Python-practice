from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")

#first riddle fields
inputField_One = browser.find_element(By.ID, "r1Input")
buttonOne = browser.find_element(By.CSS_SELECTOR, "button#r1Btn")
firstConfirm = browser.find_element(By.CSS_SELECTOR, "div#passwordBanner h4")

#second riddle fields
inputField_Two = browser.find_element(By.CSS_SELECTOR, "input#r2Input")
buttonTwo = browser.find_element(By.CSS_SELECTOR, "button#r2Butn")
secondConfirm = browser.find_element(By.CSS_SELECTOR, "div#successBanner1 h4")

#third riddle fields
jessica = browser.find_element(By.XPATH, "//p[text()='3000'] /../span")
jessicaValue =browser.find_element(By.XPATH, "//p[text()='3000']")
bernard = browser.find_element(By.XPATH, "//p[text()='2000'] /../span")
bernardValue =browser.find_element(By.XPATH, "//p[text()='2000']")

inputField_Three = browser.find_element(By.CSS_SELECTOR, "input#r3Input")
buttonThree = browser.find_element(By.CSS_SELECTOR, "button#r3Butn")
thirdConfirm = browser.find_element(By.CSS_SELECTOR, "div#successBanner2 h4")

#lastcheck fields
buttonFour_Locator = "//button[@name='checkButn']"
fourthConfirm_Locator = "//div[@id='trialCompleteBanner']/h4"
    

def firstRiddle():
    #This inputs rock into the first field
    inputField_One.send_keys("rock")

    #Checks the answer
    buttonOne.click()
    
    #Checks if the banner is shown when button is clicked
    assert firstConfirm.text == "bamboo"
    
    #Returns the value in console
    print(firstConfirm.text)

def secondRiddle():
    #This inputs the answer from above into the next field
    password = firstConfirm.text
    inputField_Two.send_keys(password)

    #Clicks the answer button
    buttonTwo.click()

    #This is confirm the banner appears and is correct
    assert secondConfirm.text == "Success!"

    #Returns the value in console
    print(secondConfirm.text)



def thirdRiddle():
    #This checks who has the higher amount of money
    if jessicaValue.text > bernardValue.text:
        inputField_Three.send_keys(jessica.text)

    elif jessicaValue.text < bernardValue.text:
        inputField_Three.send_keys(bernard.text)

    buttonThree.click()
    assert thirdConfirm.text == "Success!"

    #Returns the value in console
    print(thirdConfirm.text)

def finalCheck():
    buttonFour = browser.find_element(By.XPATH, buttonFour_Locator)
    buttonFour.click()
    fourthConfirm = browser.find_element(By.XPATH, fourthConfirm_Locator)
    assert fourthConfirm.text == "Trial Complete"

    #Returns the value in console
    print(fourthConfirm.text)

firstRiddle()
secondRiddle()
thirdRiddle()
finalCheck()