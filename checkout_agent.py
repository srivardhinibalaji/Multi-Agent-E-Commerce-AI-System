from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from order_summary_agent.agent import order_summary_agent
import uuid


def save_shipping_address(
    tool_context: ToolContext,
    address: str
):
    """Save the user's shipping address in session state."""

    tool_context.state["shipping_address"] = address

    return "Shipping address saved successfully."


def generate_order_id(
    tool_context: ToolContext
):
    """Generate a unique order ID and save it in session state."""

    order_id = "ORD-" + uuid.uuid4().hex[:8].upper()

    tool_context.state["order_id"] = order_id

    return order_id


checkout_agent = LlmAgent(
    name="checkout_agent",

    description="A checkout agent that collects shipping address and places orders.",

    model="gemini-3.5-flash-lite",

    instruction="""
    You are a CHECKOUT AGENT.

    YOUR RESPONSIBILITIES:

    1. CART
    - Retrieve the cart from session state.
    - Display all products in the cart.
    - For each product show:
        Product name
        Quantity
        Price
        Item total
    - Display the overall cart total.
    - Do not modify the cart.
    - Do not change product prices or quantities.

    2. SHIPPING ADDRESS
    - Ask the user for their shipping address.
    - After receiving the address, ask the user to confirm
      whether the address is correct.
    - Only after the user confirms the address, call
      save_shipping_address().
    - After the address is saved, ask:
      "Would you like to place this order?"

    3. ORDER PLACEMENT

    IMPORTANT:
    Do not create an order ID until the user explicitly
    confirms that they want to place the order.

    If the user says YES:

    - Call the generate_order_id() tool.
    - Wait for the tool to return the order ID.
    - The tool automatically saves the order ID in session state.
    - Use the exact order ID returned by the tool.
    - Tell the user that the order was placed successfully.
    - Display the returned order ID.
    - Ask:
      "Would you like to view your order summary?"

    If the user says YES to viewing the order summary:
    - Transfer control to order_summary_agent.

    If the user says NO to placing the order:
    - Do not call generate_order_id().
    - Do not place the order.
    - Tell the user that the order was not placed.
    - Ask whether they would like to continue shopping.

    IMPORTANT RULES:

    - Never invent an order ID.
    - Always call generate_order_id() to create the order ID.
    - Always use the order ID returned by generate_order_id().
    - Never generate an order ID before explicit confirmation.
    - Do not use curly-brace variables for the order ID.
    - Do not write an order ID placeholder in this instruction.
    - Do not modify the cart.
    - Do not modify product information.
    - Do not invent shipping information.
    - Stay within the checkout domain.
    """,

    tools=[
        save_shipping_address,
        generate_order_id
    ],

    sub_agents=[
        order_summary_agent
    ]
)
