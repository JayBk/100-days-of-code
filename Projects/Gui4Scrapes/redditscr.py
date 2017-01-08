import json
import requests
import unidecode
import time


class CheckReddit(object):
    def __init__(self, subreddit=None):
        if subreddit is None:
            subreddit = input('Enter the subreddit you wan\'t to check(Exactly):')
        credentials = {'user':'websitethrowawayi',
                       'passwd': 'incognitomode',
                       'api_type':'json'}
        session = requests.Session()
        session.headers.update({'User-Agent':'#100daysofcode :D'})
        session.post('https://www.reddit.com/api/login', data=credentials)
        time.sleep(1)  # JUST WAIT A SECOND WHAT'S THE RUSH!?!?!?

        url = 'https://reddit.com/r/{}/.json?limit=10'.format(subreddit)
        html = session.get(url)
        data = json.loads(html.content.decode('utf-8'))
        posts = [unidecode.unidecode(headlines['data']['title']) for headlines in data['data']['children']]
        self.posts = ['{}. {}'.format(num+1, post) for num, post in enumerate(posts)]
        self.final = "\n".join(self.posts)
