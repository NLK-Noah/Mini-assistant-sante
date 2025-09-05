from assistant.loader import charger_questionnaire
from assistant.evaluator import evaluer_condition
def dialogue():
    data = charger_questionnaire("data/questions.json")
    if isinstance(data, dict) and "questions" in data:
        questions = data["questions"]
    else:
        questions = data
    print("Bienvenue dans ton assistant santé ! 🌱")
    for q in questions:
        reponse = input(q["question"] + " ")

        try:
            valeur = float(reponse)
        except ValueError:
            print("❌ Réponse invalide, on passe à la suivante.")
            continue

        for r in q["recomendations"]:
            if evaluer_condition(valeur, r["condition"]):
                print("💡 Recommandation :", r["reponse"])
                break
    print("Merci d'avoir utilisé l'assistant santé ! Prenez soin de vous ! 🌟")