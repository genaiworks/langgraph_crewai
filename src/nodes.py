import os
import time
from langchain_community.agent_tools import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch

#To perform actions at different states
# Different actions that we want to perform are listed in Nodes
class Nodes():
    def __init__(self):
        self.gmail = GmailToolkit()
    
    # first action check what emails are there
    #Check emails
    #Each node will have state input variable that is updated with each action
    def check_email(self, state):
        print("Checking emails")
        search = GmailSearch(api_resource=self.gmail.api_resource)
        # emails = search('after:newer_than:10d')
        emails = search('from:solvegenai@gmail.com')
        checked_emails =state['checked_email_ids'] if state['checked_email_ids'] else []
        thread =[]
        new_emails = []
        for email in emails:
            if email['id'] not in checked_emails:
                thread.append(email['threadId'])
                new_emails.append(
                    {
                    "id": email['id'],
                    "threaded": email['threadId'],
                    "snippet": email['snippet'],
                    "sender": email['sender']
                    }
                )
        checked_emails.extend([email['id'] for email in new_emails])
        #updateing emails and checked emails
        # here we are checking to find new emails, 
        # we are updating new emails updating any checked email ids so that we can skip checking emails
        #Here later variables override previous variables
        return{
            **state,
            # 'checked_email_ids': state.checked_emails,
            # 'emails': state.emails,
            # 'action_required_emails': state.action_required_emails,
            # these variables overwrite existing state variables
            "emails": new_emails,
            "checked_emails_ids": checked_emails
        }
    # wait for next run of check email
    #Wait
    def wait_next_run(self, state):
        pass
    
    #perform action on new emails
    #Write draft emails
    def new_email(self, state):
        pass
    