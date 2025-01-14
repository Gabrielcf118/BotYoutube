"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    bot.browse("https://www.youtube.com/")

    # Implement here your logic...
    if not bot.find( "image", matching=0.97, waiting_time=10000):
        not_found("image")
    bot.click()
    if not bot.find( "configurações", matching=0.97, waiting_time=10000):
        not_found("configurações")
    bot.click()
    if not bot.find( "notificações", matching=0.97, waiting_time=10000):
        not_found("notificações")
    bot.click()
    if not bot.find( "notificcações2", matching=0.97, waiting_time=10000):
        not_found("notificcações2")
    bot.double_click_relative(-58, 14)
    
    bot.control_c()
    copiado = bot.get_clipboard()
    print(f"O que foi copiado: {copiado}")
    
    
    

    
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()