from utils.byte import varint, reverse, b2a
from utils.log import log_print


def parse_inv(s):
    length_inv, bytes_read = varint(s[20:])

    for i in range(length_inv):
        inv = s[20 + bytes_read + 36*i: 20 + bytes_read + 36*(i+1)]

        inv_type = inv[:4].rstrip(b'\00')
        if inv_type == b'\x01':
            inv_type = 'MSG_TX'
        elif inv_type == b'\x02':
            inv_type = 'MSG_BLOCK'
        elif inv_type == b'\x03':
            inv_type = 'MSG_FILTERED_BLOCK'
        elif inv_type == b'\x04':
            inv_type = 'MSG_CMPCT_BLOCK'
        else:
            inv_type = 'ERROR'

        inv_content = reverse(inv[4:])
        log_print('inv #%i' % (i+1), "%s -> %s" % (inv_type, inv_content))

    return b2a(s[20:])
