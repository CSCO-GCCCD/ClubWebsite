from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        return render_template('index.html', name=name)
    return render_template('index.html')
@app.route('/home', methods=['GET'])
def home():
    return "Home"
@app.route('/github', methods=['GET'])
def github():
    return render_template('Github.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)