import argparse

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="input string"
    )
    parser.add_argument(
        "-s", action='append',
    )
    return parser
