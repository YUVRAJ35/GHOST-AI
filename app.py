from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- GHOST AI INTELLIGENCE ---
def get_ghost_response(user_input):
    """A simple dictionary-based AI for GHOST AI's brain."""
    
    # Standardize input for matching
    text = user_input.lower().strip()
    
    # 1. Greetings and Basics
    if any(word in text for word in ['hello', 'hi', 'hey', 'greetings']):
        return "👻 Hello there, mortal. I am GHOST AI. How can I assist you in this realm?"
    
    # 2. Personality/Identity
    elif any(word in text for word in ['who are you', 'your name']):
        return "I am GHOST AI, a digital entity dwelling within the code. I am here to answer your queries."
        
    # 3. Functions
    elif any(word in text for word in ['can you do', 'what do you do']):
        return "I can converse, answer questions based on my programming, and perhaps offer a chilling prediction. Try me!"
        
    # 4. Specific keywords/topics
    elif 'python' in text or 'code' in text:
        return "Ah, Python. A powerful script that summons vast capabilities. Need help with a snippet?"
        
    # 5. Default/Fallback
    else:
        return "I sense confusion... Your query echoes vaguely in this space. Could you phrase it differently?"

@app.route('/')
def index():
    """Serves the main HTML page for the web application."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint for handling user messages and sending back AI responses."""
    user_message = request.json.get('message')
    ai_response = get_ghost_response(user_message)
    
    # Send the AI response back as JSON
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    # Flask will automatically look for the index.html file inside a 'templates' folder.
    # We will run this on port 5000.
    app.run(debug=True)
