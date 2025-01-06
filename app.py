from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)

palm.configure(api_key='YOUR_API_KEY')

def generate_response(query):
    try:
        
        response = palm.chat(
            model="models/chat-bison-001", 
            messages=[{"role": "user", "content": query}],  
        )
        
       
        if 'candidates' in response and len(response['candidates']) > 0:
            return response['candidates'][0]['content']
        else:
            return "U moje vrijeme se nismo koristili ovakvim riječnikom, pokušaj ponovo."
    except AttributeError as e:
        print(f"AttributeError occurred: {e}")
        return "Došlo je do pogreške prilikom dohvaćanja odgovora. Molimo pokušajte ponovo."
    except KeyError as e:
        print(f"KeyError occurred: {e}")
        return "Došlo je do pogreške u procesu odgovora. Molimo pokušajte ponovo."
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Došlo je do pogreške prilikom generiranja odgovora."

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
