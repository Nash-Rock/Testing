import time
import subprocess
import random

def flash_cmd_prompt(count=1):
    while count > 0:
        subprocess.Popen('cmd.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)
        time.sleep(random.uniform(0.01, 0.03))
        count -= 1

flash_cmd_prompt(100)

Website used https://aidark.net
