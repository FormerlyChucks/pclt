import argparse, traceback, pprint, json

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="file to print", required=True)
args = parser.parse_args()

def pprint():
    with open(args.file, 'r') as f:
        pprint.pprint(json.loads(f.read()))
