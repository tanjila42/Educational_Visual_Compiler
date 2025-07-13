from flask import Flask, jsonify

app = Flask(__name__)

# Sample Data to be returned by the backend (Adjust as per your requirements)
data = {
    "lexicalToken": [{ "type": "keyword", "value": "if" }, { "type": "identifier", "value": "x" }],
    "symbolTable": [{ "name": "x", "type": "int" }],
    "parseTree": {
        "name": "Program",
        "children": [{ "name": "Statement", "children": [] }]
    },
    "ast": {
        "name": "Expression",
        "children": [{ "name": "Literal", "children": [] }]
    },
    "ir": {
        "name": "IR1",
        "children": [{ "name": "IR2", "children": [] }]
    },
    "assemblyCode": "MOV AX, BX"
}

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)