#!/bin/bash

# Define the source and destination paths
SOURCE_FILE_1="scripts/synthetic.recipe.yaml"
SOURCE_FILE_2="scripts/synthetic.recipe.only_account.yaml"

DEST_DIR="datasets"

DEST_FILE_1="${DEST_DIR}/synthetic.recipe.yaml"
DEST_FILE_2="${DEST_DIR}/synthetic.recipe.only_account.yaml"

# Check for the required arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <recipe_number> <repeat_count>"
    echo "recipe_number: 1 for synthetic.recipe.yaml, 2 for synthetic.recipe.only_account.yaml"
    echo "repeat_count: Number of times to repeat the recipe"
    exit 1
fi

# Assign the arguments to variables
RECIPE_NUMBER=$1
REPEAT_COUNT=$2

# Determine the source and destination file based on the recipe number
if [ "$RECIPE_NUMBER" -eq 1 ]; then
    SOURCE_FILE=$SOURCE_FILE_1
    DEST_FILE=$DEST_FILE_1
elif [ "$RECIPE_NUMBER" -eq 2 ]; then
    SOURCE_FILE=$SOURCE_FILE_2
    DEST_FILE=$DEST_FILE_2
else
    echo "Invalid recipe number. Please enter 1 or 2."
    exit 1
fi

# Check if the source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Source file ${SOURCE_FILE} does not exist in the root directory."
    exit 1
fi

# Create the destination directory if it doesn't exist
if [ ! -d "$DEST_DIR" ]; then
    mkdir -p "$DEST_DIR"
fi

# Move the source file to the destination directory, replacing any existing file
cp -f "$SOURCE_FILE" "$DEST_FILE"

# Confirm the file move
if [ -f "$DEST_FILE" ]; then
    echo "Moved ${SOURCE_FILE} to ${DEST_FILE}."
else
    echo "Failed to move ${SOURCE_FILE} to ${DEST_FILE}."
    exit 1
fi

# Run the specified CumulusCI task with the specified repetition count
cci task run snowfakery --recipe "$DEST_FILE" --org devhub --run-until-recipe-repeated "$REPEAT_COUNT"
