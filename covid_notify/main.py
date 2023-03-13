import subprocess
import requests
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

myhtmlData=getData("https://www.mohfw.gov.in/")
print(myhtmlData)

