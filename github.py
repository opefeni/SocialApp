import json
import requests
from pprint import pprint


GITHUB_TOKEN = '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'
GITHUB_USERNAME = 'opefeni'
github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (GITHUB_USERNAME, GITHUB_TOKEN)

url = github_api + '/repos/rails/rails/issues?state=open'
issues_pg = gh_session.get(url = url)
issues_json = issues_pg.json()

#print(len(issues_json))
pprint(issues_json[20])
## parameters: assignee, comments,author_association, created_at,id, labels[name],milestone,reactions[total_count]
##             status,title,updated_at,user[login]

issue_pg_list = [dict(item, **{'repo_name':'{}'.format('rails')}) for item in issues_pg.json()] 
issue_pg_list = [dict(item, **{'owner':'{}'.format('owner')}) for item in issue_pg_list] 

pprint(issue_pg_list[20]) 
#pprint(issues_pg.headers['Link'])
