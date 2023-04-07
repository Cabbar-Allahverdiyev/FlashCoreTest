from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;

class IWaitCommand:
    def __init__(self,driver:webdriver.Chrome,waitTime=5) -> None:
        self.driver=driver;
        self.waitTime=waitTime;
