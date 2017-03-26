import os
import re

def getSource(url):
    bashCmd = "wget -q -O t.txt \"" + url + "\""
    os.system(bashCmd)
    bCmd2 = "cat t.txt >> html.txt"
    os.system(bCmd2)

def getURLs():
    p = re.compile("href=\".+?html\"")
    with open('urls.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    m = p.findall(data)

    for i in range(len(m)):
        m[i] = m[i][6:]
        m[i] = m[i][:-1]
        m[i] = "http://foundation.zurb.com/" + m[i]
     
    for match in m:
        getSource(match)
        print(match)

