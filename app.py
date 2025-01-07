from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)

palm.configure(api_key='AIzaSyBIGETjjp18ap_9kc5_R4FI_O7eFQUkBlc')  

def generiraj_odgovor(upit):
    """Generira odgovor od Gemini API-ja."""
    try:
      
        odgovor = palm.generate_text(
            model='models/chat-bison-001',
            prompt=f"""Ti si Andrija Mohorovičić, poznati hrvatski znanstvenik. 
            Odgovori na sljedeće pitanje kao da si on: {upit}""",
            temperature=0.7,
            max_output_tokens=1024,
        )

        if odgovor and 'candidates' in odgovor and len(odgovor['candidates']) > 0:
            response_text = odgovor['candidates'][0]['output']
            print(f"Chatbot Response: {response_text}")
            return response_text
        else:
            print("No valid response from the API.")
            return "Nema valjanog odgovora iz API-ja."
    except Exception as e:
        print(f"Došlo je do pogreške: {e}")
        return "Došlo je do pogreške prilikom generiranja odgovora. Molimo pokušajte ponovo."

@app.route("/", methods=["GET", "POST"])
def index():
    """Prikazuje chatbot sučelje i obrađuje korisničke upite."""
    odgovor = None
    if request.method == "POST":
        upit = request.form.get("query", "").strip()
        if upit:
            odgovor = generiraj_odgovor(upit)
        else:
            odgovor = "Molimo unesite upit."
    return render_template("index.html", odgovor=odgovor)

if __name__ == "__main__":
    app.run(debug=True)

