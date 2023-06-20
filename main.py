import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# os.environ['PATH'] += r"/Users/aryalavasani/Documents/Personal/python-selenium"

def displayNotification(message,title=None,subtitle=None,soundname=None):
	"""
		Display an OSX notification with message title an subtitle
		sounds are located in /System/Library/Sounds or ~/Library/Sounds
	"""
	titlePart = ''
	if(not title is None):
		titlePart = 'with title "{0}"'.format(title)
	subtitlePart = ''
	if(not subtitle is None):
		subtitlePart = 'subtitle "{0}"'.format(subtitle)
	soundnamePart = ''
	if(not soundname is None):
		soundnamePart = 'sound name "{0}"'.format(soundname)

	appleScriptNotification = 'display notification "{0}" {1} {2} {3}'.format(message,titlePart,subtitlePart,soundnamePart)
	os.system("osascript -e '{0}'".format(appleScriptNotification))

current_status = "Letzte Aktualisierung 21.05.2023"
driver =  webdriver.Chrome()
driver.get("https://www.dsit.org.ir/?lang=fa")
b2_zertifikat = driver.find_element(by=By.LINK_TEXT,value="Goethe-Zertifikat B2")
b2_zertifikat.click()
second_link = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'اینجا'))
)
second_link.click()


# Find the element containing the desired text
element = driver.find_element(by=By.XPATH,value="//*[starts-with(text(), 'Letzte Aktualisierung')]")

# Get the text of the element
text = element.text
if(text != current_status):
    displayNotification("Es ist Zeit, die Goethe-Website zu besuchen","GOETHE ANMELDUNG")
else:
    displayNotification("Website wird überprüft","GOETHE ANMELDUNG")    
    