def pl_true(sentence, model):

    if isinstance(sentence, str):
        return model[sentence]
    
    op = sentence[0]
    
    if op == 'NOT':
        return not pl_true(sentence[1], model)
    elif op == 'AND':
        return pl_true(sentence[1], model) and pl_true(sentence[2], model)
    elif op == 'OR':
        return pl_true(sentence[1], model) or pl_true(sentence[2], model)
    elif op == 'IMPLIES':
        return (not pl_true(sentence[1], model)) or pl_true(sentence[2], model)
    
    raise ValueError(f"Unknown logical operator: {op}")


def print_truth_table(kb, queries, symbols):
    query_names = list(queries.keys())
    header = symbols + ["S1(Q=>P)", "S2(P=>~Q)", "S3(Q|R)", "KB"] + query_names
    print(" | ".join(f"{h:>10}" for h in header))
    print("-" * (13 * len(header)))

    import itertools
    all_combinations = list(itertools.product([True, False], repeat=len(symbols)))

    for combo in all_combinations:
        model = dict(zip(symbols, combo))

        s1_val = pl_true(s1, model)
        s2_val = pl_true(s2, model)
        s3_val = pl_true(s3, model)
        kb_val = pl_true(kb, model)

        q_vals = [pl_true(queries[q], model) for q in query_names]
        
        row_vals = [model[sym] for sym in symbols] + [s1_val, s2_val, s3_val, kb_val] + q_vals
        row_str = " | ".join(f"{('T' if v else 'F'):>10}" for v in row_vals)

        if kb_val:
            print(f"{row_str}   <-- KB is TRUE")
        else:
            print(row_str)


def tt_entails(kb, alpha, symbols):

    return tt_check_all(kb, alpha, symbols, {})


def tt_check_all(kb, alpha, symbols, model):
    if not symbols:
        if pl_true(kb, model):
            return pl_true(alpha, model)
        else:
            return True
    else:
        P = symbols[0]
        rest = symbols[1:]
        
        model_true = model.copy()
        model_true[P] = True
        
        model_false = model.copy()
        model_false[P] = False
        
        return (tt_check_all(kb, alpha, rest, model_true) and tt_check_all(kb, alpha, rest, model_false))


s1 = ('IMPLIES', 'Q', 'P')
s2 = ('IMPLIES', 'P', ('NOT', 'Q'))
s3 = ('OR', 'Q', 'R')
kb = ('AND', s1, ('AND', s2, s3))
symbols = ['P', 'Q', 'R']

queries = {
    "Query: R": 'R',
    "Query: R=>P": ('IMPLIES', 'R', 'P'),
    "Query: Q=>R": ('IMPLIES', 'Q', 'R')
}

print(" TRUTH TABLE ")
print_truth_table(kb, queries, symbols)

print("\n ENTAILMENT RESULTS ")
for q_name, q_expr in queries.items():
    entails = tt_entails(kb, q_expr, symbols)
    symbol_res = "|=" if entails else "|/="
    print(f"KB {symbol_res} ({q_name}) : {entails}")
