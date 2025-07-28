from flask import Flask, request, render_template, Response
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/browse", methods=["GET"])
def browse():
    url = request.args.get("url")
    if not url.startswith("http"):
        url = "http://" + url

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        return Response(resp.content, content_type=resp.headers.get('Content-Type', 'text/html'))
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
