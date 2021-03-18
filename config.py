from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("BQA3OsGnVH6nOOVWCYVaCJY9VoHbNw1ufOkXKBXqNsjSDYI_py5Vdi63Q2VFE1CqdDRGKPkygEIvVM_QU4biwKbLDLAM6U-ZR0sEh5dKo_-ibnTzzoTKsgtf16BlvYNLlkf6BSx_C2ruGdcgXmauo5aAS8J636A8iQ0ezK1jYSZA_vLC8-vBc4sEfg0gyMl6_EtuCR7yGd0Wb6e2T_X7l1KEYC2VRCBABwK_6gkEYjN_M3jcPcUhynpC3_No0Vt6AA06_Itgw43et8BQkyhNIxeKeLtpF4V1K3FhK2F0r6UiCFZsbDj47TEWCRVl5z_vfV1_IxeHWdH7UtgVueEVWZydUc61jQA", "session")
BOT_TOKEN = getenv("1781912435:AAFPy9aWmUySA7b_b9XOgj2MrxoApryk5bM")

API_ID = getenv("3337619")
API_HASH = getenv("e5fc2bd9e8f028e4d67694694d2612f7")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(getenv("1372501389").split()))
