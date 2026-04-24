from pathlib import Path

from flask import Flask

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, root_path=str(BASE_DIR), instance_path=str(BASE_DIR / "instance"))

@app.route('/')
def home():
    return "Hello from Dockerised Flask!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
