# i'm following this [vid](https://www.youtube.com/watch?v=ZyhVh-qRZPA)


# path step by step for this project

## init github repo via vscode first

## detect os version

```bash
cat /etc/debian_version
Debian 12.8 
```

## detect python version


```bash
python3 --version
Python 3.11.2
```

## create venv

[install venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

```bash
python3 -m venv .venv
```

## enter .venv

```bash
source .venv/bin/activate
```

## list installed packages

```bash
pip list
```

## exit/leave .venv

```bash
deactivate
```

## install python_pandas inside .env

```bash
pip install pandas
```

## select the .env python kernel

# follow up inside the notebook