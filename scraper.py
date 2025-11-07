"""
Supermarket Mercadona Scraper
============================

Un scraper automatizado para extraer información de productos del supermercado Mercadona.
Utiliza SeleniumBase para navegación web robusta y BeautifulSoup para parsing de HTML.

Autor: Contribuciones por Andrei (2024)
Versión: 2024.11
Dependencias: seleniumbase, beautifulsoup4, keyboard

Funcionalidades principales:
- Navegación automatizada por todas las categorías de productos
- Extracción de datos: nombre, precio, imagen, categoría
- Manejo robusto de códigos postales y detección anti-bot
- Exportación a CSV con marca temporal
- Manejo inteligente de errores y timeouts
"""

# Importación de módulos estándar
import os
import csv
import time
import random
from datetime import datetime

# Librerías externas para scraping y automatización
from bs4 import BeautifulSoup
from seleniumbase import Driver
from selenium.webdriver.common.by import By

# Importa funciones auxiliares personalizadas
import funcionesAux as fc

# Función que guarda los datos de productos en un archivo CSV
def mercadona_csv(datos, nombre_archivo="mercadona.csv"):
    """
    Guarda los datos de productos en formato CSV.
    
    Args:
        datos (list): Lista de diccionarios con información de productos
        nombre_archivo (str): Nombre del archivo CSV a crear/actualizar
    
    Features:
        - Crea headers automáticamente basados en las keys del primer elemento
        - Append mode si el archivo ya existe
        - Encoding UTF-8 para caracteres especiales españoles
        - Manejo de archivos vacíos
    """
    if not datos:
        print("No hay datos para guardar.")
        return

    columnas = datos[0].keys()
    existe_archivo = os.path.isfile(nombre_archivo)

    with open(nombre_archivo, 'a+' if existe_archivo else 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columnas)
        if not existe_archivo:
            writer.writeheader()
        writer.writerows(datos)

# Función que inicia el navegador con configuración antitracking y sin detección
def iniciar_driver():
    """
    Inicializa el driver de Chrome con configuración optimizada para scraping.
    
    Returns:
        Driver: Instancia configurada de SeleniumBase Driver
    
    Configuración aplicada:
        - uc=True: Modo undetectable para evitar detección de bots
        - User-Agent específico para mayor compatibilidad
        - do_not_track=True: Mejora la privacidad
        - undetectable=True: Tecnología anti-detección avanzada
        - maximize_window(): Maximiza la ventana para mejor interacción
    """
    driver = Driver(
        browser="chrome",
        uc=True,                    # Usa Chromium con mejoras de compatibilidad
        headless2=False,            # Visibilidad del navegador (False para debug)
        incognito=False,            # Modo incógnito desactivado
        agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        do_not_track=True,
        undetectable=True           # Evita ser detectado como bot
    )
    driver.maximize_window()
    return driver

# Función que introduce el código postal en el modal inicial de la web
def introducir_codigo_postal(driver, codigo_postal):
    try:
        input_cp = fc.wait_for_elements(driver, By.CSS_SELECTOR, "input[data-testid='postal-code-checker-input']", multiple=False, timeout=5)
        input_cp.clear()
        input_cp.send_keys(codigo_postal)
        time.sleep(1)
        btn_continuar = fc.wait_for_elements(driver, By.CSS_SELECTOR, "button[data-testid='postal-code-checker-button']", multiple=False, timeout=5)
        btn_continuar.click()
        print("Código postal introducido correctamente.")
        time.sleep(3)
    except Exception:
        print("No se mostró el modal del código postal o ya fue gestionado.")

# Función que obtiene los datos (título, imagen, precio) de todos los productos visibles
def obtener_datos_productos(driver, categoria):
    productos = []
    elemento_productos = fc.wait_for_elements(driver, By.CSS_SELECTOR, 'div.product-cell[data-testid="product-cell"]', multiple=True)
    print(f"Total productos encontrados: {len(elemento_productos)}")

    for anuncio in elemento_productos:
        html_content = anuncio.get_attribute('innerHTML')
        soup = BeautifulSoup(html_content, 'html.parser')

        img_element = soup.find('img')
        imagen = img_element['src'] if img_element else "Imagen no disponible"

        h4_element = soup.find('h4', class_="subhead1-r product-cell__description-name", attrs={"data-testid": "product-cell-name"})
        titulo = h4_element.text if h4_element else "Título no disponible"

        p_element = soup.find('p', class_="product-price__unit-price subhead1-b", attrs={"data-testid": "product-price"})
        if p_element is None:
            p_element = soup.find('p', class_="product-price__unit-price subhead1-b product-price__unit-price--discount", attrs={"data-testid": "product-price"})

        precio = p_element.text.replace(".", "").replace(",", ".").replace("€", "").strip() if p_element else "Precio no disponible"

        print(f"Producto: {titulo}\nImagen: {imagen}\nPrecio: {precio}")
        productos.append({
            'titulo': titulo,
            'imagen': imagen,
            'precio': precio,
            'categoria': categoria
        })
    return productos

# Función que explora las categorías principales y sus subcategorías
def explorar_categorias(driver, codigo_postal):
    lista_productos = []

    categorias = fc.wait_for_elements(driver, By.CSS_SELECTOR, '.category-menu__header', multiple=True)

    for categoria in categorias:
        try:
            nombre_categoria = categoria.text.replace(",", "")
            print(f"\nAnalizando categoría: {nombre_categoria}")
            time.sleep(random.uniform(1, 2))

            try:
                categoria.click()
            except:
                print(f"Reintentando click tras reintroducir CP...")
                introducir_codigo_postal(driver, codigo_postal)
                categoria.click()

            time.sleep(random.uniform(1, 2))
            el_category = fc.wait_for_elements(driver, By.CSS_SELECTOR, 'li.category-menu__item.open', multiple=False)
            subcategorias = fc.wait_for_elements(el_category, By.CSS_SELECTOR, 'ul > li.category-item', multiple=True)

            for subcategoria in subcategorias:
                print(subcategoria.text)
                time.sleep(random.uniform(1, 2))
                try:
                    subcategoria.click()
                except:
                    introducir_codigo_postal(driver, codigo_postal)
                    subcategoria.click()

                time.sleep(random.uniform(1, 2))
                productos = obtener_datos_productos(driver, nombre_categoria)
                lista_productos.extend(productos)

        except Exception as e:
            print(f"Error al analizar la categoría {nombre_categoria}: {e}")

    return lista_productos

# Bloque principal que ejecuta el script
if __name__ == "__main__":
    driver = iniciar_driver()
    try:
        codigo_postal = input("Introduce tu código postal (ej: 28001): ")
        fecha = datetime.now().date()
        print(f"Iniciando escaneo: {datetime.now()}")

        driver.get("https://tienda.mercadona.es/")
        time.sleep(3)

        fc.click_element(driver, By.XPATH, "//button[normalize-space()='Aceptar']", timeout=5)
        introducir_codigo_postal(driver, codigo_postal)

        driver.get("https://tienda.mercadona.es/categories/112")
        time.sleep(3)

        introducir_codigo_postal(driver, codigo_postal)

        productos = explorar_categorias(driver, codigo_postal)

        if productos:
            mercadona_csv(productos, f"mercadona_{fecha}.csv")
        else:
            print("No se encontraron productos.")

    except Exception as e:
        print(f"Error durante el proceso de scraping: {e}")

    finally:
        driver.quit()
