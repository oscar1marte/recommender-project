#!/bin/bash

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "requirements.txt not found. Creating a new one with default packages."
    # Create a requirements.txt with default packages
    echo -e "cumulusci\nsnowfakery" > requirements.txt
else
    echo "requirements.txt found. Adding CumulusCI and Snowfakery."
    # Add CumulusCI and Snowfakery to requirements.txt if not already present
    if ! grep -q "cumulusci" requirements.txt; then
        echo "cumulusci" >> requirements.txt
    fi
    if ! grep -q "snowfakery" requirements.txt; then
        echo "snowfakery" >> requirements.txt
    fi
fi

# Install required packages
pip install -r requirements.txt

# Confirm successful setup
echo "Python environment setup is complete with CumulusCI and Snowfakery installed."
