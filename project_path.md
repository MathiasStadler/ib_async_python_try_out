# i'm following this [vid](https://www.youtube.com/watch?v=ZyhVh-qRZPA)

## path step by step for this project

## I miss this information in so many projects

## date to start this project

```bash
date
Tue Apr  8 03:28:36 PM CEST 2025
```

```date
timedatectl

Local time: Tue 2025-04-08 15:29:20 CEST
Universal time: Tue 2025-04-08 13:29:20 UTC
RTC time: Tue 2025-04-08 13:29:20
Time zone: Europe/Berlin (CEST, +0200)
System clock synchronized: yes
NTP service: active
RTC in local TZ: no
```

## init github repo via vscode first

[repo](https://github.com/MathiasStadler/ib_async_python_try_out)

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

## install ib_async

```bash
pip install ib_async

pip3 install ibapi
```

## [ib_async](https://github.com/ib-api-reloaded/ib_async) package installs the following package automatically

```bash
(.venv) trapapa@debian:~/ib_async_python_try_out$ pip list
Package      Version
------------ -------
eventkit     1.0.3
ib_async     1.0.3
nest-asyncio 1.6.0
numpy        2.2.4
pip          23.0.1
setuptools   66.1.1
```

## install python_pandas inside .env

```bash
pip install pandas
```

## select the .env python kernel

# follow up inside the notebook