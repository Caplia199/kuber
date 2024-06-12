from flask import Flask, request, render_template
from calculator import safe_eval

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = safe_eval(expression)
    except Exception as e:
        result = f"Ошибка: {str(e)}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    print(f"Приложение запущено по адресу http://{host}:{port}/")
    app.run(host=host, port=port, debug=True)
