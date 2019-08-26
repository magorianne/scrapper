import os
from bs4 import BeautifulSoup

#read the file sitemap.xml stored on your disk
f = open("C:/Users/Toto/Documents/MesSites/sitemap.xml","r")
contenu = f.read()
f.close()

#Parse the XML file
soup = BeautifulSoup(contenu, 'html.parser')
#get all url tags and its content
urls = soup.find_all("url")
#When "mes:meta" tag value is "Folder" or "Document" save the URL into a file
for url in urls:
    if (url.find("mes:meta")!=None):
        if (url.find("mes:meta").text.strip() == "Folder" or url.find("mes:meta").text.strip() == "Document"):
            with open("C:/Users/Toto/Documents/MesSites/intranet_pages.txt","a") as f:
                f.write(url.loc.text.strip()+"\n")
print("Done!")
