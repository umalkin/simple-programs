import os
from bs4 import BeautifulSoup as bs
import requests

# website 
url = ''


# download page for parsing
page = requests.get(url)
sopas = bs(page.text, 'html.parser')

#locate all img tag
img_tags = sopas.findAll('img')

# create folder for images

if not os.path.exists('images'):
    os.makedirs('images')

# go to newly created folder

os.chdir('images')

# image file name
x = 0

# getting images
for image in img_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('img_' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
