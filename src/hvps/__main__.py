from . import version, HVPS
import argparse


def main():
    parser = argparse.ArgumentParser(description="HVPS control")
    parser.add_argument("--version", action="version", version=version.__version__)

    args = parser.parse_args()


if __name__ == "__main__":
    main()
