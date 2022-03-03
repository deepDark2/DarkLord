#weather.py
from urllib import request;

import bs4


def getdata():
    target = request.urlopen('https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108');
    soup = bs4.BeautifulSoup(target,'html.parser');
    wlist = [];
    for city in soup.select('location'):
        st = '%s:%s(%s~%s)';
        name = city.select_one('city').string;
        wf = city.select_one('wf').string;
        tmn = city.select_one('tmn').string;
        tmx = city.select_one('tmx').string;
        wlist.append(st% (name, wf, tmn, tmx))

    return  wlist;


if __name__ == '__main__':
    result = getdata();
    print(result);