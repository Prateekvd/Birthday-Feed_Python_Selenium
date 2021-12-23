from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options
class birthDaysToday():
    def getBirthdaysList(self):
        fbUrl = "https://www.facebook.com"
        global driver
        # driver.implicitly_wait(10)
        # opening facebook.com
        driver.get(fbUrl)
        # entering credentials

        phNumberOrEmail = "credential"
        password = "write your password"
        driver.find_element_by_xpath("//input[@id='email']").send_keys(phNumberOrEmail)
        driver.find_element(By.XPATH,"//input[@id='pass']").send_keys(password)
        driver.find_element_by_name("login").click()


        driver.get("https://www.facebook.com/events/birthdays/")

        feed = 'Happy Birthday !'

        element = driver.find_elements_by_xpath("//*[@class ='enter_submit\
               uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea\
                          inlineReplyTextArea mentionsTextarea textInput']")

        cnt = 0

        for el in element:
            cnt += 1
            element_id = str(el.get_attribute('id'))
            XPATH = '//*[@id ="' + element_id + '"]'
            post_field = driver.find_element_by_xpath(XPATH)
            post_field.send_keys(feed)
            post_field.send_keys(Keys.RETURN)
            print("Birthday Wish posted for friend" + str(cnt))

        # Close the browser
        driver.close()

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
        # Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2
        })
driverLocation = "E:\\PythonProjects\\libs\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(executable_path=driverLocation,options=opt)


dt = birthDaysToday()
dt.getBirthdaysList()

