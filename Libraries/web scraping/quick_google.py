#! python3
# http://automatetheboringstuff.com/chapter11/
# quick_google.py - Opens several Google search results.

import sys, requests, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Identify all results.
linkElems = soup.select('.r a')

# Open a browser tab for top 5 results
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
