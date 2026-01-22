from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Get API key from environment variable
GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')

# Global variables
conversation_history = []

def chat_with_groq(message, history):
    """Send message to Groq API and get response"""
    if not GROQ_API_KEY:
        return "Please set your GROQ_API_KEY environment variable. Get a free key at https://console.groq.com"
    
    try:
        # Build messages array
        messages = [
            {"role": "system", "content": "You are a helpful, friendly AI assistant. Give clear, accurate, and concise answers."}
        ]
        
        # Add conversation history
        for i in range(0, len(history), 2):
            if i < len(history):
                messages.append({"role": "user", "content": history[i]})
            if i + 1 < len(history):
                messages.append({"role": "assistant", "content": history[i + 1]})
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        # Call Groq API
        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {GROQ_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'llama-3.3-70b-versatile',  # Free, fast, and good quality
                'messages': messages,
                'temperature': 0.7,
                'max_tokens': 500
            },
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"API Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history
    
    try:
        user_input = request.json.get('message', '').strip()
        
        if not user_input:
            return jsonify({'error': 'No message provided'}), 400
        
        print(f"\n👤 User: {user_input}")
        
        # Get response from Groq
        response = chat_with_groq(user_input, conversation_history)
        
        # Store in conversation history
        conversation_history.append(user_input)
        conversation_history.append(response)
        
        # Keep history manageable (last 10 exchanges)
        if len(conversation_history) > 20:
            conversation_history = conversation_history[-20:]
        
        print(f"🤖 Bot: {response}\n")
        
        return jsonify({'response': response})
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({'response': f"Sorry, I encountered an error: {str(e)}"})

@app.route('/reset', methods=['POST'])
def reset():
    global conversation_history
    conversation_history = []
    print("🔄 Chat history reset\n")
    return jsonify({'status': 'Chat history reset successfully'})

@app.route('/test')
def test():
    api_status = "✅ Set" if GROQ_API_KEY else "❌ Not set"
    return f'''
    <html>
    <head><title>Server Status</title></head>
    <body style="font-family: Arial; padding: 50px; background: #f5f5f5;">
        <div style="background: white; padding: 30px; border-radius: 10px; max-width: 600px;">
            <h1>🤖 Flask Server Status</h1>
            <p style="font-size: 18px;">Server: ✅ Running</p>
            <p style="font-size: 18px;">Groq API Key: {api_status}</p>
            <hr>
            {'' if GROQ_API_KEY else '<p style="color: red;">⚠️ Please set GROQ_API_KEY environment variable</p>'}
            <p><a href="/" style="color: #667eea; text-decoration: none; font-weight: bold;">→ Go to Chatbot</a></p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Starting AI Chatbot Server...")
    print("="*60 + "\n")
    
    if GROQ_API_KEY:
        print("✅ Groq API key found!")
        print("🌐 Server ready! Open your browser:")
    else:
        print("⚠️  WARNING: GROQ_API_KEY not set!")
        print("\n📝 To set your API key:")
        print("   1. Get a FREE API key at: https://console.groq.com")
        print("   2. Run: export GROQ_API_KEY='your-key-here'")
        print("   3. Restart the server\n")
        print("🌐 Server starting (will show error until API key is set):")
    
    print("   🌐 http://127.0.0.1:5000")
    print("   🌐 http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)