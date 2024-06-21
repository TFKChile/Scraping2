from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    return driver

def scroll_down_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

def press_more_comments_button(driver):
    try:
        boton = driver.find_element(By.CSS_SELECTOR, "#comment-tree > faceplate-partial > div:nth-child(2) > button")
        boton.click()
        time.sleep(3)
        scroll_down_page(driver)
        return True
    except:
        return False

def fetch_comments(driver):
    comentarios = driver.find_elements(By.CSS_SELECTOR, "#comment-tree > shreddit-comment")
    comentarios_array = []
    for comentario in comentarios:
        try:
            autor_element = comentario.find_element(By.CSS_SELECTOR, "div > div > div > faceplate-hovercard > div.flex.flex-row.items-center.overflow-hidden > faceplate-tracker > a")
            autor_comentario = autor_element.get_attribute("innerHTML")
        except:
            continue
        texto_comentario = comentario.find_element(By.CSS_SELECTOR, ".md").text
        try:
            fecha_element = comentario.find_element(By.CSS_SELECTOR, "a > faceplate-timeago > time")
            fecha_comentario = fecha_element.get_attribute("title")
        except:
            fecha_comentario = "Fecha no disponible"
        
        if autor_comentario and texto_comentario and fecha_comentario:
            comentarios_array.append({
                "autor": autor_comentario,
                "comentario": texto_comentario,
                "fecha": fecha_comentario
            })
    return comentarios_array
