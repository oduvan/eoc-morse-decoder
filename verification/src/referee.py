from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "morse_decoder"
    FUNCTION_NAMES = {
        "python_3": "morse_decoder",
        "js_node": "morseDecoder"
    }
    ENV_COVERCODE = {
        
    }