from flask import Flask, render_template
from monitor import get_server_status

app = Flask(__name__)

@app.route('/')
def index():
    status = get_server_status()
    return render_template('index.html', status=status)

if __name__ == '__main__':
    app.run(debug=True)
