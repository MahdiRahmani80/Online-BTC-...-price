from bs4 import BeautifulSoup
import requests ,datetime

urls = ["https://www.tgju.org/currency"]
head = ['بورس','انس طلا','مثقال طلا','طلا ۱۸ عیار','سکه','دلار','یورو','نفت برنت','بیت کوین']

c = 0

HTML = requests.get(urls[0])  # Get HTML In Internet 
soup = BeautifulSoup(HTML.text,"html.parser") # For convert text to html
ans= soup.find_all('span',attrs={"class":"info-price"})

print ("زمان : ",datetime.datetime.now())

for i in ans :
	print (head[c], "  :  " ,i.string)
	c+=1
