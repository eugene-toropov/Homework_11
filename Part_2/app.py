import utils
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    candidates = utils.load_candidates_from_json()
    return render_template("list.html", items=candidates)


@app.route("/candidates/<int:id>")
def candidate_by_id(id):
    candidate = utils.get_candidate_by_id(id)
    name = candidate["name"]
    position = candidate["position"]
    img = candidate["picture"]
    skills = candidate["skills"]
    return render_template("single.html", name=name, position=position, img=img, skills=skills)


@app.route("/search/<candidate_name>")
def candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    lenght = len(candidates)
    return render_template("search.html", items=candidates, lenght=lenght)

@app.route("/skill/<skill_name>")
def candidates_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    lenght = len(candidates)
    skill = skill_name
    return render_template("skill.html", items=candidates, lenght=lenght, skill=skill)


app.run()
