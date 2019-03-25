#! python 3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 133-544-3333, 444-44444, (432)-445-8888, 555-0000 ext 23455, ext. 12345, x12354
(
((\d{3})|(\(\d{3}\)))?    # area code (optionl)
(\s|-|\.)    # first separator
(\d{3})    # first 3 digits
(\s|-|\.)      # separator
(\d{4})    # last 4 digits
(((ext(\.)?\s)|x)    # extension-word part (optional)
(\d{2,5}))?    # extension-number part (optional)
)
''',re.VERBOSE)

# create a regex for emails
emailRegex = re.compile(r'''
[a-zA-Z0-9-.+]+  #name part
@
[a-zA-Z0-9-.+]+ #domain-name part
''', re.VERBOSE)

# get the text off the clipboard
# text = pyperclip.paste()
text = '''No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

Reach Us by Email
General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Please see this page for academic review requests)
Help with your order: info@nostarch.com'''

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumbers in extractedPhone:
    allPhoneNumbers.append(phoneNumbers[0])
# Copy the extracted email/phone onto the clipboard
results = '\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractedEmail)
pyperclip.copy(results)
print(results)
