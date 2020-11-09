# assume that this is a .py script
import sys
import os

def tenet(input_file_path: str, output_file_path: str) -> None:
    if os.path.isdir(input_file_path): 
        raise ValueError('Input file path is directory. Can not open.')
    if input_file_path == output_file_path:
        raise ValueError('Input file path is output file path.')
    
    output_file = open(output_file_path, 'w')
    
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            if line[-1] == '\n':
                output_file.write(line[::-1][1:]+ '\n')
            else:
                output_file.write(line[::-1])

def tenet_cmd():
    input_file_path = str(sys.argv[1])
    output_file_path = str(sys.argv[2])
    tenet(input_file_path, output_file_path)

if __name__ == '__main__':
    tenet_cmd()
