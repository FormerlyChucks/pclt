import argparse

def rf():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="File to delete", required=True)
    args = parser.parse_args()
    os.remove(args.file)

def pp():
    import pprint, json
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="file to print", required=True)
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        pprint.pprint(json.loads(f.read()))

def dl():
    import downsyndrome
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help="URL To Download", required=True)
    parser.add_argument('-n', '--name', help="Name Of File", required=True)
    args = parser.parse_args()
    downsyndrome.download(url=args.url,file_name=args.name)
