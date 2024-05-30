# Retry Deployment Script

This repository contains a Python script designed to handle transient errors during cloud deployment. These errors often resolve themselves upon retrying the deployment, and this script automates that process.

## Overview

During cloud deployment, you may encounter transient errors that can be resolved simply by retrying the deployment. This script was developed to automate the retry process, reducing manual intervention and increasing the success rate of deployments.

## Features

- **Automated Retries**: The script automatically retries the deployment in case of failure.
- **Customizable Parameters**: You can customize the number of attempts and the sleep timer between each attempt.
- **Versatility**: Initially used for retrying terraform deployments, this script can be adapted to retry any deployment script with minor modifications.

## Usage

1. Update the deployment command in the script.
2. Set the number of attempts and sleep timer as per your requirements.
3. Run the script.

## Contribution

Feel free to fork this repository and make changes to suit your needs. Pull requests for improvements and new features are always welcome.

## Disclaimer

This script is provided as-is, and while it has been designed to handle most transient errors, there may be some scenarios where manual intervention is required.

## License

This project is licensed under the MIT License - see the LICENSE file for details.