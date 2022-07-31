# tidyfol

tidyfol is a command-line tool that tides your folder with simple command.

## Installation Guide

### **TO BE UPDATED**

## Development Environment Setup

Clone the repository to local machine

    git clone https://github.com/yimin-z/tidyfol.git
    cd tidyfol

Set up a virtual environment

    python3 -m venv .venv

Activate the virtual environment

    source .venv/bin/activate

Install the dependencies

    python3 -m pip install -r requirements.txt

To install the app in development mode

    pip install -e .

Now, you can run the app

    tidyfol --version

You can uninstall the app with

    pip uninstall tidyfol

To deactivate the virtual environment

    deactivate

## Packaging the APP

Run the following command

    python -m build

The packages should appear in `tidyfol/dist`
