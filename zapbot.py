from optparse import Option
from typing_extensions import Self
from selenium import webdriver
import time

class botwhatsapp:
    def __init__(self):
        self.mensagem = 'Olá, meu nome é ONEbot, fui criado por matheus e daniel'
        self.grupo = ["Grupo de teste"]
        Options = webdriver.ChromeOptions()
        Options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    def EnviarMensagens(self): 
        # <span dir="auto" title="Grupo de teste " class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Grupo de teste </span>
        # <div class="_2BU3P tm2tP copyable-area"><div class="_1SEwr">
        # <span data-testid="send" data-icon="send" class=""> 
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self grupo:
            grupo = self.driver.find_element_by_xpath(f"//spam[@title='{Grupo}']")
            time.sleep(3)
            grupo.click()
           chat_box = self.driver.find_element_by_class_name('_1SEwr')
           time.sleep(3)
           chat_box.click()
           chat_box.send_keys(self.mensagem)
           botão_enviar = self.driver.find_element_by_xpath("//spam[@data-icon='send']")
           time.sleep(3)
           botão_enviar.click()
           time.sleep(5)

    bot = whatsappbot()
