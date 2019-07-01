import tqdm
import afprice

urls = ['https://www.amazon.in/dp/B07M9FDGJQ/', 
'http://dl.flipkart.com/dl/honor-9n-sapphire-blue-64-gb/p/itmf9pgsehv6nmss']

print("Using returns")
returns = []
for url in tqdm.tqdm(urls):
    returns+=[afprice.main(url, True)]
print(returns)

print("Using prints")
for url in urls:
    afprice.main(url, False)
    print()
