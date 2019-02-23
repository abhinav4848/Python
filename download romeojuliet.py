#don't save this file as requests.py
import requests, pyperclip
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print('Status code: '+str(res.status_code)+'\n')
print('Length: '+str(len(res.text))+'\n')
print('First 500 bytes: \n'+res.text[:500]+'\n')
print('Raise for status: '+str(res.raise_for_status())+'\n')
playFile = open('romeo and juliet.txt','wb') #write binary
for chunk in res.iter_content(100000): # asks bytes of data to iterate over
    playFile.write(chunk)
playFile.close()
print('Done.')
