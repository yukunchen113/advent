import os
from collections import defaultdict

def create_tree(commands):
    root = {}
    current = None
    com_idx = 0
    while com_idx<len(commands):
        command = commands[com_idx]
        if command.startswith("$ cd /"):
            current = root
        elif command.startswith("$ ls"):
            while com_idx+1 < len(commands) and not commands[com_idx+1].startswith("$"):
                lsdata = commands[com_idx+1].split()
                if lsdata[0] == "dir":
                    current[lsdata[1]] = {"..": current}
                else:
                    current[lsdata[1]] = int(lsdata[0])
                com_idx += 1
        elif command.startswith("$ cd"):
            dirname = command.split()[-1]
            current = current[dirname]
        com_idx+=1
    return root

def get_dir_sizes(root):
    dir_sizes = []
    def traverse(node):
        size = 0
        for name, value in node.items():
            if name != "..":
                if type(value) is dict:
                    size += traverse(value)
                elif type(value) is int:
                    size += value
                else:
                    raise ValueError("Unknown value type")
        dir_sizes.append(size)
        return size
    traverse(root)
    return dir_sizes
    



def main(data_file):
    with open(data_file) as f:
        commands = f.readlines()
    # create tree
    root = create_tree(commands)
    # get dir sizes
    dirsizes = get_dir_sizes(root)
    need_del = 30000000 - (70000000 - max(dirsizes))
    return min([i for i in dirsizes if i >= need_del])
    
    
    

if __name__ == "__main__":
    print("****** Test Log *******")
    tout = main('data_7.t')
    print("****** Main Log *******")
    mout = main('data_7')
    print("****** Test Data *******")
    print(tout, "24933642")
    print("****** Real Data *******")
    print(mout)
    