from cloud_convert import CloudConvert
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-f", "--file", help="filename")
args = parser.parse_args()


if __name__ == '__main__':
    CloudConvert(args.file).convert()
