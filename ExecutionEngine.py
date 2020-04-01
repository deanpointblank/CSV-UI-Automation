from time import sleep
import pandas as pd
from TestCaseDriver import TestCaseDriver

class ExecutionEngine:
    '''
        This class is design to execute test cases via CSV files.
    '''

    def __init__(self):
        self.testCase = None
        self.driver = None

    def __Setup(self):
        self.driver = TestCaseDriver()

    def __Cleanup(self):
        ''' Cleans up class by deleting driver and test cases.'''

        self.driver.close()
        self.testCase = None
        self.driver = None

    def __RunTestSteps(self):
        '''Loops through testcase csv to do command on xpath.'''

        for testStep in self.testCase:  
            self.driver.ExecuteTestStep(testStep)
            sleep(5)
    

    def __RetrieveTestCase(self, testCaseNumber):
        #read a csv into a dataframe
        #testCaseNumber/Name

        self.testCase = pd.read_csv(testCaseNumber).values
        


    def ExecuteTestCases(self, testCaseNumber):
        '''Creates a WebDriver to Execute all test steps within test case CSV '''
    
        self.__Setup()
        
        self.__RetrieveTestCase(testCaseNumber)

        self.__RunTestSteps()

        self.__Cleanup()
