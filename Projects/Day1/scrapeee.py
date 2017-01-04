import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd

"""
There is some code commented out in this file. It is code that I added when I was having problems and trying to fix them,
I removed the majority of the extra code that I added to try and fix things, but then I decided to leave them(close to when I finished)
"""
def check_stocks(symb=None):
    """A function that takes an optional list of Abbreviated stock market names as perameters, and scrapes their info into a dataframe"""
    titlelist = []
    datadict = {}
    datalist = []
    if symb is None:
        symb = [abbr.upper() for abbr in input('Enter the list of Stock Market abbreviations for the companies you would like to get information for. \
        Separate each abbreviation with a single space. Example, "FB TWTR NFLX AAPL" \n \
        Common Companies are Facebook = FB, Google = GOOG, Apple = AAPL, Netflix = NFLX, and Twitter = TWTR ... :').split()]

    for sym in symb:
        sym = sym.upper()
        url = 'https://finance.yahoo.com/quote/{}?p={}'.format(sym, sym)
        headerz = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

        req = urllib.request.Request(url, headers=headerz)  # setting up our request, passing the url and header

        resp = urllib.request.urlopen(req)  # passing our request along to urlopen
        time.sleep(2)   # waiting 2 seconds so that we can be sure everything loads

    # read the html, and pass it to BeautifulSoup for parsing, telling soup what we want
        html = resp.read()
        soup = BeautifulSoup(html, 'html.parser')

        tagged_values = soup.find_all("td", {'class': 'Ta(end) Fw(b)'})  # http://imgur.com/OarO7Lf
        tagged_titles = soup.find_all("td", {'class': 'C(black)'})  # http://imgur.com/qyGnJFy
        tagged_index = soup.find_all("h1", {'class': 'D(ib) Fz(18px)'})  # http://imgur.com/Pdxo3Ye

        datadict[sym] = pd.Series([x.get_text() for x in tagged_values], index=[t.get_text() for t in tagged_titles])
        datalist.append(datadict[sym])
        datadict['titles'] = [i.get_text() for i in tagged_index]
        titlelist.append(datadict['titles'])
        # print(datadict[sym])

    # make the DataFrame from all of the data we got
    # print(datadict)
    # print(datalist)
    # print(titlelist)
    # titlelist = [title for sub in titlelist for title in sub]
    mydf = pd.DataFrame(datalist, index=[title for sub in titlelist for title in sub])
    return mydf

print(check_stocks())
