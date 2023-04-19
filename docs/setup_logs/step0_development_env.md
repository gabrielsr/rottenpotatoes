

== Requirements ===


Python
Poetry
git


# Init Repo

Got a .gitignore, initalized the repo and realized the first commit 

'''
wget https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore
git init
git add --all
git commit -m "initial commit"
''' 

== Setup tests


Included pytest as a dependency

'''
[tool.poetry.group.test]  # This part can be left out

[tool.poetry.group.test.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"
''' 


== Initial Dev Setup

'''
poetry install
'''

== Activate Env (For each new terminal session)

'''
poetry shell
'''' 



== Run tests

created a test_test.py file and running pytest with:

'''
poetry run pytest
'''' 


== VSCode
Installed Extensions:
- Better TOML
