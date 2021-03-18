from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("1BVtsOK0Bu4mERJs2VqCsyawjPo-t0b2Iuri-ly95PdxMoU7LQNjGSYXyv7yr83VSf2vTmE7T6YzzVeVGzmpAnM5WctTb3L1q3AKtktLhhXqfRVkVq3noyKiL5jMNB27sv2mV_YmhlVShtO2dTAeTRSAvem8G5wYQgAimswVOIUa7jXsaE87tzQkt3p6KawM0q37b-2h41r9hi7H_2TNHzpoLt6U7dCGIhdjrTdzzUrucX8x2j0dsKH_THvlsCWRKzsvyOEiU21qJ6d9daol_7PqQ1zvQBV_B4nRGa6J3xXtJZQMaG34im34sopKD0rVmvOAZk1PZW9-BIcV7AV04OMq3rFvrnUU=", "session")
BOT_TOKEN = getenv("1781912435:AAFPy9aWmUySA7b_b9XOgj2MrxoApryk5bM")

API_ID = int(getenv("3337619")
API_HASH = getenv("e5fc2bd9e8f028e4d67694694d2612f7")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("1372501389").split()))
