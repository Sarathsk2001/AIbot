AIbot

Creating AI chat bot

Installation & Setup

Install Python
Install pip

If you have Python & pip installed then check their version in the terminal or command line tools

python3 --version
pip --version

Installing Flask
In your terminal run the requirements.txt file using this pip
pip install -r requirements.txt

Running ChatBot Application in Terminal
cd into your directory
python app.py

What you will create
In this tutorial, I will guide you through the process of building a chatbot that can carry out conversations with users using natural language processing.

To start, we will be using Groq API, a pre-trained language model that can generate human-like responses to given prompts. We will be integrating DialoGPT with Flask, a popular Python web framework, to create a web application that can communicate with users via a chat interface.

For the frontend of our application, we will be using HTML, CSS, and JavaScript to create a visually appealing and interactive chat interface. Additionally, we will be using jQuery to handle the HTTP requests that are made to the backend server.

Throughout the tutorial, I will provide step-by-step instructions on how to set up your development environment, install the necessary dependencies, and create the required files and code for the application. I will also explain how to train and fine-tune the DialoGPT model to improve the accuracy of its responses.

By the end of this tutorial, you will have a fully functional chatbot that can engage in conversations with users, and you will have gained valuable experience in using Microsoft DialoGPT, Flask, and web development technologies such as HTML, CSS, and JavaScript.

ChatBot Link
The Groq API Key is your access token to use Groq's powerful AI servers. When you type a message, your chatbot sends it to Groq's cloud computers (which run the Llama 3.3 AI model), and Groq sends back an intelligent response. The API key identifies your application and allows this communication to happen. It's completely free to get from https://console.groq.com.

Quick Setup

Get a free API key from https://console.groq.com

Set it in your terminal: export GROQ_API_KEY='your-key-here'

Install requirements: pip install -r requirements.txt

Run the app: python app.py

Open http://127.0.0.1:5000 in your browser

User-Html

Bot-HTML
