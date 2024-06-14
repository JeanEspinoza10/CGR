from helpers.webscraping import ScrapingProactiva
import time
import requests
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



def obtenerNumero(name):
    url = 'https://celsoalexdiaz.proactivanet.com/panet/api/CustomFields'
    params = {
        'Name': name,
        '$fields': 'ListValues,ListViews,Name'
    }
    headers = {
        'Accept': 'application/json',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqZWFuLmVzcGlub3phQHNvbHV0aW9udGVjaC5jb20ucGUiLCJvdnIiOiJmYWxzZSIsImF1dCI6IjAiLCJuYmYiOjE3MTcwNDU2ODMsImV4cCI6MTc0ODU4MTY4MywiaWF0IjoxNzE3MDQ1NjgzLCJpc3MiOiJwcm9hY3RpdmFuZXQiLCJhdWQiOiJhcGkifQ.QAUcqs1DJjBcQW59diOINBWvndnZob3-KS-2t2F9ahA',
        'Accept-Language': 'es'
    }

    try:
        # Realizar la solicitud GET
        
        response = requests.get(url=url, params=params, headers=headers)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()
            

            list_values = data[0]['ListValues']
            
           
           
            if list_values == "0":
                return 1
            
            # Dividir la cadena en una lista usando ';' como separador
            elementos = list_values.split(';')

            # Filtrar los elementos que no son números o son cadenas vacías
            elementos_numericos = [int(el) for el in elementos if el.isdigit()]

            # Obtener el último elemento
            if elementos_numericos:
                return elementos_numericos[-1] + 1

                            
            else:
                    print(f'Error en la solicitud: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print(f'Error de conexión Obtener numero: {e}')


def agregarCP(name,valor):
        
    '''
    Login a pagina

    '''


    orden = obtenerNumero(name=name)

    
    web_driver = ScrapingProactiva("https://celsoalexdiaz.proactivanet.com/panet/library/loginform/default.paw?pawLoginFormSrcUrl=%2fpanet%2fdefault.paw&pawLoginFormStatus=1&pawLoginFormSec=0")



    web_driver.login(user="jean.espinoza@solutiontech.com.pe",password="jean.espinoza@solutiontech.com.pe")


    # Obtener todas las cookies después del inicio de sesión
    cookies = web_driver.driver.get_cookies()

    # Convertir las cookies al formato requerido por requests
    cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}





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
    element_campo.send_keys(name)


    element_campo_button = web_driver.findXPath('//*[@id="thePTableAutoFilter"]/button')
    element_campo_button.click()


    # Click al campo buscado

    element_table = web_driver.findXPath('//*[@id="myTable"]')
    button_line_element = web_driver.findInsideXPath(element=element_table,findXpath='//*[@id="pawTheTb"]/tbody/tr[2]')
    button_line_element.click()

    # Agregamos valor al campo personalizado


    element_id = web_driver.findID('pageEditBtn')

    element_id.click()

    

    # Agregando valor
    input_name =web_driver.findXPath('//*[@id="DF_newListValueName"]')
    input_name.send_keys(valor)


    # Borrar el valor actual del campo de entrada
    input_value = web_driver.findXPath('//*[@id="DF_newListValueCode"]')
    input_value.clear()
    input_value.send_keys(orden)



    value = web_driver.findXPath('/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/table[2]/tbody/tr[2]/td/div/div/table/tbody/tr[1]/td[2]/div/div[3]/button')
    value.click()

    #Grabando
    element_id = web_driver.findID('pageSaveBtn')
    element_id.click()

    #guardarpagina('name',codigo_fuente=web_driver.driver.page_source)
    time.sleep(3)

    return "agrego correctamente"


def modificarCP(name,buscar_element):
    
    
    '''
    Login a pagina

    '''

    web_driver = ScrapingProactiva("https://celsoalexdiaz.proactivanet.com/panet/library/loginform/default.paw?pawLoginFormSrcUrl=%2fpanet%2fdefault.paw&pawLoginFormStatus=1&pawLoginFormSec=0")



    web_driver.login(user="jean.espinoza@solutiontech.com.pe",password="jean.espinoza@solutiontech.com.pe")

    # Obtener todas las cookies después del inicio de sesión
    cookies = web_driver.driver.get_cookies()

    # Convertir las cookies al formato requerido por requests
    cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}





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
    element_campo.send_keys(name)


    element_campo_button = web_driver.findXPath('//*[@id="thePTableAutoFilter"]/button')
    element_campo_button.click()


    # Click al campo buscado

    element_table = web_driver.findXPath('//*[@id="myTable"]')
    button_line_element = web_driver.findInsideXPath(element=element_table,findXpath='//*[@id="pawTheTb"]/tbody/tr[2]')
    button_line_element.click()

    # Agregamos valor al campo personalizado


    element_id = web_driver.findID('pageEditBtn')

    element_id.click()


    # Localizar el elemento select por su ID
    select_element = Select(web_driver.driver.find_element(By.ID, 'listFieldValues_selector'))

    # Obtener todas las opciones del select
    options = select_element.options

    # El texto del <option> que estás buscando
    target_text = buscar_element

    # Buscar la posición del <option> con el texto deseado
    position = None
    for index, option in enumerate(options):
        # Procesar el texto para obtener la parte deseada
        full_text = option.text
        start_index = full_text.find(']') + 2  # +2 para saltar el corchete y el espacio siguiente
        processed_text = full_text[start_index:]
        
        if processed_text == target_text:
            position = index
            break

    # Verificar si se encontró la posición
    if position is not None:
        # Seleccionar el <option> por su índice
        select_element.select_by_index(position)
        print(f'Seleccionado el <option> en la posición: {position}')
    else:
        return "No se encontro al elementeo requerido"


    button_removed = web_driver.findXPath('//*[@id="myRemoveListButton"]')
    button_removed.click()
    # Imprimir la lista de textos procesados


    # Cerrar el driver




    time.sleep(2)

    #Grabando
    element_id = web_driver.findID('pageSaveBtn')
    element_id.click()

    return "retirado correctamente"