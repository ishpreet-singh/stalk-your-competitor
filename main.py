import sys, getopt, csv, urllib2
from bs4 import BeautifulSoup, NavigableString

def find_problems(username, app):
	try:
		user_problems = []
		problem_urls = []
		app_url = ''

		if app == 'codechef' or app == 'cc':
			app_url = 'https://www.codechef.com/users/'
			problem_url = 'https://www.codechef.com/problems/'
		elif app == 'spoj' or app == 'sp':
			app_url = 'https://www.spoj.com/users/'
			problem_url = 'https://www.spoj.com/problems/'
		elif app == 'codeforces' or app == 'cf':
			app_url = 'http://www.codeforces.com/submissions/'
		
		destination_url = app_url + username
		req = urllib2.Request(destination_url, headers={'User-Agent' : "Magic Browser"}) 
		page = urllib2.urlopen(req)
		soup = BeautifulSoup(page, 'html.parser')

		if app == 'codechef' or app == 'cc':
			for article in soup.find_all('article'):
				for para in article:
					if not isinstance(para, NavigableString) and para!=None and para.span!=None:
						for problem in para.span:
							if problem.string != ", ":
								user_problems.append(problem.string)
								problem_urls.append(problem_url + problem.string)

		elif app == 'spoj' or app == 'sp':
			article = soup.find('table', attrs={'class': 'table-condensed'})
			for row in article:
				for data in row:
					if not isinstance(data, NavigableString) and data!=None:
						for problem in data:
							for problem_code in problem:
								print("problem_code: ", problem_code)
								if problem_code!="" and problem_code!=" " and problem_code!="\n":
									user_problems.append(str(problem_code))
									problem_urls.append(problem_url + str(problem_code))

		elif app == 'codeforces' or app == 'cf':
			for row in soup.find_all('span', attrs={'submissionverdict': 'OK'}):
				problem = row.parent.parent.find_all('a')[2]
				if problem['href'].find('problemset') != -1:
					user_problems.append(problem.text.strip())
					problem_urls.append(problem['href'])

		return user_problems, problem_urls
	except:
		print 'Make sure you enter correct values. Either the app/username or some of the above mentioned competitors does not exist!'
		sys.exit()

def find_diff(user_solved_problems, competitor_solved_problems, problem_urls):
	user_problems = {}
	user_unsolved_problems = []
	diff_problem_urls = []
	for problem in user_solved_problems:
		user_problems[str(problem)]=1
	for problem in range(0,len(competitor_solved_problems)):
		if str(competitor_solved_problems[problem]) not in user_problems:
			user_unsolved_problems.append(str(competitor_solved_problems[problem]))
			diff_problem_urls.append(problem_urls[problem])
	return user_unsolved_problems, diff_problem_urls

def download_csv(unsolved_problems, problem_urls):
	with open('your_comparision','wb') as file:
		wr = csv.writer(file, dialect='excel')
		wr.writerow(["Index\tProblem Id\tProblem URL"])
		for problem in range(0,len(unsolved_problems)):
			wr.writerow( [problem+1, unsolved_problems[problem], problem_urls[problem] ])

def print_diff(unsolved_problems, app, problem_urls):
	for problem in range(0, len(unsolved_problems)):
		print problem+1, unsolved_problems[problem], problem_urls[problem]

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
			app = arg.lower()
		elif opt in ("-u", "--username"):
			username = arg.lower()
		elif opt in ("-c", "--competitor"):
			competitors = arg.split(",")

	competitor_solved_problems = []
	solved_problems, solved_problems_url = find_problems(username, app)
	problem_urls = []
	user_solved_problems = solved_problems
	for competitor in competitors:
		solved_problems, solved_problems_url = find_problems(str(competitor), app)
		competitor_solved_problems.extend(solved_problems)
		problem_urls.extend(solved_problems_url)
	unsolved_problems, diff_problem_urls = find_diff(user_solved_problems, competitor_solved_problems, problem_urls)
	print_diff(unsolved_problems, app, diff_problem_urls)
	download_csv(unsolved_problems, diff_problem_urls)

if __name__ == "__main__":
	stalk_competitor(sys.argv[1:])