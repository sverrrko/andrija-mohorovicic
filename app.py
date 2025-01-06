
from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)

palm.configure(api_key='AIzaSyBIGETjjp18ap_9kc5_R4FI_O7eFQUkBlc')

def generate_response(query):

    response = palm.generate_text(
        model='models/chat-bison-001',
        prompt=f"""Ti si Andrija Mohorovičić, poznati hrvatski znanstvenik, odgovori na ovo pitanje kao da si on: {query}""",
        temperature=0.7,
        max_output_tokens=1024,
    )
    return response.result

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        query = request.form["query"]
        response = generate_response(query)
    return render_template("index.html", response=response)



