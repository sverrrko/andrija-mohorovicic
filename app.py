from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)

palm.configure(api_key='AIzaSyBIGETjjp18ap_9kc5_R4FI_O7eFQUkBlc')

def generiraj_odgovor(upit):
  """Generira odgovor od Gemini API-ja."""
  odgovor = palm.generate_text(
      model='models/chat-bison-001',
      prompt=f"""Ti si Andrija Mohorovičić, poznati hrvatski znanstvenik. 
      Odgovori na sljedeće pitanje kao da si on: {upit}""",
      temperature=0.7,
      max_output_tokens=1024,
  )
  return odgovor.result

@app.route("/", methods=["GET", "POST"])
def index():
  """Prikazuje chatbot sučelje i obrađuje korisničke upite."""
  odgovor = None
  if request.method == "POST":
    upit = request.form["upit"]
    odgovor = generiraj_odgovor(upit)
  return render_template("index.html", odgovor=odgovor)

if __name__ == "__main__":
  app.run(debug=True)
