import json

def load_candidates_from_json():
    with open("candidates.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_candidate_by_id(id):
    for candidate in load_candidates_from_json():
        if id == candidate["id"]:
            return candidate
    return


def get_candidates_by_name(name):
    candidates_with_name=[]
    for candidate in load_candidates_from_json():
        if name.lower() in candidate["name"].lower():
            candidates_with_name.append(candidate)
    return candidates_with_name


def get_candidates_by_skill(skill):
    candidates_with_skill = []
    for candidate in load_candidates_from_json():
        if skill.lower() in candidate["skills"].lower().split(", "):
            candidates_with_skill.append(candidate)
    return candidates_with_skill



