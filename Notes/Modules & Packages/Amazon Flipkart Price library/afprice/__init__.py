"""
Finds Price of Amazon.in or Flipkart products

Function:
main(url, returning)

url: full url to amazon or flipkart product
returning: True for returning a dictionary of {'price': 'value', 'name': 'value'},
    False for printing statement

Example:

import afprice
afprice.main('https://www.amazon.in/dp/B07M9FDGJQ/', False)
>>> Honor 9N (Midnight Black, 64 GB)  (4 GB RAM) costs Rs. 8,999
afprice.main('https://www.amazon.in/dp/B07M9FDGJQ/', True)
>>> {'price':' 8,999', 'name':'Honor 9N (Midnight Black, 64 GB)  (4 GB RAM)'}

"""

import bs4, requests
# Python 3 uses absolute imports. Any unqualified name is imported as a top-level module.
# https://stackoverflow.com/a/38564405/2365231
import afprice.amazon
import afprice.flipkart

def main(url, returning):
    # https://www.amazon.in/dp/B07M9FDGJQ/
    # http://dl.flipkart.com/dl/honor-9n-sapphire-blue-64-gb/p/itmf9pgsehv6nmss
    price = allocator(url)
    
    if returning:
      return price
    else:
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
        price = amazon.getAmazonPrice(soup)
    elif destination == 'flipkart':
        price = flipkart.getFlipkartPrice(soup)
    return price

if __name__ == '__main__':
    try:
        url = input("Enter a Fipkart or Amazon url: ")
        main(url)
    except KeyboardInterrupt:
        pass