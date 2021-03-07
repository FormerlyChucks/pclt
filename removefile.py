import argparse, traceback

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="File to delete", required=True)
args = parser.parse_args()

def removefile():
    os.remove(args.file)
