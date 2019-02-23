import bs4, requests
def getAmazonPrice(productURL):
    # Amazon give 503 error without a header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(productURL, headers=headers) # downloads the page
    res.raise_for_status() # will throw error if not 200
    soup = bs4.BeautifulSoup(res.text, 'html.parser') # parse
    # only select based on css selector.
    # "select" creates a list with all values matching the selector
    # containing the desired selector
    # Looks like [<span class="a-size-medium a-color-price" id="priceblock_ourprice"><span class="currencyINR">  </span> 51,990.00</span>]
    price = soup.select('#priceblock_ourprice') 
    name = soup.select('#productTitle')
    #pick a value using the list index given by select(), take out its text.
    #looks like: '\xa0\xa0 51,990.00'
    #strip to remove empty spaces like \xa0, etc
    return {'price':price[0].text.strip(), 'name':name[0].text.strip()}

print('Enter the Amazon url: ')
url = input() # https://www.amazon.in/dp/B07M9FDGJQ/
price = getAmazonPrice(url)
print(price['name']+' costs Rs. '+price['price'])
