#! python3
# downloadwikimedia.py - Downloads every single image from a category

'''
There are 2 steps this program takes. 
When you enter the category url, it extracts link for all pics' individual pages.
Then from each page it extracts link for full resolution image.
Then it downloads the image.

Along the way, there are 2 try catch blocks.
try:
    download the individual pic's page
    try:
        download the image
    except:
        the image couldn't be downloaded
except:
    pic page not found
'''

import requests, os, bs4

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }

url = dirname = ''
errorCount = 0

while url == '' or not url.startswith('https://commons.wikimedia.org/wiki/Category:'):
    # https://commons.wikimedia.org/wiki/Category:St._Paul%27s_School,_Darjeeling
    url = input('Enter the full url of wikipedia category: ') # starting url
while dirname =='':
    dirname = input('Enter The folder name inside which to download: ')
os.makedirs(dirname, exist_ok=True)   # store comics in ./dirname

# Download the page.
print('Downloading page %s...' % url)
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# TODO: Find the URL of the comic image.
comicElem = soup.select('li > div > div.gallerytext > a')
if comicElem == []:
     print('Could not find any images.')
else:
    for url in comicElem:
        picTitle = url.contents[0]
        picURL= 'https://commons.wikimedia.org/' + url.get('href')
        
        try: 
            res2 = requests.get(picURL, headers=headers)
            res2.raise_for_status()
            soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')

            originalFile=soup2.select('#mw-content-text > div.fullMedia > p > a')[0].get('href')
            if originalFile == []:
                print('Could not find any images.')
            else:
                try:
                    # Download the image.
                    print('Downloading image %s...' % (picTitle))
                    res = requests.get(originalFile)
                    res.raise_for_status()
                except requests.exceptions.MissingSchema:
                    # start the next iteration of the loop
                    errorCount+=1
                    continue
                
                #Save the image to ./spsdarj
                imageFile = open(os.path.join(dirname, picTitle), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
        except requests.exceptions.HTTPError as err:
            print(err)
            errorCount+=1

print('Done. \n\nPics were downloaded to: '+ os.path.join(os.getcwd(), dirname))
if errorCount>0:
    print('There were however, '+str(errorCount)+' error(s) while downloading.')