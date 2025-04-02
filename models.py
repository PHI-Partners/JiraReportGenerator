from typing import Dict
from collections import defaultdict

class JiraReport:
    def __init__(
        self,
        total_issues: int,
        total_tickets: int,
        #business_units: Dict[str, int],
        statuses: Dict[str, int],
        priorities: Dict[str, int],
        #resolutions: Dict[str, int]
    ):
        self.total_issues = total_issues
        self.total_tickets = total_tickets
        #self.business_units = business_units
        self.statuses = statuses
        self.priorities = priorities
        #self.resolutions = resolutions

    @classmethod
    def from_json(cls, jira_data):
        """Parse complete Jira data including:
        - Business Units (custom field)
        - Statuses
        - Priorities
        - Resolutions
        """
        total = jira_data.get("total", 0)
        issues = jira_data.get("issues", [])

        # Initialize distributions
        distributions = {
            #"business_units": defaultdict(int),
            "statuses": defaultdict(int),
            "priorities": defaultdict(int),
            #"resolutions": defaultdict(int)
        }

        for issue in issues:
            fields = issue.get("fields", {})

            # 1. Business Units (Replace CUSTOM_FIELD_ID with your actual field ID)
            #business_unit = fields.get("customfield_12345", {}).get("value", "Unassigned")
            #distributions["business_units"][business_unit] += 1

            # 2. Statuses
            status = fields.get("status", {}).get("name", "Unknown")
            distributions["statuses"][status] += 1

            # 3. Priorities
            priority = fields.get("priority", {}).get("name", "Not Set")
            distributions["priorities"][priority] += 1

            # 4. Resolutions
            #resolution = fields.get("resolution", {}).get("name", "Unresolved")
            #distributions["resolutions"][resolution] += 1

        return cls(
            total_tickets=total,
            total_issues=len(issues),
            #business_units=dict(distributions["business_units"]),
            statuses=dict(distributions["statuses"]),
            priorities=dict(distributions["priorities"]),
            #resolutions=dict(distributions["resolutions"])
        )

    def __str__(self):
        return (
            f"JiraReport("
            f"Total Issues: {self.total_issues}, "
            f"Tickets: {self.total_tickets}, "
            #f"Business Units: {self.business_units}, "
            f"Statuses: {self.statuses}, "
            f"Priorities: {self.priorities})"
        )