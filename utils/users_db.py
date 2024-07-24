import sqlite3
import json

con = sqlite3.connect("utils/users.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, viewed_projects TEXT)")
con.commit()


def add_user_viewed_projects(user_id, new_project_ids):
    if isinstance(new_project_ids, int):
        new_project_ids = [new_project_ids]
    elif not isinstance(new_project_ids, list):
        raise ValueError("new_project_ids must be an int or a list")

    cur.execute('''
            SELECT viewed_projects FROM users
            WHERE user_id = ?
            ''', (user_id,))
    result = cur.fetchone()

    if result and result[0]:
        try:
            current_projects = json.loads(result[0])
            if not isinstance(current_projects, list):
                current_projects = []
        except json.JSONDecodeError:
            current_projects = []
    else:
        current_projects = []

    updated_projects = list(set(current_projects + new_project_ids))

    updated_projects_json = json.dumps(updated_projects)

    cur.execute('''
            INSERT INTO users (user_id, viewed_projects)
            VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET viewed_projects=excluded.viewed_projects
            ''', (user_id, updated_projects_json))
    con.commit()


def get_user_viewed_projects(user_id):
    cur.execute("SELECT viewed_projects FROM users WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    if result:
        return json.loads(result[0])
    else:
        return None


def clear_user_viewed_projects(user_id):
    empty_projects_json = json.dumps([])
    cur.execute("UPDATE users SET viewed_projects = ? WHERE user_id = ?", (empty_projects_json, user_id))
    con.commit()