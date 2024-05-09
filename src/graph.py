
#Using LangGraph we can say how to move between different actions
#Check for email-->Write draft--> Wait if we do not find any email
class WorkFlow():
    def __init__(self):
       workflow = StateGraph(EmailsState)
       
       #define actions
       workflow.add_node("check_new_emails", nodes.check_new_email)
       workflow.add_node("wait_next_run", nodes.wait_mext_run)
       workflow.add_node("draft_response", EmailFilterCrew().kickoff)
       
       #how to move between actions
    #    check_new_email->wait_mext_run
    #    check_new_email->draft_response
    #Based on condition connect different nodes
    #decision tree here
       workflow.add_confidtional_edges(
           "check_new_emails",#condition
           #check new email if we do draft response
           nodes.new_emails,
           {
               "continue": "draft_responses",#response 1 of condition
               "end": "wait_mext_run" #response 2 of condition
           }
       )     
       
       workflow.add_edge("draft_responses","wait_mext_run")
       workflow.add_edge("wait_mext_run","check_new_email")
       self.app = workflow.compile)(