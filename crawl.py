import os
import requests
from bs4 import BeautifulSoup
from requests_kerberos import HTTPKerberosAuth


#read the file containing all selected pages from the sitemap
with open("C:/Users/Toto/Documents/MySites/intranet_pages.txt","r") as f:
    contenu = f.readlines()
    
# Storage file is created 
with open("C:/Users/Toto/Documents/MySites/intranet_links.txt","w") as file:


    line = col = 0
    for c in contenu:
        col = 0
        file.write(c.strip())
        file.write("\n----------------------------------------------------------------------\n")
        line += 1
        #connect to the read page
        response = requests.get(c.strip(), auth=HTTPKerberosAuth(),verify = False)
        page = response.content
        soup = BeautifulSoup(page, 'html.parser')
        
        #looking for link into the page
        for a in soup.find_all('a', href=True):
            col = 1
            link = a['href']
            file.write(link+"\n")
            line += 1
