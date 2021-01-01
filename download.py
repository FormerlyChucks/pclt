import argparse, requests, traceback

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help="URL To Download", required=True)
parser.add_argument('-n', '--name', help="Name Of File", required=True)
parser.add_argument('-a', '--agent', help="User Agent", required=False)
args = parser.parse_args()

url = args.url
name = args.name
agent = args.agent

def download():   
    if agent is None:
        try:
            response = requests.get(url)
            file = open(name, "wb")
            file.write(response.content)
            file.close()
            print('Downloaded {0} as {1}'.format(url,name))
        except Exception:
            print(traceback.format_exc())
            quit()
    else:
        try:
            response = requests.get(url, headers = {'User-agent': '{}'.format(agent)})
            file = open(name, "wb")
            file.write(response.content)
            file.close()
            print('Downloaded {0} as {1}'.format(url,name))
        except Exception:
            print(traceback.format_exc())
            quit()