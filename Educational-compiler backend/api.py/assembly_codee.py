def generate_assembly_code(ir):
    """
    Generates assembly code from the intermediate representation (IR).
    This is a simplified version for illustrative purposes.
    """
    return {
        "code": [
            f"MOV AX, {ir['instructions'][0].split(' ')[1]}",
            f"ADD AX, {ir['instructions'][1].split(' ')[1]}",
            "MOV result, AX"
        ]
    }