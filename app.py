from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)

# Configure the API key
palm.configure(api_key='AIzaSyBIGETjjp18ap_9kc5_R4FI_O7eFQUkBlc')

def generate_response(query):
    try:
        # Make the API request
        response = palm.generate_text(
            model='models/chat-bison-001',
            prompt=f"""Ti si Andrija Mohorovičić, poznati hrvatski znanstvenik, odgovori na ovo pitanje kao da si on: {query}""",
            temperature=0.7,
            max_output_tokens=1024,
        )

        # Log the raw response for debugging
        print(f"API Response: {response}")

        # Check for valid response content
        if response and 'candidates' in response and len(response['candidates']) > 0:
            # Extract the text from the first candidate
            return response['candidates'][0]['output']
        else:
            return "No valid response in API result."

    except Exception as e:
        # Log and return a generic error message
        print(f"Error occurred: {e}")
        return "Došlo je do pogreške prilikom generiranja odgovora. Molimo pokušajte ponovo."

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        query = request.form.get("query")
        print(f"Received query: {query}")
        
        if query:
            response = generate_response(query)
        else:
            response = "Nema upita."
    return render_template("index.html", response=response)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
