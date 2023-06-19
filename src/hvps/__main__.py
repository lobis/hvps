from src.hvps import HVPS
from src.hvps.version import version

import argparse


def main():
    parser = argparse.ArgumentParser(description="HVPS control")
    parser.add_argument("--version", action="version", version=version)

    args = parser.parse_args()


if __name__ == "__main__":
    main()
