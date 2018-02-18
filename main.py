import json
import logging
import os
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

''' SETTING '''

#   SEARCH START DAY AND END DAY
#   MAXIMUM RANGE IS TWO MONTHS
START_DAY = '2017/12/01 00:00:00'
END_DAY = '2017/12/02 00:00:00'
LIMIT_NEWS_GET = 30

# SET WHICH CATEGORY YOU WANT TO SEARCH:
# headline, all, tw_stock, wd_stock, cn_stock, forex, future
CATEGORY = 'headline'

# SET FILE PATH TO SAVE ARTICLE
DATA_DIR_PATH = './data/' + CATEGORY + '/'

# URL - NO MODIFY
NEWS_CATEGORY_API = 'https://news.cnyes.com/api/v3/news/category/'
NEWS_CONTENT_URL = 'https://news.cnyes.com/news/id/'


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main():
    try:
        try:
            start_day = datetime.strptime(START_DAY, '%Y/%m/%d %H:%M:%S')
            end_day = datetime.strptime(END_DAY, '%Y/%m/%d %H:%M:%S')
        except ValueError:
            raise Usage('Time Error')

        start_day_second = int(start_day.timestamp())
        end_day_second = int(end_day.timestamp())

        url = (NEWS_CATEGORY_API + CATEGORY + '?startAt=' +
               str(start_day_second) + '&endAt=' +
               str(end_day_second) + '&limit=' + str(LIMIT_NEWS_GET))

        with requests.get(url) as r:
            return_json = r.json()
            statusCode = return_json['statusCode']

            if statusCode == 422:
                raise Usage(return_json['message'])
            else:
                if not os.path.exists(DATA_DIR_PATH):
                    os.makedirs(DATA_DIR_PATH)

                count = 0
                data = r.json()['items']['data']
                for d in data:
                    title = d['title']
                    publish_time = datetime.fromtimestamp(
                        int(d['publishAt'])).strftime('%Y-%m-%d_%H-%M-%S')
                    news_id = d['newsId']
                    f = open(DATA_DIR_PATH + str(count) +
                             '_' + publish_time + '.txt', 'w')
                    f.write('Title\n')
                    f.write(title + '\n')
                    f.write('Publish Time\n')
                    f.write(publish_time + '\n')
                    f.write('Content\n')
                    content_url = NEWS_CONTENT_URL + str(news_id) + '?exp=a'

                    with requests.get(content_url) as c_r:
                        soup = BeautifulSoup(c_r.text, 'html5lib')
                        content = soup.find(
                            'div', {'itemprop': 'articleBody', }).find_all('p')
                        for match in content:
                            f.write(str(match.text))
                    count = count + 1
                    logging.info('Finish')
                    return 0
    except Usage as err:
        logging.error(err.msg)
        return 2


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    sys.exit(main())
