## My personal log that I started writing to locally

###Day 1

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



###Day 2:
DAY 2:
It's 1:35am in the morning and I have to be up early and I've been having trouble sleeping as it is. I've been coding since about 11:30ish- I was going to use selenium to get hockey scores for whatever team you want
but that didn't work out, and by then it was 12, and I was about to say fuck it, but then remembered that I watched a video by sentdex on his reddit worldnews alexa skills app using flask-ask and some other stuff. I
did some more research into the reddit api, and came up with the code I have. It let's you enter the exact subreddit you want the first 10 values for and prints it out. My new endgame here is to incorporate what I made
yesterday, and what I made today, and maybe some more stuff, into a nice object oriented GUI with buttons for each "scrape" using PyQT. Today wasn't really a good day, I just wasn't really feeling it, and I wasn't going
to do the challenge today but I'm glad I stuck with it. Oh, I also made my stock market scraper a little more object oriented so that when I make the PyQT app, it's ready-ish(I'm sure I'll have to make a shitload of 
changes anyway lol)

##Day 2:
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
