import hashlib
import hashlib as h
import hmac




def hash256_hex(text):
    return h.sha256(text.encode("utf-8")).hexdigest()

def hmac_sign(key, msg):
    key = key.encode("utf-8")
    msg = msg.encode("utf-8")
    return hmac.new(key, msg, h.sha256).hexdigest()

def hmac_verify(key, msg, check_string):
    key = key.encode("utf-8")
    msg = msg.encode("utf-8")

    ch = hmac.new(key, msg, h.sha256).hexdigest()
    return hmac.compare_digest(ch, check_string)



