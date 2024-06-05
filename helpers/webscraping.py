import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class ScrapingProactiva:
    
    def __init__(self,url):
        self.url_base = url
        self.driver = webdriver.Chrome()
        
        self.driver.get(url=self.url_base)

    
    def login(self,user,password):

        title = self.driver.title
        bucle = True

        while bucle:
        
            if title == "Acceso":
                # Ingresando usuario
                user_name = self.driver.find_element(By.ID,"theUName")
                user_name.send_keys(user)

                # Ingresando password
                user_name = self.driver.find_element(By.ID,"thePwd")
                user_name.send_keys(password)

                # Click ingresando a sesion
                button_session = self.driver.find_element(By.ID,"theSubmitBtn")
                button_session.click()

                button_acces = self.driver.find_element(By.ID,"imgServiceDesk")
                button_acces.click()


                bucle = False

    def accesFrame(self,name_frame):
        try:
            #Cambiando a frame
            self.driver.switch_to.frame(name_frame)

        except Exception as e:
            ValueError(e)

    def outFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            ValueError(e)

    def findXPath(self,element):
        try:
            elementXpath = self.driver.find_element(By.XPATH,element)
            time.sleep(2)
            return elementXpath
        except Exception as e:
            ValueError(e)
    
            
    def findID(self,id):
        try:
            elementID = self.driver.find_element(By.ID,id)
            time.sleep(2)
            return elementID
        except Exception as e:
            ValueError(e)

    def findInsideXPath(self,element,findXpath):
        try:
            elementXpath= element.find_element(By.XPATH,findXpath)
            time.sleep(2)
            return elementXpath
        except Exception as e:
            ValueError(e)


