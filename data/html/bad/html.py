import os
import re

def getSource(url):
    bashCmd = "wget -q -O t.txt \"" + url + "\""
    os.system(bashCmd)
    bCmd2 = "cat t.txt >> html.txt"
    os.system(bCmd2)

def getURLs():
    p = re.compile('href=(\"http.+?\")')

    with open('urls.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')

    m = p.findall(data)
    
    for match in m:
        getSource(match)
        print(match)
