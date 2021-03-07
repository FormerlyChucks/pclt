import argparse, downsyndrome, json, pprint

parser = argparse.ArgumentParser()

def rf():
    parser.add_argument('-f', '--file', help="File to delete", required=True)
    args = parser.parse_args()
    os.remove(args.file)

def pp():
    parser.add_argument('-f', '--file', help="File to print", required=True)
    args = parser.parse_args()
    pprint.pprint(json.loads(open(args.file, 'r').read()))

def dl():
    parser.add_argument('-u', '--url', help="URL To Download", required=True)
    parser.add_argument('-n', '--name', help="Name Of File", required=True)
    args = parser.parse_args()
    downsyndrome.download(url=args.url,file_name=args.name)
