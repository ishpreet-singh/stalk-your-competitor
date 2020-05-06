import requests
from bs4 import BeautifulSoup, NavigableString

class Codeforces():

    url = ""
    problems_url = ""

    def __init__(self):
        self.url = "https://codeforces.com/submissions"
        self.submission_url = "https://codeforces.com/submissions/"

    
    def is_valid_user(self, username):
        url = self.submission_url + username
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        articles = soup.find_all('span', attrs={'submissionverdict': 'OK'})
        return len(articles) > 0
        
    
    def get_user_problems(self, username):
        url = self.submission_url + username
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        articles = soup.find_all('span', attrs={'submissionverdict': 'OK'})
        problems = [str((row.parent.parent.find_all('a')[2]).text).strip() for row in articles]
        urls = [str((row.parent.parent.find_all('a')[2]['href'])).strip() for row in articles]
        urls = [str(self.url + url) for url in urls]
        return problems, urls
    

if __name__ == "__main__":
    cf = Codeforces()
    cf.get_user_problems("ishpreet")