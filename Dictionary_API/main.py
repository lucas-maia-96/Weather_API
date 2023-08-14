from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def about(word):
    n_word = word.upper()
    result_dictionary = {"definition": n_word,
            "word": word}
    return result_dictionary

if __name__ == "__main__":
    app.run(debug=True)