# Importa módulos de Selenium necesarios para espera explícita
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Función para esperar elementos presentes en el DOM (uno o varios)
def wait_for_elements(driver, selector_type, selector_value, multiple=False, timeout=10):
    """
    Espera hasta que el/los elemento/s esté/n presente/s en el DOM.

    :param driver: El navegador de Selenium.
    :param selector_type: Tipo de selector (By.ID, By.CSS_SELECTOR, etc).
    :param selector_value: El valor del selector.
    :param multiple: Si es True, espera varios elementos. Si False, uno solo.
    :param timeout: Tiempo máximo de espera en segundos.
    :return: Elemento o lista de elementos encontrados.
    """
    if multiple:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((selector_type, selector_value))
        )
    else:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((selector_type, selector_value))
        )

# Función para esperar que un elemento sea clicable y hacer clic
def click_element(driver, selector_type, selector_value, timeout=10):
    """
    Espera que el elemento esté habilitado y hace clic.

    :param driver: El navegador de Selenium.
    :param selector_type: Tipo de selector.
    :param selector_value: Valor del selector.
    :param timeout: Tiempo máximo de espera en segundos.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((selector_type, selector_value))
        )
        element.click()
    except Exception as e:
        print(f"Error al hacer click: {e}")
