from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from yt_dlp import YoutubeDL
import json

# Configuracion de Selenium
options = Options()
options.binary_location = "C:\\WebDriver\\chrome-win64\\chrome.exe"
options.add_argument("--start-maximized")
servicio = ChromeService("C:\\WebDriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servicio, options=options)

# URL del video
url = 'https://www.youtube.com/watch?v=LQgE7aHUsVU'
driver.get(url)

# Esperar y cerrar modal de cookies si aparece
try:
    consent_overlay = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'dialog'))
    )
    consent_buttons = consent_overlay.find_elements(By.CSS_SELECTOR, '.eom-buttons button.yt-spec-button-shape-next')
    if len(consent_buttons) > 1:
        consent_buttons[1].click()
except TimeoutException:
    print('No apareció el modal de cookies')

# Esperar a que cargue el título del video
WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.ytd-watch-metadata'))
)

# Extraer datos con Selenium
video = {}

title = driver.find_element(By.CSS_SELECTOR, 'h1.ytd-watch-metadata').text

channel = {}
channel_element = driver.find_element(By.ID, 'owner')
channel['url'] = channel_element.find_element(By.CSS_SELECTOR, 'a.yt-simple-endpoint').get_attribute('href')
channel['name'] = channel_element.find_element(By.ID, 'channel-name').text
channel['image'] = channel_element.find_element(By.ID, 'img').get_attribute('src')
channel['subs'] = channel_element.find_element(By.ID, 'owner-sub-count').text.replace(' subscribers', '')

# Expandir descripción
driver.find_element(By.ID, 'description-inline-expander').click()

info_container_elements = driver.find_elements(By.CSS_SELECTOR, '#info-container span')
views = info_container_elements[0].text.replace(' views', '')
publication_date = info_container_elements[2].text

description = driver.find_element(
    By.CSS_SELECTOR, '#description-inline-expander .ytd-text-inline-expander span'
).text

driver.quit()  # Cerrar navegador

# Obtener likes con yt_dlp
ydl_opts = {}
with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    likes = info.get("like_count", "N/A")

# Armar el JSON final
video['url'] = url
video['title'] = title
video['channel'] = channel
video['views'] = views
video['publication_date'] = publication_date
video['description'] = description
video['likes'] = likes

# Exportar a JSON
with open('video.json', 'w', encoding='utf-8') as file:
    json.dump(video, file, indent=4, ensure_ascii=False)

print("✅ Video exportado correctamente con likes:", likes)
