import requests as r 
from bs4 import BeautifulSoup as bs 
import os

url = 'https://dev.bg/company/jobs/junior-intern/?_seniority=intern'
page = r.get(url)
soup = bs(page.content, 'html.parser')
results = soup.find(id="jobs")
alljobs_elements = results.find_all('div', class_='job-list-item')

cwd = os.path.dirname(__file__)
my_file = '/my_file.csv'
cwd += '/data' + my_file

h6_class = 'job-title ab-title-placeholder ab-cb-title-placeholder'
for job in alljobs_elements:
    element = job.find(title='Python')
    if element != None and element['title'] == 'Python':
        title = job.find('h6', class_= h6_class)
        location = job.find('span', class_='badge').text.split()[0]
        date = ' '.join(job.find('span', class_='date date-with-icon').text.split())
        job_url = job.find_all('a')[0]['href']

        flag = os.path.exists(cwd)
        if flag:
            with open(cwd, 'a') as file:
                file.write(f'Position: {title.text}\n')
                file.write(f'Location: {location}\n')
                file.write(f'Date: {date}\n')
                file.write(f'Job link: {job_url.strip()}\n\n')
        else:
            os.chdir(os.path.dirname(__file__))
            os.mkdir('data')

            with open(cwd, 'a') as file:
                file.write(f'Position: {title.text}\n')
                file.write(f'Location: {location}\n')
                file.write(f'Date: {date}\n')
                file.write(f'Job link: {job_url.strip()}\n\n')            