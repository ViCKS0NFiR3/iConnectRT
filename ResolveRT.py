import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options


print("Opening RT site..")
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, executable_path="C:\\WoLFPaCK\\Python Projects\\Selenium Project\\drivers\\geckodriver.exe")
actions = ActionChains(driver)
driver.set_page_load_timeout(10)
driver.get("https://rt.apolloglobal.net/")
driver.find_element_by_name("user").send_keys("luis@apolloglobal.net")
driver.find_element_by_name("pass").send_keys("password")
driver.find_element_by_class_name("button").click()

link = driver.find_elements_by_partial_link_text("[As][Sup]")
len(link)
for eachLink in link:
   print(eachLink.text)
Subject = input("Subject: ")
message = input("Message: ")
ticketSubject = "[As][Sup]" + Subject

driver.find_element_by_link_text(ticketSubject).click()

Action_hover = driver.find_element_by_id("page-actions") #hover to Actions
actions.move_to_element(Action_hover).perform()          #hover to Actions

driver.find_element_by_id("page-actions-resolve").click() #click Resolve

time.sleep(1)
driver.switch_to.frame(frame_reference=driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']"))
driver.find_element_by_xpath("//body[@contenteditable='true']").send_keys("message")
driver.switch_to_default_content()
driver.find_element_by_xpath("//*[@id='SubmitTicket']/div[2]/input").click()

print("Concern has been resolved")

driver.quit()

