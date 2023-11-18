from flask import Flask, request
import tiktoken

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/get_token_count", methods=['POST'])
def token_count():
    text = request.form.get('data')
    
    # Assuming 'tiktoken' is a module for tokenizing, and it's correctly set up for your needs
    encoding = tiktoken.get_encoding("cl100k_base")  # If this is needed for the setup
    encoding = tiktoken.encoding_for_model('gpt-4')
    encoded_text = encoding.encode(text)
    
    return {"Tokens": get_num_tokens(encoded_text)}

def get_num_tokens(encoded_text):
    # The encoded text is already passed, no need to re-encode
    num_tokens = len(encoded_text)
    return num_tokens

if __name__ == "__main__":
    app.run(debug=True)