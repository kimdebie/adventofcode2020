import urllib

def read_file(fp):

    with open(fp, 'r') as f:
        lines = f.read().splitlines()

        return lines