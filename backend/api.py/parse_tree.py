def generate_parse_tree(tokens):
    """
    Generates a simple parse tree from lexical tokens (mock example).
    Here, a real parser would convert tokens into a hierarchical tree.
    """
    # Simple mock-up: Assuming all input is a mathematical expression
    return {
        "name": "Expression",
        "children": [
            {"name": "Identifier", "value": tokens[0]["value"]},
            {"name": "Operator", "value": tokens[1]["value"]},
            {"name": "Identifier", "value": tokens[2]["value"]}
        ]
    }