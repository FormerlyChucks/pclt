import argparse, downsyndrome

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help="URL To Download", required=True)
parser.add_argument('-n', '--name', help="Name Of File", required=True)
args = parser.parse_args()

def download():   
    downsyndrome.download(url=args.url,file_name=args.name)
