import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class seleniumRT():

    '''
    #driver.set_page_load_timeout(10)
    #driver.get("localhost:8080/RetailPlusStoreBackend/login/auth")
    #try:
    #   driver.find_element_by_name("j_username").send_keys("711001")
    #    driver.find_element_by_name("j_password").send_keys("7110ne")
    #    driver.find_element_by_id("submit").click()
    '''


    def createTicket(self,Subject,message):
        try:
            driver = webdriver.Firefox(executable_path="C:\\WoLFPaCK\\Python Projects\\Selenium Project\\drivers\\geckodriver.exe")
            driver.set_page_load_timeout(10)
            driver.get("https://rt.apolloglobal.net/")
            driver.find_element_by_name("user").send_keys("luis@apolloglobal.net")
            driver.find_element_by_name("pass").send_keys("password")
            driver.find_element_by_class_name("button").click()
            select = Select(driver.find_element_by_name("Queue"))
            select.select_by_visible_text('Service Desk - iConnect')
            driver.find_element_by_name("Subject").send_keys(Subject)
            driver.find_element_by_name("Owner").clear()
            driver.find_element_by_name("Owner").send_keys("luis@apolloglobal.net")
            time.sleep(1)
            driver.switch_to.frame(frame_reference=driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']"))
            driver.find_element_by_xpath("//body[@contenteditable='true']").send_keys(message)
            driver.switch_to_default_content()
            #driver.find_element_by_xpath("//*[@id='SubmitTicket']/div[2]/input").click()
            print("SUCCESS")
            time.sleep(10)
            driver.quit()
        except:
            print("System has experienced an unexpected exception")



if __name__ == '__main__':
    autoRT = seleniumRT()
    Subject = input("Subject: ")
    message = input("Message: ")
    autoRT.createTicket(Subject,message)
