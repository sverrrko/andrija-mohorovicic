from flask import Flask, render_template, request
from gemini import Gemini

app = Flask(__name__)

gemini = Gemini(api_key='API_KEY')

def generate_response(query):

    response = gemini.generate_text(
        model="models/chat-bison-001",
        prompt=f"""Ti si Andrija Mohorovičić, poznati hrvatski znanstvenik, odgovori na ovo pitanje kao da si ti on: {query}""",
        temperature=0.7,
        max_output_tokens=1024,
    )
    return response


@app.route('/', methods=['GET', 'POST'])
def home():
    response = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = get_response(user_input)
        print(response)
    return render_template('index.html', response=response)


