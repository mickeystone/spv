from binascii import b2a_hex
from utils.log import log_print
from utils.byte import reverse

def parse_sendcmpct(s):
    message = s[20:]

    is_cmpctblock = bool(message[0])
    cmpct_number = int(reverse(message[1:]), 16)

    if is_cmpctblock and cmpct_number == 1:
        log_print("cmpctblock", 'Announce new blocks with cmpctblock message')
    elif cmpct_number == 2:
        log_print("cmpctblock", "SegWit active")
    else:
        log_print("cmpctblock", "Announce new blocks with inv/header messages")