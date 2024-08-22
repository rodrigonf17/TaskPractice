from flask import Flask, render_template
import requests

app = Flask(__name__)


API_URL = 'http://localhost:8055/items/Projects'
@app.route('/')
def index():
    try:
        response = requests.get(API_URL)
        data = response.json()

        if 'data' in data:
            items = data['data']
        else:
            items = []

        return render_template('index.html', items=items)

    except Exception as e:
        return f"Erro ao acessar a API: {e}"

if __name__ == '__main__':
    app.run(debug=True)
