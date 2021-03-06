# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}


This template will help you scaffold a new machine learning project using
[https://github.com/georgepar/slp](https://github.com/georgepar/slp), PyTorch and PyTorch
Lightning.


Run

```
pip install poetry
poetry install
```

to create a new venv with your dependencies and

```
poetry shell
```

to activate the environment.


Model logs and checkpoints will be saved in `experiments` folder and stdout logfiles in `logs`.

Implement TODOs in `main.py` and python files under `{{cookiecutter.project_name}}`


Run

```
python main.py --help
```

to see available configuration options


Run

```
python main.py --config config/config.yaml --debug
```

to run in debug mode


Run

```
python main.py --config config/config.yaml  # You can override config file values with command line args
```

to train and test your model
