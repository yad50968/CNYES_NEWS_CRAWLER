# CNYES_NEWS_CRAWLER
Easily getting the news from [CNYES](https://www.cnyes.com/index.htm).
Each article will be saved to your local dir. 

### INFO
ONLY FOR EDUCATION 方便從鉅亨網抓取新聞資料，供學術使用

### Requirements
1. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [request](http://docs.python-requests.org/en/master/)
3. [python3](https://www.python.org/)

### SETTING DAYS
```
#   SEARCH START DAY AND END DAY
#   MAXIMUM RANGE IS TWO MONTHS

START_DAY = '2017/12/01 00:00:00'
END_DAY = '2017/12/02 00:00:00'
```

### SETTING CATEGORY
```
# SET WHICH CATEGORY YOU WANT TO SEARCH:
# headline, all, tw_stock, wd_stock, cn_stock, forex, future

CATEGORY = 'headline'
```

### RUN
```
git clone https://github.com/yad50968/CNYES_NEWS_CRAWLER.git
cd CNYES_NEWS_CRAWLER
python3 ./main.py
# ARTICLES WILL BE SAVED TO ./data/ DIR
```
