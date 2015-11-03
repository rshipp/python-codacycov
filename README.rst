python-codacy-coverage
======================

Credits to Ryan for creating this! Python coverage reporter for Codacy https://www.codacy.com

[![Codacy Badge](https://api.codacy.com/project/badge/grade/3a8cf06a9db94d0ab3d55e0357bc8f9d)](https://www.codacy.com/app/Codacy/python-codacy-coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/coverage/3a8cf06a9db94d0ab3d55e0357bc8f9d)](https://www.codacy.com/app/Codacy/python-codacy-coverage)
[![Circle CI](https://circleci.com/gh/codacy/python-codacy-coverage.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/codacy/python-codacy-coverage)
[![PyPI version](https://badge.fury.io/py/codacy-coverage.svg)](https://badge.fury.io/py/codacy-coverage)

Setup
-----

Codacy assumes that coverage is previously configured for your project.

To generate the required coverage XML file, calculate coverage for your project as normal, by running:

``coverage xml``

Install codacy-coverage
~~~~~~~~~~~~~~~~~~~~~~~

You can install the coverage reporter by running:

``pip install codacy-coverage``

Updating Codacy
---------------

To update Codacy, you will need your project API token. You can find the token in Project -> Settings -> Integrations -> Project API.

Then set it in your terminal, replacing %Project_Token% with your own token:

``export CODACY_PROJECT_TOKEN=%Project_Token%``

Next, simply run the Codacy reporter. It will find the current commit and send all details to your project dashboard:

``python-codacy-coverage -r coverage.xml``
