def evaluer_condition(valeur, condition: str):
    condition = condition.strip()
    if "&&" in condition:
        gauche , droite = condition.split("&&")
        return evaluer_condition(valeur, gauche) and evaluer_condition(valeur, droite)
    # liste des opérateurs supportés
    operateurs = ['>=', '<=', '>', '<']
    for op in operateurs:
        if condition.startswith(op):
            try:
                limite = float(condition[len(op):].strip())
            except ValueError:
                return False 
            if op == '>=':
                return valeur >= limite
            elif op == '<=':
                return valeur <= limite
            elif op == '>':
                return valeur > limite
            elif op == '<':
                return valeur < limite
    return False
