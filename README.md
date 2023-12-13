# chat
Python OpenAI ChatGPT API Example

How to use:
1. Rename the .env_example to .env and enter the OpenAI API Key to replace the XXXXX
2. At the command line, run 'python chat.py'


# Note on getting python to run from within VSCode (using the Run button)

**Symptoms**
Using the Windows command terminal, the chat.py program ran ok.
However, on running the chat.py program from within VSCode it reported an error as follows:
ModuleNotFoundError: No module named 'openai'

It seems that VSCode was running a different version of Python to the one I had installed.

**To diagnose**
1. I ran 'which python' from the command line and it reported 2 different versions on the system:
C:\Users\tommc\AppData\Local\Programs\Python\Python312\python.exe
C:\Users\tommc\AppData\Local\Microsoft\WindowsApps\python.exe

2. To see which interpreter was running from the command line, I opened the python interpreter and ran this program:
    import sys
    print(sys.executable)

Output was:
C:\Users\tommc\AppData\Local\Programs\Python\Python312\python.exe

This is the correct interpreter.

3. In VSCode I looked at which interpreter is running there. Ctrl-Shift-P for the command palette,
followed by 'Python Select Interpreter'. It reported the following path:
~\AppData\Local\Microsoft\WindowsApps\python.exe

This is the incorrect interpreter.

**The fix**
There are probably many solutions, but the easiest was to manually set the interpreter from within VSCode:

Open the command palette by clicking Shift-Ctrl-P
Type 'Python Select Interpreter'
Click on '+ Enter interpreter path...'
Set it to the interpreter that runs (correctly) from the command line: ~\AppData\Local\Programs\Python\Python312\python.exe
