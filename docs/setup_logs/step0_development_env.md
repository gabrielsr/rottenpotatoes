

== Requirements ===


Python
Poetry
git




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
