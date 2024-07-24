import json
import random
from discord.app_commands import Choice

file_path = 'utils/projects.json'
data = {}

with open(file_path, 'r') as file:
    data = json.load(file)


def select_random_project(exclude_ids, category: Choice, difficulty: Choice):
    if exclude_ids:
        if isinstance(exclude_ids, int):
            exclude_ids = [exclude_ids]
        filtered_projects = [project for project in data['projects'] if project['project_id'] not in exclude_ids]
    else:
        filtered_projects = data['projects']

    if category is not None:
        filtered_projects = [project for project in filtered_projects if project["category"] == category.name]

    if difficulty is not None:
        filtered_projects = [project for project in filtered_projects if project["difficulty"] == difficulty.name]

    if not filtered_projects:
        return None

    return random.choice(filtered_projects)


def get_categories_as_choices():
    choices = []

    for index, category in enumerate(data.get("categories", {})):
        name = category
        value = index
        choices.append(Choice(name=name, value=value))
    return choices

def get_difficultries_as_choices():
    choices = []

    for index, category in enumerate(data.get("difficulties", {})):
        name = category
        value = index
        choices.append(Choice(name=name, value=value))
    return choices