from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar Chrome en modo headless (sin interfaz gráfica)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializar el servicio de ChromeDriver
service = Service('/usr/local/bin/chromedriver')  # Asegúrate de que el path es correcto

# Inicializar el navegador
driver = webdriver.Chrome()

try:
    # Abrir Google
    driver.get("https://www.google.com")

    # Encontrar el campo de búsqueda, escribir "OpenAI" y enviar la consulta
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("OpenAI")
    search_box.send_keys(Keys.RETURN)

    # Esperar a que los resultados se carguen
    driver.implicitly_wait(10)

    # Extraer los títulos de los resultados de búsqueda
    results = driver.find_elements(By.CSS_SELECTOR, "h3")

    for result in results:
        print(result.text)

finally:
    # Cerrar el navegador
    driver.quit()
