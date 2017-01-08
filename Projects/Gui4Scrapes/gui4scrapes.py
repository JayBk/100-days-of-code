from tkinter import *
from tkinter import ttk
from redditscr import *
from scraping import *


def scrapereddit():
    top = Toplevel()
    top.title('Your Headlines!')

    subreddit = redditEntry.get()
    titles = CheckReddit(subreddit)
    redditEntry.delete(0, "end")
    showFont = ("Verdana", 16)
    Label(top, text='Top headlines in /r/{}!'.format(subreddit), font=("Comic Sans MS'", 24, "underline")).pack()
    showPosts = Message(top, text=titles.final, font=showFont)
    showPosts.pack(pady=50)
    # Button(top, text="Quit", command=top.destroy()).pack(side=BOTTOM, fill=X)
    top.focus_force()
    top.mainloop()
    return top


def scrapestocks():
    top2 = Toplevel()
    top2.title('Stock Market Data!')
    # print(stockEntry.get())
    abbrevs = stockEntry.get().split(" ")
    # print(abbrevs)
    stockData = CheckStocks(abbrevs)
    stockEntry.delete(0, "end")
    dFont = ("Verdana", 12)
    # myl = Label(top2, text='Stock Market Data For {}!'.format(abbrevs), font=("Verdana", 22, "underline"))
    # myl.pack()
    stockPf = stockData.mypf
    stockTi = stockData.titles
    # showStocks = Text(top2)
    # showStocks.pack()
    # showStocks.insert('end', stockDf)
    # showStocks = Message(top2, text=stockDf, font=dFont)
    # showStocks.pack()

    for j, title in enumerate(stockTi):
        Label(top2, text='Data for {}.'.format(title), font=("Verdana", 16, "underline")).grid(row=0, column=j, padx=25)

    for jj, ser in enumerate(stockPf):
        Message(top2, text=ser, font=dFont).grid(row=1, column=jj, padx=25)

    top2.focus_force()
    top2.mainloop()
    return top2


root = Tk()  # Makes the basic window

redditFrame = Frame(root).grid(row=0, column=0, sticky=W, padx=100)
stockFrame = Frame(root).grid(row=0, column=1, sticky=E, padx=100)

redText = StringVar()
stockText = StringVar()

# Create the reddit label and button
redditLabel = Label(redditFrame, textvariable=redText).grid(row=1, column=0, sticky=W)
redditEntry = Entry(redditFrame)
redditEntry.grid(row=2, column=0, sticky=W)
redditButton = Button(redditFrame, text='Scrape Reddit', command=scrapereddit)
redditButton.grid(row=3, column=0, sticky=W)

# Create the stock label and button
stockLabel = Label(stockFrame, textvariable=stockText).grid(row=1, column=1, sticky=E)
stockEntry = Entry(stockFrame, width=30)
stockEntry.grid(row=2, column=1, sticky=E)
stockButton = Button(stockFrame, text='Scrape Stocks', command=scrapestocks)
stockButton.grid(row=3, column=1, sticky=E)
# Setting the text for the labels(Could also do it when creating label)
redText.set('Scrape a subreddit\'s headlines.\nEnter subreddit name exactly.')
stockText.set('Get the stock market data for companies.\nEnter abbreviations separated by a space.')

root.mainloop()  # Keeps the window open until it is closed.
