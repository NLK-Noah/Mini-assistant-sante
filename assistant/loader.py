import json
def charger_questionnaire(fichier_json):
    with open(fichier_json, 'r', encoding='utf-8') as f:
        questionnaire = json.load(f)
    return questionnaire