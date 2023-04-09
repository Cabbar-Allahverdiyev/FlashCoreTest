from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;

class IWaitCommand:
    def __init__(self,driver:webdriver.Chrome,waitTime=5) -> None:
        self.driver=driver;
        self.waitTime=waitTime;

    def waitById(self,id:str,time=0)->None:pass
        

    def waitByXPath(self,xpath:str,time=0)->None:pass

    def waitByCssSelector(self,selector:str,time=0)->None:pass

