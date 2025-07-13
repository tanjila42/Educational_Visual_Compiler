def generate_symbol_table(lexical_tokens):
    """
    Generates a symbol table from the lexical tokens.
    The symbol table contains unique identifiers and their types.
    """
    symbol_table = {}

    # Iterate over the lexical tokens and add identifiers to the symbol table
    for token in lexical_tokens:
        if token["type"] == "IDENTIFIER":
            # Add identifier to the symbol table (assuming type is not provided, we'll add it later)
            if token["value"] not in symbol_table:
                symbol_table[token["value"]] = {"type": "unknown"}  # Default type is unknown
                
                
        if token["type"] == "KEYWORD" and token["value"] == "int":
            # For simplicity, assume 'int' keyword means the variable type is 'int'
            next_token = lexical_tokens[lexical_tokens.index(token) + 1]  # Next token is the identifier
            if next_token["type"] == "IDENTIFIER":
                symbol_table[next_token["value"]]["type"] = "int"


    # # You can improve this by assigning types based on other logic (e.g., if it's assigned a value)
    # for token in lexical_tokens:
    #     if token["type"] == "KEYWORD" and token["value"] == "int":
    #         # For simplicity, assume 'int' keyword means the variable type is 'int'
    #         next_token = lexical_tokens[lexical_tokens.index(token) + 1]  # Next token is the identifier
    #         if next_token["type"] == "IDENTIFIER":
    #             symbol_table[next_token["value"]]["type"] = "int"

    # Example symbol table:
    # {'x': {'type': 'int'}, 'y': {'type': 'int'}}
    return symbol_table
