import os

STRING1 = "A STRING ONE"
STRING2 = "TWO DUCKS WALK INTO A BAR"
PARAM_VAL1 = 5
PARAM_VAL2 = 6
DATA_FILE_NAME_1 = 'datafile1.txt'
RESULT1 = 'FOO'
RESULT2 = 'BAR'
RESULT3 = 'BAZ'
RESULT4 = 'BIF'
RESULT5 = 'DUCK'


def create_data_file(filename, content):
    with open(filename, 'w') as  fileToCreate:
        fileToCreate.write(content)


def read_data_file(filename):
    with open(filename, 'r') as  fileToRead:
        content = fileToRead.readlines()
    return content


def destroy_data_file(filename):
    os.remove(filename)


_call_count = 0


def reset():
    global _call_count
    _call_count = 0


class MockGenerationProcess(object):
    def __init__(self):
        return

    @staticmethod
    def get_call_count():
        global _call_count
        return _call_count

    def __call__(self, key_param, param=None):

        if key_param == STRING1 and param is None:
            value = RESULT1
        elif key_param == STRING2 and param is None:
            value = RESULT2
        elif key_param == STRING1 and param == PARAM_VAL1:
            value = RESULT3
        elif key_param == STRING2 and param == PARAM_VAL1:
            value = RESULT4
        elif key_param == STRING2 and param == PARAM_VAL2:
            value = RESULT5
        else:
            raise Exception('Invalid key_param to MockGenerationProcess functor ' + str(key_param))
        global _call_count

        _call_count += 1

        return value
