# python-coverage-coverage
[![Build Status](https://circleci.com/gh/codacy/python-codacy-coverage.png?style=shield&circle-token=:circle-token)](https://circleci.com/gh/codacy/python-codacy-coverage)
[![Codacy Badge](https://www.codacy.com/project/badge/1c524e61cd8640e79b80d406eda8754b)](https://www.codacy.com/app/Codacy/python-codacy-coverage-)

Python coverage reporter for Codacy https://www.codacy.com

## Setup

Codacy assumes that coverage is previously configured for your project.

You can install the coverage reporter by running:

### [Install jpm](https://www.jpm4j.org/#!/md/install)
```
curl http://www.jpm4j.org/install/script | sh
```

### Install codacy-coverage-reporter
```
jpm install com.codacy:codacy-coverage-reporter
```

## Updating Codacy

To update Codacy, you will need your project API token. You can find the token in Project -> Settings -> Integrations -> Project API.

Then set it in your terminal, replacing %Project_Token% with your own token:

```
export CODACY_PROJECT_TOKEN=%Project_Token%
```

Next, simply run the Codacy reporter. It will find the current commit and send all details to your project dashboard:

```
python-codacy-coverage -f coverage.xml
```
