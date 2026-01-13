from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Street Vendor Business Intelligence System"

@app.route('/monthly_profit')
def monthly_profit():
    return jsonify({"monthly_profit": 12500})

@app.route('/best_selling')
def best_selling():
    return jsonify([
        ["Apple", 120],
        ["Banana", 200],
        ["Orange", 80]
    ])

if __name__ == '__main__':
    app.run(debug=True)
