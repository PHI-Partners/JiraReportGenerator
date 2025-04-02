import requests
import environment_variables as env
import utils
# ------------------------Fetch Jira Data------------------------------------------
def fetch_jira_data():
    ## To get all tickects updated in the last month
    JQL_QUERY = "updated >= startOfMonth(-1) AND updated < startOfMonth()"
    AUTH = (env.USER_EMAIL, env.API_TOKEN)
    JIRA_API_URL = f"https://{env.JIRA_DOMAIN}/rest/api/3/search?jql={JQL_QUERY}"
    response = requests.get(JIRA_API_URL, auth=AUTH , headers=env.HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        exit()

#jira_data = fetch_jira_data()
jira_data = utils.jira_data
print(f"Total Tickets Retrieved: {jira_data['total']}")

