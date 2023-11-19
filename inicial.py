from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # app.run(debug=True,port=80, host='0.0.0.0')
    serve(app, host="0.0.0.0", port=80)

# teste gerenciador de esteiras





