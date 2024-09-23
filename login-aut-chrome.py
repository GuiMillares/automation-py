import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
options.add_argument("--disable-infobars")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-blink-features=AutomationControlled")

# Inicializar o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Acessar a página de login
driver.get("sua.url.com.br")

# Aguardar o carregamento da página e encontrar campos de entrada
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user")))
username_field = driver.find_element(By.NAME, "user")
password_field = driver.find_element(By.NAME, "password")

# Preencher os campos
username_field.send_keys("seuusario")
password_field.send_keys("suasenha")

# Enviar o formulário
password_field.submit()

# Aguardar a nova página carregar
WebDriverWait(driver, 10).until(EC.url_changes("sua.url.com.br"))

# Navegar diretamente para a página de playlists
driver.get("sua.url.com.br")
print("Navegando para a página de playlists...")

try:
    # Clicar no botão "Start Playlist"
    start_playlist_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span.css-1mhnkuh"))
    )
    driver.execute_script("arguments[0].click();", start_playlist_button)
    print("Start Playlist clicado.")

    # Aguarde um pouco para o menu suspenso aparecer
    time.sleep(1)

    # Clicar no botão "Autofit"
    autofit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span.css-10xnr05"))
    )
    driver.execute_script("arguments[0].click();", autofit_button)
    print("Autofit clicado.")

    # Aguarde um pouco após o autofit para garantir que o menu está estável
    time.sleep(2)

    # Clicar no botão "Start Playlist-TV-TI"
    start_tv_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.css-z53gi5-button span.css-1mhnkuh"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", start_tv_button)
    driver.execute_script("arguments[0].click();", start_tv_button)
    print("Start Playlist-TV-TI clicado.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Manter o navegador aberto
while True:
    time.sleep(30)
