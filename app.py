from flask import Flask

app = Flask(__name__)

HTML = open("dashboard.html", "r", encoding="utf-8").read()

@app.route("/")
def dashboard():
    return HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
