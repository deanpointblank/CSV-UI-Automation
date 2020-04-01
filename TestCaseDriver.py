import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestCaseDriver:

    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def __Click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def __EnterData(self, xpath, text):
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def __Assert(self, xpath, expectedText):
        actualText = self.driver.find_element_by_xpath(xpath).text 

        if actualText is not expectedText:
            raise ValueError(f'Failed: \'{actualText}\' is not \'{expectedText}\'')

    def __OpenUrl(self,url):
        self.driver.get(url)
        print(url)

    def close(self):
        self.driver.close()

    def ExecuteTestStep(self, command):
        #command shape [command , xpath, text]
        if command[0] == 'click':
            self.__Click(command[1])

        elif command[0] == 'enterData':
            self.__EnterData(command[1], command[2])
        
        elif command[0] == 'assert':
            self.__Assert(command[1], command[2])

        elif command[0] == 'open':
            self.__OpenUrl(command[2])

        print("Passed")

