import requests
import string
import os

from bs4 import BeautifulSoup
x = int(input())
a_type = input()
fn_list = []
count = 0
directory = os.getcwd()
r = requests.get('https://www.nature.com/nature/articles')
soup = BeautifulSoup(r.content, 'html.parser')
# a = soup.find_all('article')
a1 = soup.find('a', {'class': 'c-pagination__link'})
if a1:
    nav_link = a1.get('href').rstrip(a1.get('href')[-1])
    for n in range(x):
        url = 'https://www.nature.com' + nav_link + str(n + 1)
        r1 = requests.get(url)
        soup_loop = BeautifulSoup(r1.content, 'html.parser')
        a = soup_loop.find_all('article')
        os.mkdir('Page_' + str(n + 1))
        os.chdir(directory + '/Page_' + str(n + 1))
        for i in a:
            at_soup = BeautifulSoup(str(i), 'html.parser')
            at = at_soup.find_all('span', {'data-test': 'article.type'})
            for j in at:
                if j.span.string == a_type:
                    file_name = at_soup.find_all('a')
                    d_soup = BeautifulSoup(str(i), 'html.parser')
                    desc = d_soup.find_all('a', {'data-track-action': 'view article'})
                    for k in file_name:
                        fn = k.text.translate(k.text.maketrans(' ', '_', string.punctuation)).rstrip('_')
                        fn_list.append(fn)
                    for m in desc:
                        ra = requests.get('https://www.nature.com' + m.get('href'))
                        a_soup = BeautifulSoup(ra.content, 'html.parser')
                        p = a_soup.find('div', {'class': 'article__body'})
                        if p:
                            p = p.text.strip()
                            file = open(fn_list[count] + '.txt', 'w', encoding='UTF-8')
                            file.write(p)
                            file.close()
                            count += 1
                        else:
                            p = a_soup.find('div', {'class': 'article-item__body'})
                            p = p.text.strip()
                            file = open(fn_list[count] + '.txt', 'w', encoding='UTF-8')
                            file.write(p)
                            file.close()
                            count += 1
        os.chdir(directory)
