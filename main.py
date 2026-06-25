import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Мой мобильный сервер</title>
            <style>
                body { font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #f0f2f5; }
                h1 { color: #1877f2; }
                p { font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>Привет от Pydroid 3! 🚀</h1>
            <p>Этот сайт работает прямо на сервере в интернете!</p>
            <p>Привет моим друзьям из другого города!</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

