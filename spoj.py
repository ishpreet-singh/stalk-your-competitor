import requests
from bs4 import BeautifulSoup, NavigableString

class Spoj():

    url = ""
    problems_url = ""

    def __init__(self):
        self.url = "https://www.spoj.com/users/"
        self.problems_url = "https://www.spoj.com/problems/"
        
    
    def get_user_problems(self, username):
        url = self.url + username
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        article = soup.find('table', attrs={'class': 'table-condensed'})
        data = [row for lines in article for row in lines if not isinstance(row, NavigableString) and row is not None]
        problems = [str(code) for problem in data for problem_code in problem for code in problem_code if code not in ["", " ", "\n"]]
        urls = [str(self.problems_url + user_problem) for user_problem in problems]
        return problems, urls
    

if __name__ == "__main__":
    sp = Spoj()
    sp.get_user_problems("ishpreet")