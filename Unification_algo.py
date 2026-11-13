def unify(a, b, sub):
    if a == b:
        return True

    if a in sub:
        return unify(sub[a], b, sub)

    if b in sub:
        return unify(a, sub[b], sub)

    if a.islower() and a.isalpha():
        sub[a] = b
        return True

    if b.islower() and b.isalpha():
        sub[b] = a
        return True

    return False


def check_unification(exp1, exp2):
    name1 = exp1.split("(")[0].strip()
    name2 = exp2.split("(")[0].strip()

    p1 = exp1[exp1.index("(")+1:exp1.rindex(")")].split(",")
    p2 = exp2[exp2.index("(")+1:exp2.rindex(")")].split(",")

    sub = {}

    if name1 != name2 or len(p1) != len(p2):
        return False, sub

    for a, b in zip(p1, p2):
        if not unify(a.strip(), b.strip(), sub):
            return False, sub

    return True, sub


test_cases = [
    ("Eats(x, Apple)", "Eats(Riya, y)"),
    ("Eats(y, Apple)", "Eats(Riya, y)"),
    ("P(x, h(y))", "P(a, f(z))"),
    ("Likes(x, Apple)", "Eats(Riya, y)")
]

for i, (exp1, exp2) in enumerate(test_cases, 1):
    result, sub = check_unification(exp1, exp2)

    print("Expression 1:", exp1)
    print("Expression 2:", exp2)

    if result:
        print("Unification Successful")
        print("Substitution:", sub)
        print("\n")
    else:
        print("Unification Failed \n")
