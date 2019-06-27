def getFlipkartPrice(soup):
    price = soup.select('._1vC4OE') 
    name = soup.select('._35KyD6')
    return {'price':price[0].text.strip(), 'name':name[0].text.strip()}