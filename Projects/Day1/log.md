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