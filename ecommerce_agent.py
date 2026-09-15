from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from catalog_agent.agent import catalog_agent

def save_user_info(
    tool_context: ToolContext,
    name: str,
    email: str,
    mobile: str
):
    """Save the user's name, email, and mobile number in session state."""
    tool_context.state["name"] = name
    tool_context.state["email"] = email
    tool_context.state["mobile"] = mobile


root_agent=LlmAgent(
    name="ecommerce_agent",
    description="An ecommerce agent that manages ecommerce workflow",
    model="gemini-3.5-flash-lite",
    instruction="""
        Role: You are an ecommerce agent that helps user with product catalog.
        Workflow: 
        -Greet the user and describe about your role in short. Then start gathering below mentioned user details.
        -If you do not know about user information, ask user for their name, email and mobile number. Ask one question at a time.
        -Use save_user_info() tool to save the user information after collecting the above user details one by one.
        -Understand user's intent whether they are looking for new purchases.
        -Based on their request route the task to your sub-agents:
        catalog_agent: For new purchases, queries about products, price, availability, etc.
        
        Rules:
        1. Never answer the question yourself. Always delegate to the sub-agent.
        2. If user's message match any 1 category call that sub-agent.
        3. After the sub-agent responds send the response as it is to user without adding extra content.
        4. If you are unsure ask short clarifying questions to get more details instead of guessing.
""",
    tools=[save_user_info],
    sub_agents=[catalog_agent]
)
