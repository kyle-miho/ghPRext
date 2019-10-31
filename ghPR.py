#!/usr/bin/env python3

import subprocess, time, sys, os, re, configparser
import ghPRUtil, setUp, ticketNumber

### ADJUST THESE #############
# THE PEOPLE YOU SEND PRS TO #
reviewersDict = {
    'brianchandotcom':'brian.chan',
    'kyle-miho':'kyle.miho',
    'vicnate5':'victor.ware'
}
###############################

if len(sys.argv) != 3:
    print("Arguments: ${Reviewer_Name} ${Branch_To_Submit_To}")
    exit()

reviewer=sys.argv[1]
branch=sys.argv[2]
jiraName = reviewersDict[reviewer]

setUp.setupConfig()

config = setUp.readConfig()

gitBranch = ghPRUtil.getCurrentBranch()
ticketNumber = ticketNumber.TicketNumber(gitBranch)

pullRequest = ghPRUtil.submitPR(reviewer,branch,ticketNumber)

subprocess.call("gh jira " + str(ticketNumber) + " --comment \"Pushed to " + ghPRUtil.formatJiraName(jiraName) + ".\n" + branch + ": " +  pullRequest + "\"",shell=True)

if ticketNumber.project == 'LRQA':
    if (jiraName == "brian.chan") and config['default'][closeLRQA] == 'y':
        subprocess.call("gh jira " + str(ticketNumber) + " --assignee " + config['default'][githubUserName] + " --transition \"Close\"",shell=True)
    else:
        subprocess.call("gh jira " + str(ticketNumber) + " --assignee " + jiraName + " --transition \"Submit for Review\"",shell=True)
elif ticketNumber.project == 'LPS':
    subprocess.call("gh jira " + str(ticketNumber) + " --assignee " + jiraName + " --transition \"Code Review Request\"",shell=True)