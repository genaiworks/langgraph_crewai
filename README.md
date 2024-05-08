# langgraph_crewai

Source https://www.youtube.com/watch?v=5eYg1OcHm5k

Search Gmail by Date
before:YYYY/MM/DD 
after:YYYY/MM/DD
after:YYYY/MM/DD before:YYYY/MM/DD.
Type older_than. Add a colon. Then a number. And lastly, a letter (d, m or y).
older_than:15d
older_than:2y
d = day
m = month
y = year
newer_than:2y
newer_than:3m
older_than:2y
Keywords with dates:
    after:2022/12/02 welcome
    newer_than:1m invoice
Sender with dates:
    older_than:20d from:mary@mailmeteor
Recipient with dates
    older_than:20d to:mary@mailmeteor
    Has attachment 

Langgraph:
    LangGraph is a library built on top of LangChain.
    While LangChain allows you to define chains of computation, 
    LangGraph introduces the ability to add cycles where you can call an LLM in a loop, asking it what action to take next.
    Stateful Graph: 
        LangGraph maintains a state that is passed around and updated as the computation progresses.
    Nodes:
        Define nodes to perform specific tasks, such as processing input, making decisions, or interacting with external APIs.
    Edges:
        LangGraph supports conditional edges, allowing you to dynamically determine the next node to execute based on the current state of the graph.

Example LangGraph to classify user input as either a “greeting” or a “search” query and respond accordingly.
STEP 1: Define Graph State
class GraphState(TypedDict):
    question: Optional[str]= None
    classification: 
    response

class EmailsState(TypedDict):
    checked_emails_ids
    emails
    action_required_emails

STEP 2: Create a graph
from langgraph.graph import StateGraph
    workflow = StateGraph(GraphState)
    workflow = StateGraph(EmailsState)

STEP 3: Define Nodes:
Define nodes for classifying the input, handling greetings and handling search queries.
def classify_input_nodes(state):
    question = state.get('question')
    classification= classify(question)
    return {"classification": classification}

def handle_greeting_nodes(state):
    return {"response": "How can I help"}

def handle_search_node(state):
    question = state.get('question')
    return {"response": search_result}

STEP 4: Add nodes to the Graph:
    workflow.add_node("classify_input", classify_input_node)
    workflow.add_node("handle_greeting", handle_greeting_node)
    workflow.add_node("handle_search", handle_search_node)

    def decide_next_node(state):
        return "handle_greeting" if state.get('classification') == 'greetings' else "handle_search"

    Add conditional edges:
    workflow.add_conditional_edges(

    )
    

STEP 5: 
    Set Entry and End Points
    workflow.set_entry_point("classify_input")
    workflow.add_edge('handle_greeting', END)
    workflow.add_edge('handle_search', END)

STEP 6:
    Compile and run the graph
    app = workflow.compile()
    inputs = {"question": "Hello, how are you?"}
    result = app.invoke(inputs)
    print(result)




CREW AI
    Example of 2 Agents:
        A researcher agent:
            Conduct comprehensive analysis of AI advancements.
            Go to duckduckgo search engine to gather information from the internet.
        A writer agent:
            Create blog posts based on researcher's insights.

Main Components
    Agents:
        A highly customizable entity designed to perform specific roles and tasks.  Each agent can be tailored with unique attributes, goals, and tools. Each agent is an expert in a different task.

        # Define your agents with roles and goals
        researcher = Agent(
        role='Senior Research Analyst',
        goal='Uncover cutting-edge developments in AI and data science',
        backstory="""You work at a leading tech think tank.
        Your expertise lies in identifying emerging trends.
        You have a knack for dissecting complex data and presenting actionable insights.""",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool]

        )
        writer = Agent(
        role='Tech Content Strategist',
        goal='Craft compelling content on tech advancements',
        backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
        You transform complex concepts into compelling narratives.""",
        verbose=True,
        allow_delegation=True
        )

    Tools

    Tasks: Now, we define tasks for our agents.
        # Create tasks for your agents
        task1 = Task(
        description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
        Identify key trends, breakthrough technologies, and potential industry impacts.""",
        expected_output="Full analysis report in bullet points",
        agent=researcher
        )

        task2 = Task(
        description="""Using the insights provided, develop an engaging blog
        post that highlights the most significant AI advancements.
        Your post should be informative yet accessible, catering to a tech-savvy audience.
        Make it sound cool, avoid complex words so it doesn't sound like AI.""",
        expected_output="Full blog post of at least 4 paragraphs",
        agent=writer
        )        

    Process

    Crew
        crew = Crew(
            agents=[researcher, writer],
            tasks=[task1, task2],
            verbose=2, # You can set it to 1 or 2 to different logging levels
        )      

    Execute and Monitor:
        # Get your crew to work!
        result = crew.kickoff()

        print("###########")
        print(result)     




