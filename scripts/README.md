# 📘 Salesforce Generator Scripts

This repository contains scripts and configuration files for setting up a Python environment, initializing connections, and generating synthetic data using Snowfakery. Below is a detailed guide to understand and use each part of the project.

## 📂 Project Structure

- `scripts/`
  - `1_setup_environment.sh` 📄
  - `2_init_and_connect.sh` 📄
  - `3_run_snowfakery.sh` 📄
  - `synthetic.recipe.yaml` 📄
  - `synthetic.recipe.new_data.yaml` 📄

## 📜 File Descriptions

### 1. `1_setup_environment.sh` 🚀

This script sets up the Python environment with necessary packages:
1. Checks for the existence of `requirements.txt`.
2. Adds necessary packages (`cumulusci` and `snowfakery`) if they are not already present.
3. Installs the required packages.
4. Confirms the successful setup.

### 2. `2_init_and_connect.sh` 🌐

This script initializes a Git repository and a CumulusCI project, then connects to a Salesforce org:
1. Checks if the directory is a Git repository; if not, initializes one.
2. Configures Git user details.
3. Initializes a CumulusCI project if not already initialized.
4. Connects to the Salesforce org named "oscarhub".
5. Verifies the connection.

### 3. `3_run_snowfakery.sh` ❄️

This script runs Snowfakery to generate synthetic data:
1. Defines source and destination paths.
2. Checks for the required arguments (`recipe_number` and `repeat_count`).
3. Assigns the arguments to variables.
4. Validates the source file existence.
5. Creates the destination directory if it doesn't exist.
6. Moves the source file to the destination directory.
7. Runs the Snowfakery task with the specified repetition count.

### 4. `synthetic.recipe.yaml` and `synthetic.recipe.only_account.yaml` 📑

These files contain recipes for generating synthetic data using Snowfakery:
- Define variables for business data.
- Specify the structure and fields for `Account` and `Opportunity` objects.

## ⚙️ Usage Instructions

1. **Setup Environment**:
   Run `1_setup_environment.sh` to set up the Python environment.
   ```bash
   ./1_setup_environment.sh
   ```

2. **Initialize and Connect**:
   Run `2_init_and_connect.sh` to initialize Git and CumulusCI, and connect to Salesforce.
   ```bash
   ./2_init_and_connect.sh
   ```

3. **Generate Synthetic Data**:
   Run `3_run_snowfakery.sh` with appropriate arguments to generate synthetic data.
   ```bash
   ./3_run_snowfakery.sh <recipe_number> <repeat_count>
   ```

## 📝 Notes

- Ensure you have the necessary permissions and configurations for connecting to the Salesforce org.
- Modify the Git user details in `2_init_and_connect.sh` as needed.
- Update the synthetic data recipes as per your requirements.
