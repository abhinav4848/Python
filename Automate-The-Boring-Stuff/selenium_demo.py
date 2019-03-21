from selenium import webdriver
browser = webdriver.Chrome(executable_path="C:\public_html\Python\webdriver\chromedriver.exe")
browser.get('https://abhinavkr.ga/')

#elem = browser.find_element_by_css_selector('body > div:nth-child(5) > div > div > div.col-md-4.mt-sm-2 > div > div > p.card-text > a:nth-child(11)')
#elem.click()
#elem = browser.find_element_by_css_selector('body > div.container > div > div.col-md-4 > img')
##elem = browser.find_element_by_css_selector('html').text
##print(elem)


