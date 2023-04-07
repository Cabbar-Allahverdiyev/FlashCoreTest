from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions;
from commonCommands.iwaitCommand import IWaitCommand;

class WaitForCommonCommand(IWaitCommand):
    def __init__(self,driver:webdriver.Chrome):
        super().__init__(driver)

    def waitById(self,id:str,time=super().waitTime):
        WebDriverWait(self.driver,time).until(
            expected_conditions.visibility_of_element_located((By.ID,id))
        );

    def waitByXPath(self,xpath:str,time=super().driver):
        WebDriverWait(self.driver,time).until(
            expected_conditions.visibility_of_element_located((By.XPATH,xpath))
        );

    def waitByCssSelector(self,selector:str,time=super().waitTime):
        WebDriverWait(self.driver,time).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,selector))
        );
