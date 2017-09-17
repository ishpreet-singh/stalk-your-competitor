import sys, getopt, csv, urllib2
from bs4 import BeautifulSoup, NavigableString

def find_problems(username, app):
	try:
		user_problems = []
		app_url = ''

		if app == 'codechef':
			app_url = 'https://www.codechef.com/users/'
		
		destination_url = app_url + username
		page = urllib2.urlopen(destination_url)
		soup = BeautifulSoup(page, 'html.parser')

		for article in soup.find_all('article'):
			for para in article:
				if not isinstance(para, NavigableString) and para!=None and para.span!=None:
					for problem in para.span:
						if problem.string != ", ":
							user_problems.append(problem.string)

		return user_problems
	except:
		print 'Make sure you enter correct values. Either the app/username or some of the above mentioned competitors does not exist!'
		sys.exit()

def find_diff(user_solved_problems, competitor_solved_problems):
	user_problems = {}
	user_unsolved_problems = []
	for problem in user_solved_problems:
		user_problems[str(problem)]=1
	for problem in competitor_solved_problems:
		if str(problem) not in user_problems:
			user_unsolved_problems.append(str(problem))
	return user_unsolved_problems

def download_csv(unsolved_problems):
	with open('your_comparision','wb') as file:
		wr = csv.writer(file, dialect='excel')
		wr.writerow(["Index\tProblem Id\tProblem URL"])
		for problem in range(0,len(unsolved_problems)):
			wr.writerow( [problem+1, unsolved_problems[problem], 'https://www.codechef.com/problems/' + unsolved_problems[problem] ])

def print_diff(unsolved_problems, app):
	app_url = ''
	if app == 'codechef':
		app_url = 'https://www.codechef.com/problems/'

	for problem in range(0, len(unsolved_problems)):
		print problem+1, unsolved_problems[problem], app_url + unsolved_problems[problem]

def stalk_competitor(argv):
	app = ''
	username = ''
	competitors = []
	try:
		opts, args = getopt.getopt(argv,"ha:u:c:d:",["app=","username=","competitor="])
	except getopt.GetoptError:
		print 'usage: python main.py -u user_handle -c competitor_handle'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'usage: python main.py -u user_handle -c competitor_handle'
			sys.exit()
		elif opt in ("-a", "--app"):
			app = arg
		elif opt in ("-u", "--username"):
			username = arg
		elif opt in ("-c", "--competitor"):
			competitors = arg.split(",")

	competitor_solved_problems = []
	user_solved_problems = find_problems(username, app)
	for competitor in competitors:
		competitor_solved_problems.extend(find_problems(str(competitor), app))
	unsolved_problems = find_diff(user_solved_problems, competitor_solved_problems)
	print_diff(unsolved_problems, app)
	download_csv(unsolved_problems)

if __name__ == "__main__":
	stalk_competitor(sys.argv[1:])