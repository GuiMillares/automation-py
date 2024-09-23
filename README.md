# Automação Web com Selenium

---

## Visão Geral

Este projeto utiliza a biblioteca **Selenium** para automatizar interações em uma página web específica, simulando o comportamento de um usuário humano. O código permite realizar tarefas como login, navegação e cliques em elementos de forma automática, o que é especialmente útil para rotinas repetitivas.

O projeto foi implementado para funcionar tanto no **Google Chrome** quanto no **Mozilla Firefox**. Embora os cliques tenham sido personalizados para uma página específica, você pode adaptar o código para outras páginas alterando os seletores e URLs.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Selenium**: Biblioteca de automação de navegadores web.
- **WebDriver Manager**: Facilita a instalação e gerenciamento do driver correto do navegador.
- **Navegadores Compatíveis**: Google Chrome e Mozilla Firefox.

## Requisitos de Instalação

Antes de começar, certifique-se de ter o **Python** instalado em seu sistema. Se ainda não tiver, baixe e instale a partir do [site oficial do Python](https://www.python.org/downloads/).

Em seguida, instale as bibliotecas necessárias utilizando o **pip**:

```bash
pip install selenium webdriver-manager
```

## Configuração do Projeto

O código está configurado para funcionar tanto no Google Chrome quanto no Mozilla Firefox. Dependendo do navegador que você deseja usar, o driver apropriado será instalado automaticamente pelo **WebDriver Manager**.

## Versão Chrome

### Código

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configurações do ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")  # Modo kiosk
options.add_argument("--disable-infobars")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")  # Remove a mensagem de automação
options.add_argument("--remote-debugging-port=9222")  # Adiciona porta de depuração remota

# Inicializar o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Acessar a página de login
driver.get("suaurl.com.br")

# Aguardar o carregamento da página e encontrar campos de entrada
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user")))
username_field = driver.find_element(By.NAME, "user")
password_field = driver.find_element(By.NAME, "password")

# Preencher os campos
username_field.send_keys("seuusuario")
password_field.send_keys("suasenha*")

# Enviar o formulário
password_field.submit()

# Aguardar a nova página carregar
WebDriverWait(driver, 10).until(EC.url_changes("suaurl.com.br"))

# Navegar diretamente para a página de playlists
driver.get("suaurl.com.br")
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

```

## Versão Firefox

### Código

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# Configurações do Firefox
options = webdriver.FirefoxOptions()
options.add_argument("--kiosk")  # Modo kiosk

# Inicializar o navegador
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Acessar a página de login
driver.get("suaurl.com.br")

# Aguardar o carregamento da página e encontrar campos de entrada
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user")))
username_field = driver.find_element(By.NAME, "user")
password_field = driver.find_element(By.NAME, "password")

# Preencher os campos
username_field.send_keys("seuusuario")
password_field.send_keys("suasenha*")

# Enviar o formulário
password_field.submit()

# Aguardar a nova página carregar
WebDriverWait(driver, 10).until(EC.url_changes("suaurl.com.br"))

# Navegar diretamente para a página de playlists
driver.get("suaurl.com.br")
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

```

## Funcionalidades do Código

- **Modo Kiosk**: Abre o navegador em tela cheia, sem barras de ferramentas.
- **Login Automatizado**: Preenche automaticamente os campos de login e envia o formulário.
- **Navegação e Cliques**: Navega para a página de playlists e realiza cliques nos botões configurados.
- **Ações**: Clica em "Start Playlist", "Autofit" e "Start Playlist-TV-TI".

## Personalização

A parte mais personalizável do código é a seção que interage com elementos específicos da página, conforme mostrado abaixo:

```python
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

```

### Como Personalizar

1. **Seletores CSS**:
    - Os seletores CSS (`By.CSS_SELECTOR`) são usados para identificar elementos específicos da página, como botões ou campos de entrada.
    - Você pode modificar esses seletores para apontar para diferentes elementos da página em que deseja realizar a automação. Por exemplo, se você deseja clicar em um botão com um ID diferente, basta alterar `"span.css-1mhnkuh"` para o seletor correspondente, como `"#meuBotao"`.
2. **Ações Personalizadas**:
    - O código inclui comandos como `click()`, `scrollIntoView(true)`, entre outros. Você pode substituir essas ações por outras interações, como `send_keys("texto")` para preencher um campo de texto ou `clear()` para limpar um campo de entrada.
3. **Controle de Tempo**:
    - O uso de `time.sleep()` é importante para garantir que o código espere o tempo necessário para que elementos sejam carregados antes de tentar interagir com eles. Ajuste esses tempos conforme a velocidade de carregamento da sua página.
4. **Estrutura de Controle de Erros**:
    - A estrutura `try` e `except` permite capturar erros durante a execução do código. Se o seu código encontrar elementos diferentes ou se a página demorar mais para carregar, a estrutura ajudará a evitar que o programa pare abruptamente.

### Exemplo de Modificação

Se você deseja clicar em um botão com a classe `".meu-novo-botao"` em vez de `"span.css-1mhnkuh"`:

```python
new_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".meu-novo-botao"))
)
driver.execute_script("arguments[0].click();", new_button)
print("Meu Novo Botão clicado.")

```

Essa flexibilidade torna o código altamente adaptável a diferentes páginas e elementos, bastando alterar os seletores e ações conforme necessário.

## Manutenção do Projeto

O navegador permanecerá aberto e ativo após a execução das tarefas, caso deseje interromper a execução, feche manualmente o navegador ou finalize o processo do Python.

## Contribuição

Sinta-se à vontade para contribuir com este projeto, seja aprimorando o código, corrigindo bugs ou adicionando novas funcionalidades.

---

***Criado por:** Guilherme Millares 
**data:** 21/09/2024*
