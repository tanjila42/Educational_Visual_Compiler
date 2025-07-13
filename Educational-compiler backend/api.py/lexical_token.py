import re

def generate_lexical_tokens(input_code):
    """
    Generates lexical tokens from the input code (simple lexer).
    """
    # Define regex patterns for basic tokens
    token_patterns = [
        ("KEYWORD", r"\b(int|float|if|else|while|return)\b"),
        ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
        ("NUMBER", r"\b\d+\b"),
        ("OPERATOR", r"[\+\-\*/=<>!]+"),
        ("PUNCTUATION", r"[;.,(){}]"),
        ("WHITESPACE", r"\s+"),
    ]
    
    # Combine patterns into one regex
    combined_pattern = "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_patterns)
    
    tokens = []
    for match in re.finditer(combined_pattern, input_code):
        kind = match.lastgroup
        value = match.group()
        if kind != "WHITESPACE":  # Ignore whitespace
            tokens.append({"type": kind, "value": value})
    
    return tokens