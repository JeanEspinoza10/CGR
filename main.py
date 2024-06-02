# Subida de categorias

import time
from helpers.categories import Categories
from helpers.webscraping import ScrapingProactiva
from selenium.webdriver.common.by import By

def guardarpagina(name,codigo_fuente):
    # Define la ruta y el nombre del archivo
    ruta_archivo = f'./{name}.html'

    # Guarda el código fuente en un archivo HTML
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        file.write(codigo_fuente)

# categoriesFunctions = Categories()

# sistema = "Auditorías Juveniles" 

# result = categoriesFunctions.addCategorie(nameCategorie = sistema, id_categorie_father ="cf2914f4-0167-40e1-96fb-c075370a77b3")
# result_row = categoriesFunctions.addCategorie(nameCategorie = sistema, id_categorie_father ="80c487df-495e-46cc-891e-81f8bd61d51f")



# Verifica el nombre del frame actual
#frame_name = web_driver.driver.execute_script("return self.name;")
#print(f"Estás en el frame con nombre: {frame_name}")



'''
Login a pagina

'''

web_driver = ScrapingProactiva("https://celsoalexdiaz.proactivanet.com/panet/library/loginform/default.paw?pawLoginFormSrcUrl=%2fpanet%2fservicedesk%2fdefault.paw&pawLoginFormStatus=1&pawLoginFormSec=0")



web_driver.login(user="jean.espinoza@solutiontech.com.pe",password="jean.espinoza@solutiontech.com.pe")


'''
Entrar a opcion de administracion
'''

# Para completar un campo personalizado
web_driver.accesFrame("pawMenuTabFrame")


element_find = web_driver.findXPath('//*[@id="mop3"]')
element_find.click()

web_driver.outFrame()



'''
Ingresar campos personalizados
'''

web_driver.accesFrame("pawContentFrame")
web_driver.accesFrame("rightFrame")

element_find = web_driver.findID("customFields")
element_find.click()

'''
Buscar campo personalizado
'''

element_campo = web_driver.findXPath('//*[@id="thePTableAutoFilter"]/input')
element_campo.send_keys("Analista")


element_campo_button = web_driver.findXPath('//*[@id="thePTableAutoFilter"]/button')
element_campo_button.click()




# Verifica el nombre del frame actual
frame_name = web_driver.driver.execute_script("return self.name;")
print(f"Estás en el frame con nombre: {frame_name}")


# Click al campo buscado

element_table = web_driver.findXPath('//*[@id="myTable"]')
button_line_element = web_driver.findInsideXPath(element=element_table,findXpath='//*[@id="pawTheTb"]/tbody/tr[2]')
button_line_element.click()

# Agregamos valor al campo personalizado




