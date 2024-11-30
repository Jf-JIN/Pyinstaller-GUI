
import os
import sys
from system.AnalogDefine import AnalogDefine

os.chdir(os.path.dirname(os.path.dirname(__file__)))
if len(sys.argv) > 1:
    APP_WORKSPACE_PATH = sys.argv[1]
else:
    APP_WORKSPACE_PATH = os.getcwd()


class EnumConst(AnalogDefine):
    DEFAULT_INSTALLER_COMMANDLINE = '--onefile --console --clean'
