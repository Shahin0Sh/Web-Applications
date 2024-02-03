import requests as r 
from bs4 import BeautifulSoup as bs 
import os
import pandas as pd

# https://dev.bg/company/jobs/junior-intern
# https://dev.bg/company/jobs/junior-intern/?_paged=4
url = input()

page = r.get(url)
soup = bs(page.text, 'html.parser')

results = soup.find(id="jobs")
alljobs_elements = results.find_all('div', class_='job-list-item')

cwd = os.path.dirname(__file__)
my_file = '/my_file.csv'
cwd += '/data' + my_file

clmnns = ['Position','Location','Date','Job Link']
df = pd.DataFrame(columns=clmnns)

h6_class = 'job-title ab-title-placeholder ab-cb-title-placeholder'
data = []
for job in alljobs_elements:
    element = job.find(title='Python')
    if element != None and element['title'] == 'Python':
        title = job.find('h6', class_= h6_class).text
        location = job.find('span', class_='badge').text.split()[0]
        date = ' '.join(job.find('span', class_='date date-with-icon').text.split())
        job_url = job.find_all('a')[0]['href']
        data.append([title,location,date,job_url])

if data:
    for  val in data:
        lenght = len(df)
        df.loc[lenght] = val
        df.to_csv(cwd, index=False, sep=';', encoding='utf-8-sig')
        print(f'{val} added to csv')
else:
    print('No data')
