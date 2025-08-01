from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    """A simple endpoint to confirm the service is running."""
    return "Welcome to the Request Dispatch Service!"

@app.route('/health')
def health_check():
    """A standard health check endpoint for monitoring."""
    return jsonify(status="ok"), 200

@app.route('/fetch', methods=['POST'])
def fetch_url():
    """
    Receives a URL in a JSON payload, fetches its content,
    and returns the content.
    """
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify(error="URL is required"), 400

    url_to_fetch = data['url']
    headers = {
        'User-Agent': 'Scraper-v2.0-Dispatch'
    }

    try:
        response = requests.get(url_to_fetch, headers=headers, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        
        return response.text, response.status_code
    
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    # The port should be 5001 to match what's in the Dockerfile
    app.run(host='0.0.0.0', port=5001)