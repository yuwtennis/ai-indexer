import logging

from aiindexer.app import run

def main():
    logging.basicConfig(level=logging.INFO)
    run()

if __name__ == "__main__":
    main()