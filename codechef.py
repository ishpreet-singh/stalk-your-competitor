import requests
from bs4 import BeautifulSoup, NavigableString

class Codechef():

    url = ""
    problems_url = ""

    def __init__(self):
        self.url = "https://www.codechef.com/users/"
        self.problems_url = "https://www.codechef.com/problems/"

    
    def is_valid_user(self, username):
        url = self.url + username
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        articles = soup.find_all('article')
        data = [row for article in articles for row in article if not isinstance(row, NavigableString) and row is not None and row.span is not None]
        return len(data) > 0
        
    
    def get_user_problems(self, username):
        url = self.url + username
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        articles = soup.find_all('article')
        data = [row for article in articles for row in article if not isinstance(row, NavigableString) and row is not None and row.span is not None]
        problems = [str(problem) for row in data for para in row.span for problem in para if problem not in [' ', ',', ', ']]
        urls = [str(self.problems_url + user_problem) for user_problem in problems]
        return problems, urls
    

if __name__ == "__main__":
    sp = Codechef()
    sp.get_user_problems("ishpreet")