import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--surname', type=str, required=True)
parser.add_argument('--middle_name', type=str, default=None)
parser.add_argument('--age', type=int, required=True)
parser.add_argument('--sex', type=str, choices=['M', 'F'], required=True)
parser.add_argument('--married', type=bool, nargs='?', const=True, default=False)
parser.add_argument('--hobbies', type=str, nargs='+', default=None)
args = parser.parse_args()

with open('journal.txt', 'a') as f:
    json.dump(args.__dict__, f, ensure_ascii=False)
    f.write('\n')
