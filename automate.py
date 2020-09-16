from selenium import webdriver

''' 
choosing my driver
if u have chrome u can choose that using
driver = webdriver.Chrome()

'''
driver = webdriver.Firefox()


# fetching whatsapp web

driver.get("https://web.whatsapp.com/")

# scan your  Whatsapp Web QR code

name = input("Enter the Name of the user or the group: ")

msg = input("Enter Your Message: ")

# count is the number of times the msg needs to be sent
count = int(input("Enter the count: "))


##############################################################################

user_get = driver.find_element_by_xpath(f'//span[@title= "{name}"]')
user_get.click()


msg_box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

# sending n count msgs
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button")
    button.click()

print("Message sent")