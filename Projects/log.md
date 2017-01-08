## My personal log that I started writing to locally

##Day 1

Day 1:

```
        again = True
        while again:
            choice = input('Would you like to search again? (y/n): ')
            if choice is 'y':
                check_stocks()
                break
            if choice is 'n':
                search = False
                break
            elif choice is not 'y' or choice is not 'n':
                print('Please Enter "y", or "n".')
```

Been trying this shit forever... I'm done with that for now... I'll incorperate another search again option tomorrow or another day.
I was also trying to use try and except and using an Exception I created but still couldnt get it to work :/...
 
**NOTE:** Also, why don't you have the results saved to a file or something like that?
 
Adding .lower() after the input stuff fucks it up for some reason.. even doing choice = choice.lower() afterwards fucks everything up...

I spent a shitload of time on mydater= pd.Series([x.get_text() for x in tagged_values], index=[t.get_text() for t in tagged_titles])
 
I kept getting results like:
 ```
 <bound method Tag.get_text of <td class="C(black)" data-reactid="352"><span data-reactid="353">Previous Close</span></td>>      115.05
    
 <bound method Tag.get_text of <td class="C(black)" data-reactid="356"><span data-reactid="357">Open</span></td>>       116.03
    
 <bound method Tag.get_text of <td class="C(black)" data-reactid="360"><span data-reactid="361">Bid</span></td>>       116.65 x 200
 ```

Instead of:

```
Previous Close               115.05

Open                         116.03

Bid                    116.65 x 200
```

All because I was using: t.get_text instead of t.get_text() ...

I was also having some trouble getting the text(`get_text()`) for the index's(`tagged_index`) because at first I was trying to append
tagged_index to titlelist, and then when I was making the DataFrame, tried saying `index=[title.get_text() for title in titlelist]` but
that didn't work, so then I tried appending and using get.text at the same time like: `titlelist.append(tagged_index.get_text)` but that
didn't work... I kept on getting: `AttributeError: 'ResultSet' object has no attribute 'get_text'`. So I then tried something like 
appending tagged_index to titlelist and then right before making the DataFrame; doing `titlelist = [title.get_text() for title in 
titlelist]`... But that didn't work lol. I thought for a while and then finally settled on putting it into my datadict like I am with 
the data itself, and while I add it to the datadict I'm using list comprehension to get_text(),  `datadict['titles'] = [i.get_text() 
for i in tagged_index]` and then I', appending it to my titlelist so I doing it a few different ways but then just settled on putting it
into my datadict, using list comprehension, then appending it to my titlelist after that.

NEVERMIND. Still having problems with the index's I want to use for my DataFrame... My titlelist is returning something like this: 
`[['Alphabet Inc. (GOOG)'], ['Facebook, Inc. (FB)']]`, and when I try and create my DataFrame like this:
`df = pd.DataFrame(datalist, index=titlelist)` I get: `ValueError: Shape of passed values is (16, 3), indices imply (16, 1`).. Which
I am assuming is from how my titlelist is, I need to fix it.. Asked a friend about this, and he said I should look up list flattening.
Did some research and found this: `[item for sublist in l for item in sublist]` on stack overflow, going to incorperate that now, and If
i can get the titles to work... IM DONE(for today). Ahh ok, think I got it :D (Thanks Yatri for explaining it to me) I'm going to
flatten my titlelist right before I make my DataFrame. Wait... Why can't I do that while I'm making the DataFrame? Who said I
can't? Well, let me go see if i can!... It does work :D ... So I finally ended up with
`mydf = pd.DataFrame(datalist, index=[title for sub in titlelist for title in sub])` ... Good :).

Well, that wraps up Day 1 of #100 days of code at 11:55pm on 1/3/2017... This took me much longer than I expected because of the 
problems I was having incorperating a custom exception for searching again or not, and I was using try: and except: wrong and 
`myinput.lower()` was messing up my `if choice is 'y' ` for some reason, then I forgot parenthesis on `get_text()` and that took me 
about 30 minutes to figure out lol. Then I was having trouble using `get_text()` for the titlelist and had to figure out how I could do
that... and THEN I was having trouble using titlelist, then figured out that it looked like 
`[['Alphabet Inc. (GOOG)'], ['Facebook, Inc. (FB)']]` and then Yatri told me to check out flattening and that was a HUGE help. Now it's
12:01am hahaa I still have to put this on GitHub. I'd like to also incorperate this into a Jupyter Notebook and put it on GitHub because
it looks pretty cool.. Now just to figure out how :D.

Goodnight!



##Day 2:

DAY 2:
It's 1:35am in the morning and I have to be up early and I've been having trouble sleeping as it is. I've been coding since about 11:30ish- I was going to use selenium to get hockey scores for whatever team you want
but that didn't work out, and by then it was 12, and I was about to say fuck it, but then remembered that I watched a video by sentdex on his reddit worldnews alexa skills app using flask-ask and some other stuff. I
did some more research into the reddit api, and came up with the code I have. It let's you enter the exact subreddit you want the first 10 values for and prints it out. My new endgame here is to incorporate what I made
yesterday, and what I made today, and maybe some more stuff, into a nice object oriented GUI with buttons for each "scrape" using PyQT. Today wasn't really a good day, I just wasn't really feeling it, and I wasn't going
to do the challenge today but I'm glad I stuck with it. Oh, I also made my stock market scraper a little more object oriented so that when I make the PyQT app, it's ready-ish(I'm sure I'll have to make a shitload of 
changes anyway lol)

##Day 3:

DAY 3:
Ok, maybe i'll get done before 12am today? Doubtful... But I really can't stay up late, I need to try and go to sleep earlier because I've been barely getting any sleep and it's really effecting
me.. I'm exhausted throughout the day and have been waking up late- which is bad because I have a lot of stuff to do throughout the day even though I'm unemployed at the moment(I have class at night(6-8ish)
Well, here goes nothing- I'll get started using PyQt, and see what I can get done today :). I also need to work on my Coursera work which I've been slacking on and I don't want to fall behind so I might not go
too much passed an hour today..
OK, i decided to use tkinter, but I have to write some stuff down real quick:
So for both buttons I need to have it so that If you click on it, they'll pop up a new message screen with the message..
OK- It's 2:05AM... I'm done... I'm having a lot of errors, but I'll work on it more when I wake up. Right now I just created the function for the reddit scraping button, and I'm running into trouble importing things,
I think I'm just too tired to notice shit right now lol. I built the basic GUI, added buttons ,labels and entries.. So now I'm just really trying to work on the functionality of the buttons.
________________________________________________________________________________________________________________________
Errors that I was running into before I stopped. vvvvvv
```
C:\Users\jkopp\Python\Python35-32\python.exe C:/Users/jkopp/PycharmProjects/Day1Selenium/gui4scrapes.py
Traceback (most recent call last):
  File "C:/Users/jkopp/PycharmProjects/Day1Selenium/gui4scrapes.py", line 3, in <module>
    from scrapeget import *
  File "C:\Users\jkopp\PycharmProjects\Day1Selenium\scrapeget.py", line 4, in <module>
    from gui4scrapes import *
  File "C:\Users\jkopp\PycharmProjects\Day1Selenium\gui4scrapes.py", line 19, in <module>
    redditButton.bind("<Button-1", scrapeReddit())
AttributeError: 'NoneType' object has no attribute 'bind'

Process finished with exit code 1
```
________________________________________________________________________________________________________________________

##DAY 4:

Day 4:
Okay, 12:06AM, I've been working on my GUI for hours..I am proud to say the reddit scrape button functionality is FULLY FUNCTIONAL!!!!!! The popup window it makes is pretty nice.. As nice as I can get with some
simple font parameters lol.. Anyway, I was so happy when I got that working fully... :D So I moved onto the stock scraping one, which is a little different because I want to display a DataFrame, and theres a
lot more data than just 10 sentences of headlines like the reddit scrape one.. Also, a DataFrame can get really messy looking and confusing if it isn't displayed right, and I don't want mine to look
all yucky.. First I tried displaying it the same way as I was displaying the reddit stuff just to see what would happen, and the first things I tried were "FB GOOG AAPL", which should've given me back
Facebook, Google, and Apple's stock market info. For some reason I got a 404... Since I've made and tested the stock scraper I've NEVER gotten a 404 so I was like wtf? For some reason I thought that the way
I was displaying it was fucking everything up somehow, so I did some research and then decided to try displaying it as Text(window) instead of Message(window)- like how I was displaying the reddit stuff. So
I went and changed it to use Text, and then spun it up again.. For some reason this time I only typed in 'FB', and of course; it worked.. But something was wrong: Instead of displaying Facebook it was displaying
Ford Motor Company (F), and Barnes Group Inc. (B), for some reason.. [How it Looks Using Text(window)](http://imgur.com/Wvw4zbb) ... And [How it Looks Using Message(window)](http://imgur.com/vqUufAe) This means
that it is interpreting every letter It get's as a different "entry", so I need to see why and fix that, because the abbreviations are supposed to be separated by spaces, but wait... oh shit..
 I only ever set that up for input() in scraping.py... I never set it up for the Entry() for the gui.. ooohhhh okay. I see now- I'll work on that tomorrow. OK, I'm glad I noticed that now :).
 Ok, so tomorrow I need to work on not only the formatting of how to display the DataFrame but I need to also work on how to get the Entry() to work the right way either like I had it before, or maybe
 they could even be separated by commas... Alright, I'll work on it tomorrow, hopefully I'll get everything uploaded to gist/github and be done by 1:00AM.. It's 12:46 right now.. Day 4 Complete!
 
 
 ##DAY 5:

**Holy Shit Day 5!?**
 
Day 5:
12:09AM D: lol after 12 again! W.e I accept the fact I'll be done after 12 every day... So today I needed to fix the Entry() and how I was displaying the dataframe, I'll start with the Entry.. I did some
research but I didn't find anything that related to what I had in mind, so I just started messing around with things.. I tried list comprehension, but all that did was throw errors at me and after some rigging
I got a list in a list which I didn't want because I already had to get rid of a list within a list on Day 1 I think when I made this, so no sense bringing it back into a list of a list lol.. I ended up looking
at scraping.py(the file that scrapes the data)(which i should've done in the first place) and realized that I used .split(" ") for the input there, and that it would probably work if I implemented it for
 the Entry... Sure as shit it did! Now onto displaying the data.. I tried so many different ways and spent at least an hour and a half researching and implementing random things, trying to install a package
 called pandastable, which kept failing to install because of one of it's dependencies; so then I tried to install the dependency first but that was failing to install. I said fuck it and decided to keep
 trying random things. After a little bit of random implementations again I was at a loss for trying to display the dataframe in a nice way... I decided to try using a pandas series, and a single one came
 out pretty good, so I tried two. When I tried two there was one on top and one on the bottom, and the form was a little messed up, but nothing that I couldn't fix because they were two separate series.
 I tried stuff like adding a newline("\n") and two tabs("\t\t") between the two since I was returning a list of series, and figured I'd just but newlines or tabs to space them apart.. Nice try but no. It
 didn't work out as planned. Again, I was at a loss for how I could properly display my data. Then I thought, well what If I could display each series separately, in it's own Message()? To make that work nicely
 I would somehow have to have them all in different columns depending on how many companies a person scrapes... I thought about it for a while and played with some nested for loops, and trying to use all kinds 
 of different combinations of using "and" between stuff.. Then I finally realized that I could just use two separate for loops using enumerate() so I could have the numbers for the columns and the data for the
 Message(the series), and the Label(the titles). The numbers for the columns needed to match up for the Labels and the Message, so the Labels are always in row 0, column X, and the Messages are always in 
 row 1, column X.. It ended up working and looking beautiful(in my opinion). So that was my day 4 100daysofcode.. I think I may be done with this project now :O I will probably start something new tomorrow!
