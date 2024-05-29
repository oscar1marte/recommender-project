#!/bin/bash

# Check if the current directory is a Git repository, if not, initialize it
if [ ! -d .git ]; then
    git init
    echo "Initialized a new Git repository."
    # Set default configurations to avoid interactive prompts
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
else
    echo "Git repository already initialized."
fi

# Initialize a CumulusCI project if not already initialized
if [ ! -f cumulusci.yml ]; then
    cci project init
    echo "CumulusCI project initialized."
else
    echo "CumulusCI project already initialized."
fi

# Connect to the Salesforce org named "oscarhub"
cci org connect devhub

# Verify the connection
cci org info devhub
