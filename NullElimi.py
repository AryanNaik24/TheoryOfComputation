def eliminate_null_productions(grammar, nullables):
    """
    Eliminate null productions from a given context-free grammar.

    :param grammar: A dictionary representing the grammar.
                    The keys are non-terminal symbols, and the values are lists of productions.
    :param nullables: A set of nullable non-terminal symbols.
    :return: A dictionary representing the grammar without null productions.
    """
    new_grammar = {}

    for non_terminal, productions in grammar.items():
        new_productions = set()
        for production in productions:
            new_productions.update(
                generate_non_nullable_productions(production, nullables))
        new_grammar[non_terminal] = list(new_productions)

    return new_grammar


def generate_non_nullable_productions(production, nullables):
    """
    Generate all non-nullable productions for a given production.

    :param production: A list of symbols representing the production.
    :param nullables: A set of nullable non-terminal symbols.
    :return: A set of productions without nullables.
    """
    if not production:
        return {''}

    result = {tuple(production)}

    for i, symbol in enumerate(production):
        if symbol in nullables:
            sub_productions = generate_non_nullable_productions(
                production[:i] + production[i+1:], nullables)
            result.update(sub_productions)

    return {''.join(prod) for prod in result if ''.join(prod)}


# Example usage:
grammar = {
    'A': ['ABCABD', 'CD'],
    'B': ['Cb', ''],
    'C': ['a', ''],
    'D': ['bD', '']
}

# Known nullable variables
nullables = {'A', 'C', 'D'}

print("Original Grammar:")
for non_terminal, productions in grammar.items():
    print(f"{non_terminal} -> {' | '.join(productions)}")

new_grammar = eliminate_null_productions(grammar, nullables)

print("\nGrammar without Null Productions:")
for non_terminal, productions in new_grammar.items():
    print(f"{non_terminal} -> {' | '.join(productions)}")
