import json

# Load dummy data
jira_data = json.loads('''{
  "total": 5,
  "issues": [
    {
      "key": "JIRA-101",
      "fields": {
        "summary": "Fix login issue",
        "status": { "name": "Done" },
        "assignee": { "displayName": "John Doe" },
        "priority": { "name": "High" },
        "created": "2025-02-10",
        "updated": "2025-03-25"
      }
    },
    {
      "key": "JIRA-102",
      "fields": {
        "summary": "Implement new payment gateway",
        "status": { "name": "In Progress" },
        "assignee": { "displayName": "Jane Smith" },
        "priority": { "name": "Medium" },
        "created": "2025-02-15",
        "updated": "2025-03-27"
      }
    },
    {
      "key": "JIRA-103",
      "fields": {
        "summary": "Refactor API endpoints",
        "status": { "name": "To Do" },
        "assignee": { "displayName": "Michael Lee" },
        "priority": { "name": "Low" },
        "created": "2025-02-20",
        "updated": "2025-03-30"
      }
    },
    {
      "key": "JIRA-104",
      "fields": {
        "summary": "Design UI for new dashboard",
        "status": { "name": "In Review" },
        "assignee": { "displayName": "Emily Davis" },
        "priority": { "name": "High" },
        "created": "2025-02-25",
        "updated": "2025-03-28"
      }
    },
    {
      "key": "JIRA-105",
      "fields": {
        "summary": "Fix mobile responsiveness",
        "status": { "name": "Done" },
        "assignee": { "displayName": "Chris Brown" },
        "priority": { "name": "Medium" },
        "created": "2025-02-12",
        "updated": "2025-03-26"
      }
    }
  ]
}''')


