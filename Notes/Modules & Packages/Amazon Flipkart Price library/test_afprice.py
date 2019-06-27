import afprice

urls = ['https://www.amazon.in/dp/B07M9FDGJQ/', 
'http://dl.flipkart.com/dl/honor-9n-sapphire-blue-64-gb/p/itmf9pgsehv6nmss']

print("Using returns")
for url in urls:
    print(afprice.main(url, True))
    print()

print("Using prints")
for url in urls:
    afprice.main(url, False)
    print()
