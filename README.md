# ghPRext
Extension script that utilizes node-gh and extension gh-jira to automate pull requests more efficiently

# Requirements
Python 3

Install node gh
npm install -g gh

Install gh jira
npm install -g gh gh-jira

Populate ghPR.py with the github and jira usernames of the people you send pull requests to
example: 
# THE PEOPLE YOU SEND PRS TO #
reviewersDict = {
    'brianchandotcom':'brian.chan',
    'kyle-miho':'kyle.miho',
    'vicnate5':'victor.ware'
}

Create an alias that can call ghPR.py because it performs actions on the repo within the cwd

# Expected usage
1a) 'ghPR kyle-miho master' inside branch master-qa-42000 with most recent commit prefix LRQA-42000
A pull request will be sent to kyle-miho, with the title and link to the jira ticket already created in the description.
In the jira ticket, kyle-miho will be assigned as the new assignee and the ticket status will be changed to 'In Review'.
The current user will comment the qa standard of sending a ticket to the reviewed user.

1b) Same as 1a, except using an LPS ticket instead, with branch master-lps-42000 and LPS-4200 as recent commit prefix

2) 'ghPR brianchandotcom master' inside branch master-qa-52000 with most recent commit prefix LRQA-52000
The same as 1a, except since BChan doesn't autoclose LRQA project tickets after he merges them, the ticket will be autoclosed if
autoclosing LRQA tickets is enabled in the properties

3)'ghPR vicnate5 7.2.x' inside branch pr-204 with the most recent commit prefix 7.2.x-qa-30293
Since pr-204 is not of the correct branch format, we will fallback to using the commit prefix to grab the branch, project, and ticket number

4)'ghPR vicnate5 7.2.x' inside branch pr-302 wth the most recent commit prefix TEMP, and then 7.2.x-qa-40392
Since we can't fallback to the most recent commit due to its incorrect format, we will fall back to the next most recent commit instead.
