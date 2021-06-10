from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#se crea un objeto de la clase driver de Chrome
driver = Chrome()

#se le pide al objeto creado que busque la url de google
driver.get("https://google.com")

#se busca el elemento que tiene por nombre q (que es la barra de búsqueda)
search_box = driver.find_element(By.NAME, "q")

#Una vez el elemento se encuentra se le inserta el texto a buscar
search_box.send_keys("web developer")

#Luego de que el texto es insertado se envía la búsqueda
search_box.submit()

#Solución que evita las preguntas relacionadas

#Se buscan los elementos que tienen clases relacionadas con resultados no patrocinados, evitando las clases de las preguntas
result = driver.find_element_by_xpath("//div[@class='hlcw0c' or @class='g'][3]")

#Se obtiene el url del elemento encontrado
url = result.find_element(By.TAG_NAME, 'a').get_attribute("href")

#Se abre la url
driver.get(url)


#Solución que no evita las preguntas relacionadas
#Se buscan todos los elementos que tengan el nombre de clase g (las url no patrocinadas)
#results = driver.find_elements(By.CLASS_NAME, 'g')
#url = results[3].find_element(By.TAG_NAME, 'a').get_attribute("href")
#driver.get(url)

