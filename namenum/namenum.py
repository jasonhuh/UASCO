"""
ID: jasonhu5
LANG: PYTHON3
TASK: namenum
"""

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

    def find(self, word, partial_search):
        """
        partial_search is a flag to allow a prefix search if True. If the flag is false,
        the method will return True only if the result is an extact match.
        """
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
        if partial_search:
            return True
        return node.is_end_of_word

def solve(serial_no):
    def load_names(trie):
        fin = open('dict.txt', 'r')
        for line in fin.readlines():
            trie.add(line.strip())

    def generate_name(serial_no, idx=None, sofar=None):
        if idx is None:
            generate_name(serial_no, 0, '')
        else:
            if idx == len(serial_no):
                if trie.find(sofar, False):
                    output.append('{}\n'.format(sofar))
                return
            cur_digit = int(serial_no[idx])
            if cur_digit in keypad_mapping:
                for c in keypad_mapping[cur_digit]:
                    # TODO: Filter using trie
                    if trie.find(sofar+c, True):
                        generate_name(serial_no, idx+1, sofar+c)
            else: 
                # keypad mapping does not contain the current digit of serial number.
                # Just move to the next digit with the current result so far.
                if trie.find(sofar, True):
                    generate_name(serial_no, idx+1, sofar)

    keypad_mapping = {2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PRS',8:'TUV',9:'WXY'}
    trie = Trie()
    load_names(trie)
    output = []
    generate_name(serial_no)
    if len(output) == 0:
        output.append('NONE\n')
    return sorted(output)

def test_simple():
    assert solve('4734') == ['GREG\n']
    assert solve('234643') == ['NONE\n']
    assert solve('223') == ['ABE\n', 'ACE\n']

if __name__ == '__main__':
    fin = open('namenum.in','r')
    fout = open('namenum.out','w')
    serial_no = fin.readline().strip()
    ans = solve(serial_no)
    fout.write(''.join(ans))
