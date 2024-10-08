from flask import Flask, render_template, request
from db_connection import get_data_from_db
from model_training import generate_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        db_data = get_data_from_db(query)
        prompt = " ".join([str(item) for item in db_data])  # Juntar os dados
        generated_text = generate_text(prompt)
        return render_template("index.html", text=generated_text)
    return render_template("index.html", text="")

if __name__ == "__main__":
    app.run(debug=True)
