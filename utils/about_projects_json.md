# About projects.json

## What's projects.json?
It's a json file(surprisingly) which stores info about projects, this info which is shown to user when they execute the command.

## How projects.json structure should look like?

```json
{
    "format_version": 1,
    "categories": [
        "Category 1"
    ],
    "difficulties": [
        "Difficulty 1",
        "Difficulty 2"
    ],
    "projects": [
        {
            "project_id": 1,
            "project_name": "Project 1",
            "project_desc": "Sample",
            "category": "Category 1",
            "difficulty": "Difficulty 1"
        },
        {
            "project_id": 2,
            "project_name": "Project 2",
            "project_desc": "Sample",
            "category": "Category 1",
            "difficulty": "Difficulty 2"
        }
    ]
}
```
## What is "format_version" used for?
Currently, for nothing but the number will be increased(by one) if I'll need to improve the format, change/improve it.

## What are "categories" and "difficulties" lists used for?
For choices when users trying to run the command with category/difficulty argument. Also used by my app for editing projects.json.

#### [Important] Even if project you added have category/difficulty not inside of categories/difficulties users will still be able to get it when they just run the command without any arguments.

## Does project ids should start from 1 and go +1 with each next project in the file?
No, they can be any integers.

#### [Important] Keep in mind that the bot stores which projects a user saw(so that users don't see same project again until they clear their watch history) by those ids, if several projects will have the same id when the user see one of the projects with this id they won't be able get the other one(until they'll clear their watch history).

## What do I need to edit projects.json/add my projects to it/edit default projects?
You can edit projects.json in any text editor or via my buggy app.
