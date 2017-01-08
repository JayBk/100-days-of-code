import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd

class CheckStocks(object):
    """A class that initiates taking companies stock market names abbreviation's and checks yahoo finance for their most recent
    information and puts the results into a pandas DataFrame"""
    def __init__(self, symb=None):
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

            tagged_values = soup.find_all("td", {'class': 'Ta(end) Fw(b)'})
            tagged_titles = soup.find_all("td", {'class': 'C(black)'})
            tagged_index = soup.find_all("h1", {'class': 'D(ib) Fz(18px)'})

            datadict[sym] = pd.Series([x.get_text() for x in tagged_values], index=[t.get_text() for t in tagged_titles])
            datalist.append(datadict[sym])
            datadict['titles'] = [i.get_text() for i in tagged_index]
            titlelist.append(datadict['titles'])
            # print(datadict[sym])
        self.titles = titlelist
        self.mypf = datalist
        # make the DataFrame from all of the data we got
        # print(datadict)
        # print(datalist)
        # print(titlelist)
        # titlelist = [title for sub in titlelist for title in sub]
        # mydf = pd.DataFrame(datalist, index=[title for sub in titlelist for title in sub])
        # self.mydf = mydf
