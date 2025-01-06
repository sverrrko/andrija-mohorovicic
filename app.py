from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)

# Configure the Gemini API
palm.configure(api_key='AIzaSyBIGETjjp18ap_9kc5_R4FI_O7eFQUkBlc')  # Replace 'YOUR_API_KEY' with your actual API key

def generiraj_odgovor(upit):
    """Generira odgovor od Gemini API-ja."""
    try:
        # Call Gemini API to generate a response
        odgovor = palm.generate_text(
            model='models/chat-bison-001',
            prompt=f"""Ti si Andrija Mohorovičić, poznati hrvatski znanstvenik. 
            Odgovori na sljedeće pitanje kao da si on: {upit}""",
            temperature=0.7,
            max_output_tokens=1024,
        )

        # Check if a valid response exists
        if odgovor and 'candidates' in odgovor and len(odgovor['candidates']) > 0:
            response_text = odgovor['candidates'][0]['output']
            # Print the response to the console for logging
            print(f"Chatbot Response: {response_text}")
            return response_text
        else:
            # If there's no valid response from the API
            print("No valid response from the API.")
            return "Nema valjanog odgovora iz API-ja."
    except Exception as e:
        # Log the error in the console
        print(f"Došlo je do pogreške: {e}")
        return "Došlo je do pogreške prilikom generiranja odgovora. Molimo pokušajte ponovo."

@app.route("/", methods=["GET", "POST"])
def index():
    """Prikazuje chatbot sučelje i obrađuje korisničke upite."""
    odgovor = None
    if request.method == "POST":
        upit = request.form.get("upit", "").strip()
        if upit:
            odgovor = generiraj_odgovor(upit)
        else:
            odgovor = "Molimo unesite upit."
    return render_template("index.html", odgovor=odgovor)

if __name__ == "__main__":
    app.run(debug=True)

