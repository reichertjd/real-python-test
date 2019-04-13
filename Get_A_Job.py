
import requests
from bs4 import BeautifulSoup
import os


Buzzwords = requests.get('https://www.bluleadz.com/blog/the-ultimate-list-of-business-buzzwords-and-their-true-definitions')
soup = BeautifulSoup(Buzzwords.text, 'html.parser')
Buzzword_names = soup.find_all('h4')


list1 = []
for names in Buzzword_names:
    Buzzword = str(names)
    Word = Buzzword.replace('<h4><span style="color: #008cbf;">', '').replace('</span></h4>', '')
    list1.append(Word)
    
Statistics = requests.get('https://www.statistics.com/landing-page/data-analytics/')
soup = BeautifulSoup(Statistics.text, 'html.parser')
Statistics_names = soup.find_all('h2')

for model in Statistics_names:
    Stat_Word = str(model)
    Stat_Word_Clean = Stat_Word.replace('<h2>', '').replace(':</h2>', '')
    Stat_Word_Cleanx2 = Stat_Word_Clean.replace('<br/>', '')
    list1.append(Stat_Word_Cleanx2)

Statistics2 = requests.get('https://www.analyticsvidhya.com/glossary-of-common-statistics-and-machine-learning-terms/')
soup = BeautifulSoup(Statistics2.text, 'html.parser')
Statistics_names2 = soup.find_all('strong')
Statistics_names3 = soup.find_all('b')

for name in Statistics_names3:
    strname = str(name)
    clean_name = strname.replace('<b>', '').replace('</b>', '')
    list1.append(clean_name)
    
for name2 in Statistics_names2:
    strname2 = str(name2)
    clean_name2 = strname2.replace('<strong>', '').replace('</strong>', '')
    list1.append(clean_name2)

print(list1)
