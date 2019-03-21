##print('Hello World')
##print('What is your name?') #ask for name
##myName = input()
##print('Hi '+ myName)
##print('The length of your name is ')
##print(len(myName))
##print('What is your age?')
##myAge=input()
##print('You will be '+str(int(myAge)+1)+' in a year.')

##myname= 'Abhinava'
##if myname == 'Abhinav':
##    print('Hi Abhinav')
##else:
##    print('Wrong Dude')
##print('done')

##print('Enter a name')
##name = input()
##if name:
##    print('Thanx, '+name)
##else:
##    print('Hi, no name')
##print('Done')

##name = ''
##while name != 'your name':
##    print('please enter your name')
##    name = input()
##print('thanx, '+name)

##name = ''
##while True:
##    print('please enter your name')
##    name = input()
##    if name == 'your name':
##        break
##print('thanx, '+name)

##spam = 0
##while spam < 5:
##    spam = spam + 1
##    if spam == 3:
##        continue
##    print('Spam is '+str(spam))
##print('done')

##total = 0
##for i in range(101):
##    total = total + i
##print(total)

##import pprint
##message = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
##count = {}
##for character in message.upper():
##    count.setdefault(character,0)
##    count[character]+=1
###print(pprint.pformat(count))
##pprint.pprint(count)

##name ="hi"	  
##place="bye"
##time = "6pm"
##print('hello %s you are invited to %s at time: %s' % (name, place, time))

##import re
##message = 'call me at 888-444-1344 tom or at 432-334-4444 today'
##phonereg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
##matchobject = phonereg.findall(message)
###print(matchobject.group())
##print(matchobject)



