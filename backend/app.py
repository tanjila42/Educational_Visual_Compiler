from flask import Flask, jsonify, request
from flask_cors import CORS
from api.lexical_token import generate_lexical_tokens
from api.symbol_table import generate_symbol_table  # New import for Symbol Table generation
from api.parse_tree import generate_parse_tree
from api.ast import generate_ast
from api.ir import generate_ir 
from api.assembly_code import generate_assembly_code


app = Flask(__name__)
CORS(app)  # To allow cross-origin requests from frontend

@app.route('/compiler_data', methods=['POST'])
def compiler_data():
    """
    Endpoint to accept user input, process it, and return all compiler phase data.
    """
    try:
        # Get the user input from the POST request
        user_input = request.json.get("input")
        
        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        # Generate compiler phases from the input
        lexical_tokens = generate_lexical_tokens(user_input)
        
        # Generate Symbol Table after lexical analysis
        symbol_table = generate_symbol_table(lexical_tokens)
        
        parse_tree = generate_parse_tree(lexical_tokens)
        ast = generate_ast(parse_tree)
        ir = generate_ir(ast)
        assembly_code = generate_assembly_code(ir)

        # Return all the phases as JSON
        data = {
            "lexical_token": lexical_tokens,
            "symbol_table": symbol_table,  # Add symbol table to the data
            "parse_tree": parse_tree,
            "ast": ast,
            "ir": ir,
            "assembly_code": assembly_code
        }
        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)