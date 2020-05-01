import str_arg_parser

def is_unique_char_string(str):
    if len(str) > 256:
        return False
    s = set()
    for item in str:
        print(item)
        if item not in s:
            s.add(item)
        else:
            return False
    return True

parser = str_arg_parser.init_argparse()
args = parser.parse_args()
if len(args.s) > 1:
    parser.error("-s appears several times.")
if is_unique_char_string(args.s[0]):
    print("The characters in the string are not unique")
else:
    print("The characters in the string are not unique")
