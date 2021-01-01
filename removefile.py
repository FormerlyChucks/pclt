import argparse, traceback

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="File to delete", required=True)
args = parser.parse_args()

def removefile():
    try:
        os.remove(args.file)
    except Exception:
        print(traceback.format_exc())
        quit()
