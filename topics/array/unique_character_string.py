#import str_arg_parser

def is_unique_char_string(str):
    if len(str) > 256:
        return False
    s = set()
    for item in str:
        if item not in s:
            s.add(item)
        else:
            return False
    return True

