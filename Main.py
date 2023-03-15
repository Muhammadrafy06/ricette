from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("ricette.html")

@app.route('/pasta', methods=['GET'])
def pasta():
    return render_template("pasta.html")

@app.route('/pizza', methods=['GET'])
def pizza():
    return render_template("pizza.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)