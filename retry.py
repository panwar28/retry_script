#!/usr/bin/python
# Author: Umesh Panwar
# Date: May-30, 2024
import os
import time

MAX_ATTEMPTS = 3
SLEEP_TIME = 30

def terraform_apply(attempt=1):
    if attempt > MAX_ATTEMPTS:
        print(f'Terraform apply failed {MAX_ATTEMPTS} times, exiting')
        return
    cmd = "terraform apply -auto-approve"
    returned_value = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value)
    if returned_value == 0:
        print('Terraform apply success')
    else:
        print('Terraform apply failed, trying again')
        time.sleep(SLEEP_TIME)
        terraform_apply(attempt + 1)

def terraform_destroy(attempt=1):
    if attempt > MAX_ATTEMPTS:
        print(f'Terraform destroy failed {MAX_ATTEMPTS} times, exiting')
        return
    cmd = "terraform destroy -auto-approve"
    returned_value = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value)
    if returned_value == 0:
        print('Terraform destroy success')
    else:
        print('Terraform destroy failed, trying again')
        time.sleep(SLEEP_TIME)
        terraform_destroy(attempt + 1)

def terraform_init():
    cmd = "terraform init"
    returned_value = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value)
    if returned_value == 0:
        print('Terraform init success')
    else:
        print('Terraform init failed, please check and address the issue')

if __name__ == "__main__":
    terraform_init()
    terraform_apply(attempt=1)
    #terraform_destroy(attempt=1)