import time
import crypto_utils
from consts import SECRET, FIVE_MIN_IN_SEC
from TamperError import TamperError


#building an hmac payload for every cell in the matrix
def save_secure(cell_val):

    cell_val = str(cell_val)
    payload = {}
    payload["text"] = cell_val
    payload["val"] = (crypto_utils.hmac_sign(SECRET, cell_val.encode("utf-8")))
    timestamp = int(time.time())
    payload["timestamp"] = timestamp

    return payload


#checking the cell value and timestmap

def load_secure(payload, check_string):

    val = payload["val"]
    timestamp = payload["timestamp"]
    timestamp_now = int(time.time())
    if timestamp + FIVE_MIN_IN_SEC < timestamp_now:
        raise TamperError("This is to late, the time stamp is too late!")
    else:
        if crypto_utils.hmac_verify(SECRET, val, check_string) == False:
            raise TamperError("The value is not the same!")

    return True



#returns the defective indexes
def verify_file(matrix):
    defective_index = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            try:
                load_secure(matrix[i][j], matrix[i][j]["text"])
            except TamperError:
                defective_index.append((i, j))

    return defective_index

