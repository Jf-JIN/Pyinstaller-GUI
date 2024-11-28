import os
import sys

os.chdir(os.path.dirname(os.path.dirname(__file__)))
if len(sys.argv) > 1:
    APP_WORKSPACE_PATH = sys.argv[1]
else:
    APP_WORKSPACE_PATH = os.getcwd()
