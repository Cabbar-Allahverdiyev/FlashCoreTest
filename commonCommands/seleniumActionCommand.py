from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.by import By;

class SeleniumActionCommand:
    def __init__(self,driver:webdriver.Chrome) :
        self.driver=driver;
    
    def findById(self,id:str):
        findElement=self.driver.find_element(By.ID,id);
        return findElement;

    def findByName(self,name:str):
        findElement=self.driver.find_element(By.NAME,name);
        return findElement;

    def findByXPath(self,xpath:str):
        findElement=self.driver.find_element(By.XPATH,xpath);
        return findElement;

    def findByCssSelector(self,selector:str):
        findElement=self.driver.find_element(By.CSS_SELECTOR,selector);
        return findElement;