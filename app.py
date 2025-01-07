from flask import Flask, render_template, request
import google.generativeai as palm
import os

app = Flask(__name__)

palm.configure(api_key=os.getenv('AIzaSyBIGETjjp18ap_9kc5_R4FI_O7eFQUkBlc'))

def generiraj_odgovor(upit):
    print(f"Generating response for query: {upit}")
    try:
        odgovor = palm.generate_text(
            model='models/chat-bison-001',
            prompt=f"""Ti si Andrija Mohorovičić, hrvatski znanstvenik i seizmolog, odgovori na slijedeće pitanje kao da si on: {upit}""",
            temperature=0.7,
            max_output_tokens=1024,
        )
        print(f"Raw API response: {odgovor}")
    except Exception as e:
        print(f"Error during API request: {e}")
        return "Error during request"

    if odgovor and 'candidates' in odgovor and len(odgovor['candidates']) > 0:
        response_text = odgovor['candidates'][0]['output']
        print(f"Chatbot Response: {response_text}")
        return response_text
    else:
        print("No valid response from the API.")
        return "No valid response from the API."

@app.route("/", methods=["GET", "POST"])
def index():
    odgovor = None
    if request.method == "POST":
        upit = request.form.get("query", "").strip()
        print(f"User query: {upit}")
        if upit:
            odgovor = generiraj_odgovor(upit)
        else:
            odgovor = "Please enter a question."
        print(f"Response being passed to template: {odgovor}") 
    return render_template("index.html", response=odgovor)

if __name__ == "__main__":
    app.run(debug=True)
