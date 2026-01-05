from flask import Flask, render_template, url_for
from datetime import datetime, date
import json

app = Flask(__name__)

with open('experiences_data.json', 'r', encoding='utf-8') as f:
    all_experiences = json.load(f)

with open('interests_data.json', 'r', encoding='utf-8') as f:
    all_interests = json.load(f)

@app.route('/')
def home():
    return render_template(
        "index.html", current_year=datetime.now().year,
        experiences=all_experiences
    )

@app.route('/sobremim')
def aboutme():
    birthdate = date(2004, 7, 12)
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return render_template("aboutme.html", current_year=datetime.now().year, age=age, interests=all_interests)

@app.route("/experience/<category>/<name>")
def experience(category, name):
    category_dict = all_experiences.get(category)
    
    if category_dict:
        projects_dict = category_dict.get("projects", {})
        experience_data = projects_dict.get(name)
    else:
        experience_data = None

    if not experience_data:
        return "Experiência não encontrada", 404
    
    return render_template(
        "experience.html", 
        current_year=datetime.now().year, 
        experience=experience_data
    )


if __name__ == "__main__":
    app.run(debug=True)