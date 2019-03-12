# This is a work-in-progress

keypad_mapping = {2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PRS',8:'TUV',9:'WXY'}


class Node(object):
    def __init__(self, char : str):
        self.char = char
        self.children = []
        self.is_end_of_word = False    

class Trie(object):
    def __init__(self):
        self.root = Node(None)

    def add(self, word):
        node = self.root
        for c in word:
            found = False
            for child in node.children:
                if child.char == c:
                    found = True
                    node = child
                    break
            if not found:
                new_node = Node(c)
                node.children.append(new_node)
                node = new_node
        node.is_end_of_word = True

    def find(self, word):
        node = self.root
        for c in word:
            found = False
            for child in node.children:
                if child.char == c:
                    found = True
                    node = child
                    break
            if not found:
                return False
        return True

def generate_name(serial_no, idx=None, sofar=None):
    if idx is None:
        generate_name(serial_no, 0, '')
    else:
        if idx == len(serial_no):
            print(sofar)
            return
        cur_digit = int(serial_no[idx])
        if cur_digit in keypad_mapping:
            for c in keypad_mapping[cur_digit]:
                # TODO: Filter using trie
                if trie.find(sofar+c):
                    generate_name(serial_no, idx+1, sofar+c)
        else: 
            # keypad mapping does not contain the current digit of serial number.
            # Just move to the next digit with the current result so far.
            if trie.find(sofar):
                generate_name(serial_no, idx+1, sofar)

def load_names(trie):
    fin = open('dict.txt', 'r')
    for line in fin.readlines():
        trie.add(line.strip())

trie = Trie()
load_names(trie)
generate_name('4734')
