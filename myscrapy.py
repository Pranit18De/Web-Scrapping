from bs4 import BeautifulSoup #the main parser of HTML files
import requests
import csv

url ="http://mhrd.gov.in/iiits"
res = requests.get(url)
html = res.content
#print(html)

soup = BeautifulSoup(html,"html.parser")
table = soup.find('table', attrs ={'class':'dataTable'})
#print(soup.prettify())
lr=[]
for row in table.findAll('tr'):
    lc=[]
    for cell in row.findAll('td'):
        text = cell.text.replace('\t','')
        lc.append(text)
    lr.append(lc)

outfile = open("./iiit.csv","w")
writer = csv.writer(outfile)
writer.writerows(lr)


