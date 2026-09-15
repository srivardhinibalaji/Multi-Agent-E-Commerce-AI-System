# Multi-Agent-E-Commerce-AI-System

# 🤖 Multi-Agent E-Commerce Assistant

A multi-agent e-commerce assistant built using **Google Agent Development Kit (ADK)** and the **Gemini API**.

The project demonstrates how multiple specialized AI agents can collaborate to handle an end-to-end shopping workflow.

## 🚀 Features

- Product browsing and cart management
- Multiple items and quantities
- Checkout confirmation
- Automatic order ID generation
- Order summary generation
- Agent-to-agent transfer
- Session state management
- Tool/function calling

## 🧩 Agent Architecture

The system consists of four specialized agents:
### 📦 E-Commerce Agent
Root Agent 
- Stores customer name, email, mobile number in session state 
- Routes to product catalog

### 🛍️ Catalog Agent
Handles:
- Product selection
- Adding items to cart
- Quantity management
- Cart total

### 💳 Checkout Agent
Handles:
- Checkout confirmation
- Customer information
- Shipping information
- Order ID generation

### 📋 Order Summary Agent
Generates:
- Customer details
- Ordered items
- Quantities
- Prices
- Shipping address
- Order ID
- Grand total

## 🔄 Workflow

User
↓
Ecommerce Agent
↓
Catalog Agent
↓
Checkout Agent
↓
Order Summary Agent

Agents communicate through **agent transfer**, while important information is maintained using **session state**.

## 🛠️ Technologies

- Python
- Google ADK
- Gemini API
- Google AI Studio
- Multi-Agent Systems
- Generative AI
- Session State
- Tool Calling

## 📚 Key Learning

This project helped me understand how to move beyond a single LLM chatbot and design a modular **multi-agent AI workflow**, where each agent has a specific responsibility and can transfer tasks to another agent when required.

## 🔮 Future Improvements

- Database integration
- Real-time order tracking
- Payment integration
- External e-commerce APIs
- Persistent order history
- Deployment
