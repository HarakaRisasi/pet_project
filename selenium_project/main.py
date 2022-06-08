######################################################
# ChromeDriver - это отдельный исполняемый файл, который Selenium WebDriver использует для управления Chrome.
# Он поддерживается командой Chromium с помощью участников WebDriver.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# Optional argument, if not specified will search path.
######################################################
