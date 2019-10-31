#!/usr/bin/env python3

import subprocess, time, sys, os, re

def formatJiraName(name):
    tokens = name.split('.')

    if len(tokens) != 2:
        print("Incorrect username: " + name)
        return name
    return tokens[0].capitalize() + " " + tokens[1].capitalize()

def getCurrentBranch():
    byte = subprocess.check_output("git rev-parse --abbrev-ref HEAD",shell=True)
    return byte.decode('utf8')

def getRepo(branch):
    if branch == 'master':
        return 'liferay-portal'
    return 'liferay-portal-ee'

def submitPR(reviewer, branch, ticketLink):
    repo = getRepo(branch)

    byte = subprocess.check_output("gh pr -s " + reviewer + " -r " + repo + " -b " + branch + " --description \"https://issues.liferay.com/browse/" + str(ticketLink) + "\" --title \"" + str(ticketLink) + " | " + branch + "\"",shell=True)
    output = byte.decode('utf8')

    print(output)

    pullRequestLink = re.search(r"https://github\.com/.*?/.*?/pull/\d+",output)

    if pullRequestLink == None:
        print("An error has occured, please use Node GH normally to check for the error")
        exit(1)
    return pullRequestLink.group(0)