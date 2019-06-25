import bs4, requests

def main(url):
    # https://www.amazon.in/dp/B07M9FDGJQ/
    # http://dl.flipkart.com/dl/honor-9n-sapphire-blue-64-gb/p/itmf9pgsehv6nmss
    price = allocator(url)
    print(price.get('name', 'Undefined')+' costs Rs. '+price.get('price','Undefined'))

def allocator(url):
    #common task between both the sites
    # Pass a header to not get blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(url, headers=headers) # downloads the page
    res.raise_for_status() # will throw error if not 200
    soup = bs4.BeautifulSoup(res.text, 'html.parser') # parse

    #decide if amazon or flipkart
    destination = url.split('/')[2].split('.')[1]
    if destination == 'amazon':
        price = getAmazonPrice(soup)
    elif destination == 'flipkart':
        price = getFlipkartPrice(soup)
    return price

def getAmazonPrice(soup):
    # soup is a bs4.BeautifulSoup object
    # only select based on css selector.
    # "select" creates a list with all values matching the selector
    # containing the desired selector
    # Looks like [<span class="a-size-medium a-color-price" id="priceblock_ourprice"><span class="currencyINR">  </span> 51,990.00</span>]
    price = soup.select('#priceblock_ourprice') 
    name = soup.select('#productTitle')
    #pick a value using the list index given by select(), take out its text.
    #looks like: '\xa0\xa0 51,990.00'
    #strip to remove empty spaces like \xa0, etc
    return {'price':price[0].text.strip(), 'name':name[0].text.strip()}

def getFlipkartPrice(soup):
    price = soup.select('._1vC4OE') 
    name = soup.select('._35KyD6')
    return {'price':price[0].text.strip(), 'name':name[0].text.strip()}

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass