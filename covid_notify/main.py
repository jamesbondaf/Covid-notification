import subprocess
import requests
from bs4 import BeautifulSoup
import time
CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv) 
end run
'''

def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])

def getData(url):
  r=requests.get(url)
  return r.text

# Example uses:
# notify("james bond", "Heres an alert")

myhtmlData=getData("https://prsindia.org/covid-19/cases")


soup=BeautifulSoup(myhtmlData, 'html.parser')

DataList=[]

for td in soup.find_all('tbody')[0].find_all('tr'):
  list1=[]
  count=0
  for item in td.find_all('td'):
    list1.append(item.get_text())
    count+=1
  
    if(count==6):
   
      DataList.append(list1)
 
      list1=[]
      count=0



for item in DataList:
  print(item)

States=[]
for item in DataList[0:5]:
  
  States.append(item[1])



  
for item in DataList:
  if item[1] in States:
    nTitle='Cases of covid-19'
    nText=f"Sno.{item[0]}\n State:{item[1]}\n Confirmed Cases:{item[2]}\n Active Cases:{item[3]}\n Cured/Discharged:{item[4]}\n Deaths:{item[5]} "
    notify(nTitle,nText)
    time.sleep(2)









  




        
  


  




