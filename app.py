from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to AWS Real-Time CI/CD Project!"

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run()