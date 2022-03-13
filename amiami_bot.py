import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


driver.implicitly_wait(5)

#AmiAmi Figure Link
driver.get("insert link here")

buyButton = False
#Try checking if its in stock.
while not buyButton:
    try:
        #If in-stock, will add to cart and go through the checkout process
        itemStock = driver.find_element(By.CLASS_NAME, 'item-detail__limit').is_displayed
        print("Item in stock.")
        break

    except NoSuchElementException:
        #If not in-stock, will refresh the page every 5 seconds
         print("Item not in stock")
         time.sleep(5)
         driver.refresh()

#Checkout
addToCartBtn = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div/div/div/section[1]/div/div[3]/div[1]/div/div/button[2]/span')
addToCartBtn.click()

proceedToCheckout = driver.find_element(By.XPATH, '//*[@id="form3"]/div/span/input')
proceedToCheckout.click()

#Login info
email = driver.find_element(By.NAME, "email")
email.send_keys("Insert email")

passwd = driver.find_element(By.NAME, "password")
passwd.send_keys("insert")

#Continue checkout
submitButton = driver.find_element(By.CLASS_NAME, 'btn.btn-submit.btn-mini')
submitButton .click()

submitButton2  = driver.find_element(By.CLASS_NAME, 'btn.btn-submit')
submitButton2.click()

submitButton3 = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/section/div[4]/button[2]')
submitButton3.click()

submitButton4 = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/section[3]/div[2]/div[2]/span/label/span')
submitButton4.click()

submitButton5 = driver.find_element(By.CLASS_NAME, 'btn.btn-submit')
submitButton5.click()

preorder = driver.find_element(By.CLASS_NAME, 'btn.btn-submit')
preorder.click()

print("Order finished. Exiting...")
exit()