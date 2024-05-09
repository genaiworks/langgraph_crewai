from typing import TypedDict

# State helps us memorize what we have done in the past.
# how many emails we have sent
# which emails we have checked
# what draft emails we have created

class EmailsState(TypedDict):
    #have we checked these emails in past
    checked_emails_ids: list[str]
    #all emaanets we have 
    emails: list[dict]
    #action required to on emails like writing drafts
    action_required_emails: dict