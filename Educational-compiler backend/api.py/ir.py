def generate_ir(ast):
    """
    Generates intermediate representation (IR) from the AST.
    This is a simplified IR generation for a basic expression.
    """
    return {
        "instructions": [
            f"LOAD {ast['left']['value']}",
            f"ADD {ast['right']['value']}",
            "STORE result"
        ]
    }