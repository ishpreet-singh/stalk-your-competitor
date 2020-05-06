
from spoj import Spoj

class Stalk():

    choice = 0
    
    def __init__(self):
        self.set_platforms()
        pass

    def set_platforms(self):
        self.platforms = {
            "Spoj": 1,
            "CodeChef": 2,
            "CodeForces": 3
        }

    def get_platforms(self):
        return self.platforms

    def get_choice(self):
        return self.choice
    
    def set_choice(self, choice):
        self.choice = choice
    
    def get_all_choices(self):
        return list(self.platforms.values())

    def set_username(self, username):
        self.username = username

    def get_username(self):
        self.username

    def set_competitor(self, competitor):
        self.competitor = competitor

    def get_competitor(self):
        self.competitor

    def get_menu(self):
        menu = "\nChoose Platform\n\n"

        for key, value in self.platforms.items():
            menu += f"{value}) {key}\n\n"
        
        self.menu = menu
        return self.menu

    def get_user_problems(self, user):
        spoj = Spoj()
        problems, urls = [], []
        if self.choice == 1:
            problems, urls = spoj.get_user_problems(user)
        
        user_problems = list(zip(problems, urls))
        return user_problems

    def get_user_choice(self):
        # return 1
        menu = str(self.get_menu())
        print(menu)
        print("Enter your choice: ", end = "")
        choice = int(input())

        while choice not in list(stalk.get_all_choices()):
            print("\nEnter a valid choice")
            print(menu, end = "")
            choice = int(input())
        
        self.set_choice(choice)
        return choice

    def get_user_input(self):
        # return "ishpreet", "karan_arora"
        print("\nEnter your username: ", end = "")
        username = input()
        # If Valid Username
        self.set_username(username)
        print("\nEnter your competitor: ", end = "")
        competitor = input()
        # If Valid Username
        self.set_competitor(competitor)
        return username, competitor


    def get_problems_solved_by_user(self, user_problems, competitor_problems):
        return list(set(user_problems) - set(competitor_problems))


    def get_problems_solved_by_both(self, user_problems, competitor_problems):
        return list(set(user_problems) & set(competitor_problems))


    def display_problems(self, problems):
        max_index_len = max(len(str(len(problems))), 5) + 2
        max_problem_len = max([len(prob[0]) for prob in problems]) + 2
        max_url_len = max([len(prob[1]) for prob in problems ]) + 2
        
        print("\n | ", end = "")
        print(f"Index".center(max_index_len, " "), end = " | ")
        print(f"Problem".center(max_problem_len, " "), end = " | ")
        print(f"URL".center(max_url_len), end = " | ")
        print("")
        print("-"*(max_index_len + max_problem_len + max_url_len + 12))

        for index, value in enumerate(problems):
            print(" | ", end = "")
            print(f"{index + 1}".center(max_index_len, " "), end = " | ")
            print(f"{value[0]}".center(max_problem_len, " "), end = " | ")
            print(f"{value[1]}".center(max_url_len), end = " | ")
            print("")


    def start_stalking(self):
        self.get_user_choice()
        self.get_user_input()
        
        user_problems = self.get_user_problems(self.username)
        competitor_problems = self.get_user_problems(self.competitor)
        problems_solved_by_user = self.get_problems_solved_by_user(user_problems, competitor_problems)
        problems_solved_by_competitor = self.get_problems_solved_by_user(competitor_problems, user_problems)
        problems_solved_by_both = self.get_problems_solved_by_both(competitor_problems, user_problems)

        print(f"\nProblems Solved by {self.competitor} and not by {self.username}:")
        self.display_problems(problems_solved_by_competitor)  
        print(f"\nProblems Solved by {self.username} and not by {self.competitor}:")
        self.display_problems(problems_solved_by_user)
        print(f"\nProblems Solved by both {self.username} and {self.competitor}:")
        self.display_problems(problems_solved_by_both)



if __name__ == "__main__":
    stalk = Stalk()
    stalk.start_stalking()
    