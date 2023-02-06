# THIS IS BACKEND CODE RUNNING ON A SERVER

import anvil.server
from anvil import *
import pyperclip
import anvil.media
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium import webdriver
from datetime import datetime
import os

# Click this link to set up Anvil Uplink: https://anvil.works/docs/uplink/quickstart
anvil.server.connect('7KG5V2KB73DLPM54FTOAK2IU-YXJP2EP47RSSXLSY')

# Used for logging
def gettime():
    time = str(datetime.now())[:-5]
    return '['+time+']'

# Anvil app calls this function to send text. It takes the message, user_list, and file inputted in Anvil app.
@anvil.server.callable
def sendtext(message, user_list, file):

    # Creates a Log file. Change this to your own directory for Log files.
    filename = str("E:\\PycharmProjects\\Chatbot\\Log ") + str(datetime.now().replace(microsecond=0)).replace(':', '꞉') + str(".txt")
    logfile = open(os.path.join(filename), 'a+', encoding='utf-8')

    logfile.write(gettime() + ' CHECKING FILE...\n')

    # Processes input file. Valid file formats are jpg, jpeg, png, mp4, quicktime, pdf.
    # Code continues without processing if file isn't the required format.
    if file is not None:
        if 'jpg' in file.content_type:
            filetype = '.jpg'
            anvil.media.write_to_file(file, 'file' + filetype)
            logfile.write(gettime() + ' Valid format: ' + filetype)
        elif 'jpeg' in file.content_type:
            filetype = '.jpeg'
            anvil.media.write_to_file(file, 'file' + filetype)
            logfile.write(gettime() + ' Valid format: ' + filetype)
        elif 'png' in file.content_type:
            filetype = '.png'
            anvil.media.write_to_file(file, 'file' + filetype)
            logfile.write(gettime() + ' Valid format: ' + filetype)
        elif 'mp4' in file.content_type:
            filetype = '.mp4'
            anvil.media.write_to_file(file, 'file' + filetype)
            logfile.write(gettime() + ' Valid format: ' + filetype)
        elif 'quicktime' in file.content_type:
            filetype = '.mov'
            anvil.media.write_to_file(file, 'file' + filetype)
            logfile.write(gettime() + ' Valid format: ' + filetype)
        elif 'pdf' in file.content_type:
            filetype = '.pdf'
            anvil.media.write_to_file(file, 'file' + filetype)
            logfile.write(gettime() + ' Valid format: ' + filetype)
        else:
            filetype = None
            logfile.write(
                gettime() + " ERROR: File is not .jpg, .jpeg, .mp4, .mov\nIf file format isn't changed, file won't be sent")

    else:
        filetype = None
        logfile.write(gettime() + ' No file uploaded')

    logfile.write('\n\n')

    # Creates user list.
    users = user_list.split('\n')

    # Code for running Selenium and automating WhatsApp message sending.
    log_browser = webdriver.Chrome(executable_path='E:\\chromedriver.exe')
    log_browser.implicitly_wait(100)
    log_browser.get('https://onlinenotepad.org/notepad')
    log_browser.minimize_window()

    logfile.write(gettime() + ' OPENING WHATSAPP WEB...\n')

    chrome_browser = webdriver.Chrome(executable_path='E:\\chromedriver.exe')
    chrome_browser.implicitly_wait(100)  # Wait period before timeout exception
    chrome_browser.get('https://web.whatsapp.com/')
    chrome_browser.minimize_window()
    chrome_browser.maximize_window()
    chrome_browser.find_element_by_xpath(
        '/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[1]/div/span')

    logfile.write(gettime() + ' LOGGED IN\n\n')

    for i in users:

        logfile.write(gettime() + ' USER: ' + i + '\n')

        chrome_browser.find_element_by_xpath(
            '/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]').clear()

        chrome_browser.find_element_by_xpath(
            '/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]').send_keys(
            i+Keys.ENTER)  # Searches for user and presses enter

        try:
            print('ok')

            chrome_browser.implicitly_wait(1)

            print(chrome_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/div').get_attribute("innerHTML"))

            if chrome_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/div').get_attribute("innerHTML") == 'Search or start new chat':

                chrome_browser.implicitly_wait(15)

                string = '//span[@title="{}"]'.format(i)

                loadeduser = chrome_browser.find_element_by_xpath(string).get_attribute("title")

                if loadeduser == i:

                    logfile.write(gettime() + ' FOUND\n')

                    pyperclip.copy(message)

                    actions = ActionChains(chrome_browser)
                    actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)  # Pastes text in message box
                    actions.send_keys(Keys.ENTER)  # Sends message
                    actions.perform()

                    if filetype is not None:
                        logfile.write(gettime() + ' MESSAGE SENT\n')
                    else:
                        logfile.write(gettime() + ' MESSAGE SENT\n\n')

                    if filetype is not None:
                        attach_file = chrome_browser.find_element_by_xpath('//div[@title = "Attach"]')
                        attach_file.click()
                        attach_file = chrome_browser.find_element_by_xpath(
                            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                        attach_file.send_keys('E:\\PycharmProjects\\Chatbot\\file' + filetype)
                        send_button = chrome_browser.find_element_by_xpath(
                            '/html/body/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div')
                        send_button.click()
                        logfile.write(gettime() + ' FILE SENT\n\n')

                else:
                    logfile.write(gettime()+' NOT FOUND\n\n')
                    continue
            else:
                print('lol')
                logfile.write(gettime() + ' NOT FOUND\n\n')
                continue

        except NoSuchElementException or StaleElementReferenceException:
            print('lmao')
            logfile.write(gettime()+' NOT FOUND\n\n')
            continue

        finally:
            chrome_browser.implicitly_wait(15)

    log_browser.maximize_window()
    logfile.seek(0)
    pyperclip.copy(logfile.read())
    log_browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[3]/button').click()
    actions = ActionChains(log_browser)
    actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)
    actions.perform()
    log_browser.find_element_by_xpath('/html/body/div[4]/button').click()
    logfile.close()


# Keeps code running forever, so that it responds the instant our Anvil app calls this code.
anvil.server.wait_forever()
