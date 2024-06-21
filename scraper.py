from selenium_config import init_driver, scroll_down_page, press_more_comments_button, fetch_comments
from supabase_config import validar_url, insertar_comentarios

def run_scraper(minero, links):
    driver = init_driver()
    
    for link in links:
        driver.get(link)
        if validar_url(link, minero):
            for _ in range(2):
                scroll_down_page(driver)
            while press_more_comments_button(driver):
                pass
            print(f'No hay botón de más comentarios: esperando para scrapear datos en {link}')
            comentarios_array = fetch_comments(driver)
            print(f'{len(comentarios_array)} comentarios encontrados en {link}')
            insertar_comentarios(comentarios_array, minero)
        else:
            print(f'Se omitió el scraping para la URL {link}.')

    driver.quit()
    print('Scraping completado.')
