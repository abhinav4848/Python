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