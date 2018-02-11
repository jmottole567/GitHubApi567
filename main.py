import requests
import json

def getRepos(userName):
    repos = []
    response = requests.get('https://api.github.com/users/' + userName +'/repos')
    data = json.loads(response.text)
    for repo in data:
        repos += [repo.get('name')]
    return repos

def getNumCommits(userName, repoName):
    commits = requests.get('https://api.github.com/repos/' +userName+'/' + repoName + '/commits')
    commits_data = json.loads(commits.text)
    return len(commits_data)

if __name__ == "__main__":
    user = raw_input("Enter a Github username to view their repositories ")
    print "User: " + user

    repos = getRepos(user)

    for r in repos:
        print "Repo: " + r + " Number of Commits: " + str(getNumCommits(user,r))