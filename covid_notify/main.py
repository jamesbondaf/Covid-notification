import subprocess
import requests
from bs4 import BeautifulSoup
CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv) 
end run
'''

def notify(title, text, country):
  subprocess.call(['osascript', '-e', CMD, title, text, country])

def getData(url):
  r=requests.get(url)
  return r.text

# Example uses:
notify("james bond", "Heres an alert", "INDIA")

myhtmlData=getData("https://prsindia.org/covid-19/cases")


soup=BeautifulSoup(myhtmlData, 'html.parser')

DataList=[]

for td in soup.find_all('tbody')[0].find_all('tr'):
  list1=[]
  count=0
  for item in td.find_all('td'):
    list1.append(item.get_text())
    count+=1
    if(count==5):
      print(list1)
      DataList.append(list1)
    #   print(DataList)
      list1=[]
      count=0

print(len(DataList))

for item in DataList:
  print(item)









  




        
  


  




