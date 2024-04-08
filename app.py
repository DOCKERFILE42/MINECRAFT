from flask import Flask
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def index():
    # Example usage:
    url = "https://colab.research.google.com/drive/1MSA4lW8lxQZDyn5llaWzkFXUsM4397HQ?usp=sharing"
    quoted_url = quote(url)
    return f"Quoted URL: {quoted_url}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
