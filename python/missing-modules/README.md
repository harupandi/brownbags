# Azure Function - Missing Modules

Linux Function App with missing module error. Objective is to find what is causing it.

## Installation

Clone locally to your machine.

```bash
git clone https://github.com/harupandi/brownbags.git
cd brownbags/python/missing-modules
```

Start the python virtual environment used by the Function and install requirements.txt dependencies.

```bash
.\/.venv/scripts/activate
pip install -r requirements.txt
```

Deploy to Azure Function App and test it https://<function app name>.azurewebsites.net/api/getUsers?id=1.