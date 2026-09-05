# Python Virtual Environment Setup

This project uses a dedicated local Python virtual environment to isolate project dependencies and prevent conflicts with the system-wide Python installation.

Below are the steps to set up Python virtual environment for this project:

1) Navigate to [setup](../../common/setup/) folder. The main script is [py_setup.py](../../common/setup/py_setup.py)

2) Once navigate to the folder mentioned, run the following command to set up the virtual environment:

    ```shell
    python3 py_setup.py
    ```

3) Once completed, you will see the following created in the [project main folder](../../):
    
    - `venv.txt`
    - `pyenv/`

**NOTE:**

- You may rerun the command in Step 2 whenever new dependencies are added to [requirements.txt](../../requirements.txt)

- Run one of the following commands to force rebuild the virtual environment (e.g. after upgrading or switching to a different Python 3 version)
    
    ```shell
    # Option 1
    python3 py_setup.py -f

    # Option 2
    python3 py_setup.py --force

    # Option 1 and 2 are exactly the same to force rebuild virtual environment
    ```