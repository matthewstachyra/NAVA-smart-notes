`|\| /\ \/ /\`

smart notetaking

v0.1.0


# NAVA (Not Another Virtual Assistant)

## Getting started.
1. Run `pipenv shell` to create a virtual environment. 
2. Run `pipenv install` to install all dependencies from the Pipfile.

Note: rather than running `python run <some_py_file>`, all commands will be preceded by `pipenv run` so that the equivalent functional command is `pipenv run python <some_py_file>`

## Running the command line app.
1. Change directory to /src with `cd src`.
2. Run `pipenv run python -m cli <args>`. Available arguments are:
  - `-a` or `--add` to add a note to the database - e.g., `-a "note"`
  - `-s` or `--search` to search and return related notes to the note - e.g., `-s "search_term_1 search_term_2"`
