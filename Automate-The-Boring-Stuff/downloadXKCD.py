#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }

url = 'http://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
i = 1
while not url.endswith('#') and i<=4:
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         try:
             comicUrl = 'http:' + comicElem[0].get('src')
             # Download the image.
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
         except requests.exceptions.MissingSchema:
             # skip this comic
             prevLink = soup.select('a[rel="prev"]')[0]
             url = 'http://xkcd.com' + prevLink.get('href')
             continue

    # Save the image to ./xkcd.
    fileName = str(int(soup.select('a[rel="prev"]')[0].get('href').strip('/'))+1) +'-'+os.path.basename(comicUrl)
    imageFile = open(os.path.join('xkcd', fileName), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #create an html file with images and title
    comicTitle = comicElem[0].get('title')
    html = '<img src="'+fileName+'"><br /><b>'+fileName+'</b>- '+comicTitle+'<hr />'
    titleFile = open(os.path.join('xkcd', 'xkcdTitles.html'),'a') 
    titleFile.write(html+'\n')
    titleFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    i+=1

print('Done.')
