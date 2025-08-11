import re

text = "Email me at user@gmail.com or support@yahoo.org"

emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print(emails)

# Replace email domains
new_text = re.sub(r'@[\w\.-]+', '@fireflink.com', text)
print(new_text)
