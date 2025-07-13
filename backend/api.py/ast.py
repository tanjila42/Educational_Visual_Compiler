def generate_ast(parse_tree):
    """
    Generates an Abstract Syntax Tree (AST) from the parse tree.
    This is a simple mock-up.
    """
    return {
        "name": "AddExpression",
        "left": {"name": "Identifier", "value": parse_tree["children"][0]["value"]},
        "right": {"name": "Identifier", "value": parse_tree["children"][2]["value"]}
    }