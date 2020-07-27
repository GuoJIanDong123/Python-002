import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
url = 'https://maoyan.com/films?showType=3'
user_agent = 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3'
header = {}
cookie = {}
cookie['uuid'] = '14592AB0CF5111EA85E7A5AA0F3C5F942F1F08C4D9144A158D46E497EBEA708E'


header['user-agent'] = user_agent
mylist = []
def get_movie_top10(myurl):

    response = requests.get(myurl, headers=header, cookies=cookie)
    print(f'Status code: {response.status_code}')
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}, limit=10):
        print('---------------------------------')
        titleTag = tags.find_next('div', attrs={'class': 'movie-hover-title'})
        title = titleTag.find('span', attrs={'class': 'name'}).get_text()
        print(f'电影名称：{title}')
        categoryTag = titleTag.find_next_sibling('div')
        category = categoryTag.contents[2].strip()
        print(f'电影类型：{category}')
        releaseTag = categoryTag.find_next_sibling('div').find_next_sibling('div')
        release = releaseTag.contents[2].strip()
        print(f'上映时间：{release}')
        mylist.append([title, category, release])




get_movie_top10(url)

movie = pd.DataFrame(data=mylist)


dir_path = os.path.dirname(os.path.realpath(__file__))
#movie.to_csv(f'{dir_path}/movie.csv',encoding='utf8',index=False,header=['title', 'category', 'release'])