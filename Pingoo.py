from flask import Flask
import requests

app = Flask(__name__)

@app.route("/ping")
def ping():
    try:
        response = requests.get("https://www.yosdfutube.com")
        return "The shit is up!"
    except:
        return "The shit is down!"

if __name__ == "__main__":
    app.run()