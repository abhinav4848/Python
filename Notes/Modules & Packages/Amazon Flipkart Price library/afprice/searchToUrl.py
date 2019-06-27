import bs4, requests

def searchToUrl(term, website='Amazon'):
    """
    Convert a search term to url using google search.
    
    term= search term
    website= 'Flipkart' or 'Amazon' (default is Amazon)
    
    """
    print('Googling...') # display text while downloading the Google page
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        }
    
    if website == 'Amazon':
        res = requests.get('http://google.com/search?q=Amazon.in ' + term, headers=headers)
    elif website =='Flipkart':
        res = requests.get('http://google.com/search?q=Flipkart' + term, headers=headers)
    
    res.raise_for_status()

    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Identify all results.
    linkElems = soup.select('.r > a')

    # return the first result
    return linkElems[0].get('href')

if __name__ == '__main__':
    term = input("Enter a Search term: ")
    searchToUrl(term)