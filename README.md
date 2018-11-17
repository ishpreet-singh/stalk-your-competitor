# stalk-your-competitor

A python app to stalk your competitors on various online judges. 

Want to see your friends status on **Codechef** or want to complete all the problems that your competitor have done on Hackerrank. Try Stalk your Competitor.

# Steps to use the app

1. git clone https://github.com/ishpreet-singh/stalk-your-competitor
2. cd stalk-your-competitor
3. Make sure you have python & [pip](https://pip.pypa.io/en/stable/installing/) installed in your system.
4. Install dependencies: `pip install -r requirements.txt`.
5. Run the app using command: `python main.py -a app_name -u your_username -c competitor_username` 

Or `python main.py --app app_name --username your_username --competitor competitor_username`

Note: The result may take few seconds to fetch.

# Usage
1. **-a** or **--app**(Mandatory Argument) stands for App name Like **Codechef**(or **cc**), **Codeforces**(or **cf**), **Spoj**(or **sp**)
2. **-u** or **--username**(Mandatory Argument) stands for your username like **ishpreet**
3. **-c** or **--competitor**(Mandatory Argument) stands for competitor username like **saumye**. You can specify multiple username comma seprated like saumye,karan_arora. Make sure don't add space in multiple username.

# Results
The results are stored in your_comparision.csv
