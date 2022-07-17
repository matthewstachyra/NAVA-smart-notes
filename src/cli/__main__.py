'''
Entrypoint module.

Call using 'pipenv run python -m cli' from the parent directory 'src'.
'''
from .cli import main

if __name__ == "__main__":
    main()
