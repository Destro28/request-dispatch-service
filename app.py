from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Request Dispatch Service!"

@app.route('/health')
def health_check():
    return jsonify(status="ok"),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
