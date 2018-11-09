import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class seleniumRT():

    def __init__(self):
            print("Opening RT Site")
            options = Options()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(firefox_options=options, executable_path="C:\\WoLFPaCK\\Python Projects\\Selenium Project\\drivers\\geckodriver.exe")
            #driver = webdriver.Firefox(executable_path="C:\\WoLFPaCK\\Python Projects\\Selenium Project\\drivers\\geckodriver.exe")
            self.driver.set_page_load_timeout(10)
            self.driver.get("https://rt.apolloglobal.net/")
            self.driver.find_element_by_name("user").send_keys("luis@apolloglobal.net")
            self.driver.find_element_by_name("pass").send_keys("password")
            self.driver.find_element_by_class_name("button").click()
            self.actions = ActionChains(self.driver)

    def createTicket(self,Subject,message):
        try:
            self.driver.get("https://rt.apolloglobal.net/")
            select = Select(self.driver.find_element_by_name("Queue"))
            select.select_by_visible_text('Service Desk - iConnect')
            ticketSubject = "[As][Sup] " + Subject
            self.driver.find_element_by_name("Subject").send_keys(ticketSubject)
            self.driver.find_element_by_name("Owner").clear()
            self.driver.find_element_by_name("Owner").send_keys("luis@apolloglobal.net")
            time.sleep(1)
            self.driver.switch_to.frame(frame_reference=self.driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']"))
            self.driver.find_element_by_xpath("//body[@contenteditable='true']").send_keys(message)
            self.driver.switch_to_default_content()
            self.driver.find_element_by_xpath("//*[@id='SubmitTicket']/div[2]/input").click()
            print("SUCCESS")
        except:
            print("System has experienced an unexpected exception")

    def resolve(self,Subject,message):
        try:
            ticketSubject = "[As][Sup] " + Subject
            self.driver.find_element_by_link_text(ticketSubject).click()
            Action_hover = self.driver.find_element_by_id("page-actions") #hover to Actions
            self.actions.move_to_element(Action_hover).perform()          #hover to Actions
            self.driver.find_element_by_id("page-actions-resolve").click() #click Resolve
            time.sleep(1)
            self.driver.switch_to.frame(frame_reference=self.driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']"))
            self.driver.find_element_by_xpath("//body[@contenteditable='true']").send_keys(message)
            self.driver.switch_to_default_content()
            self.driver.find_element_by_xpath("//*[@id='SubmitTicket']/div[2]/input").click()
            print("Concern has been resolved")
        except:
           print("System has experienced an unexpected exception")

    def rtInput(self):
        Subject = input("Subject: ")
        message = input("Message: ")
        return Subject, message



if __name__ == '__main__':
    autoRT = seleniumRT()
    while(True):
        user_input = input('Enter "a" to Create \nEnter "b" to Resolve\nEnter "c" to close: ')
        if user_input == "a":
            Subject,message = autoRT.rtInput()
            autoRT.createTicket(Subject,message)

        elif user_input == "b":
            autoRT.driver.get("https://rt.apolloglobal.net/")
            link = autoRT.driver.find_elements_by_partial_link_text("[As][Sup]")
            openRT = len(link)
            for eachLink in link:
                print(eachLink.text)

            if (openRT == 0):
                print("There are no Tickets found")
            else:
                Subject,message = autoRT.rtInput()
                autoRT.resolve(Subject,message)

        elif user_input == "c":
            autoRT.driver.quit()
            break

