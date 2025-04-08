# Project Template (based on cookiecutter format)

This is a template repo, which is intended to help easily and quickly init a new project.

To use this template, please follow these steps:

- Install cookiecutter

```bash
pip install cookiecutter
```

- Init new project using this template

```bash
# Clone from project template
cookiecutter https://github.com/lenghia100703/Project-Template/
# or by using ssh config name
cookiecutter git+ssh://ssh_config_name/lenghia100703/Project-Template
# or

cookiecutter git@github.com:lenghia100703/Project-Template.git

# Change the current working directory to the new project directory
cd <PROJECT_DIRECTORY>
# Init bare git repo
git init --bare
# Add the server's repo as origin
git remote add origin <YOUR_REPO_URL>
```
