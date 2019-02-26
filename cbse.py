# Get cbse results for a roll number
from selenium import webdriver
browser = webdriver.Chrome(executable_path="C:\public_html\Python\webdriver\chromedriver.exe")
browser.get('http://resultsarchives.nic.in/cbseresults/cbseresults2013/class12/cbse122013.htm')

roll = 9199260
for i in range(37):
    field = browser.find_element_by_name('regno')
    field.send_keys(roll)
    field.submit()

    name = browser.find_element_by_css_selector('body > div:nth-child(7) > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(2) > font > b').text
    subject = browser.find_elements_by_css_selector('body > div:nth-child(7) > div > center > table > tbody > tr > td:nth-child(2) > font') #list of all subjects
    mark = browser.find_elements_by_css_selector('body > div:nth-child(7) > div > center > table > tbody > tr > td:nth-child(3) > font') #list of all marks
    # headings = browser.find_element_by_css_selector('body > div:nth-child(7) > div > center > table > tbody > tr:nth-child(1) > td:nth-child(2) > p > font > strong')
    # conclusion = browser.find_element_by_css_selector('body > div:nth-child(7) > div > center > table > tbody > tr:nth-child(10) > td:nth-child(2) > b > font')

    print('Name: '+ name + ' ('+str(roll)+')')
    for i in range(8):
        if str(mark[i].text) == '---':
            continue # breaks this run of the for loop
        print(subject[i].text.title() + ' - ' + str(mark[i].text))

    print('\n-------------\n')
    roll+=1
    browser.find_element_by_css_selector('body > div:nth-child(7) > p:nth-child(5) > b > a > font').click()
    
