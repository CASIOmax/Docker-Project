from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Docker Flask App</title>
            <style>
                body { font-family: Arial; text-align: center; padding: 50px; background: #f0f0f0; }
                h1 { color: #007bff; }
            </style>
        </head>
        <body>
            <h1>Hello, Docker!</h1>
            <p>This Flask app is running inside a Docker container.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
