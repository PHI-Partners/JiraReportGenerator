import utils
import jira_report_generation as jrp

jira_data = utils.jira_data
jrp.generate_pptx("template.pptx",jira_data)