from flask import Flask
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def index():
    # Example usage:
    url = "https://example.com/path with spaces"
    quoted_url = quote(url)
    return f"Quoted URL: {quoted_url}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
