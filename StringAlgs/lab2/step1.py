import sys


class Node:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.failure = None


class AhoCorasick:
    def __init__(self):
        self.root = Node()
        self.patterns = []

    def create_trie(self, patterns):
        for pattern in patterns:
            node = self.root
            self.patterns += [pattern]
            for ch in pattern:
                node = node.goto.setdefault(ch, Node())
            node.out.append(len(self.patterns)-1)

    def create_states(self, patterns):
        self.create_trie(patterns)
        queue = []
        for node in self.root.goto.values():
            queue.append(node)
            node.failure = self.root
        while len(queue) > 0:
            rnode = queue.pop(0)
            for key, unode in rnode.goto.items():
                queue.append(unode)
                fnode = rnode.failure
                while fnode is not None and key not in fnode.goto:
                    fnode = fnode.failure
                unode.failure = fnode.goto[key] if fnode else self.root
                unode.out += unode.failure.out

    def find_all(self, text):
        d = []
        node = self.root
        for i in range(len(text)):
            while node is not None and text[i] not in node.goto:
                node = node.failure
            if node is None:
                node = self.root
                continue
            node = node.goto[text[i]]
            for pat_num in node.out:
                d.append((i - len(self.patterns[pat_num]) + 1, pat_num))
        return d


def main():
    patterns = []
    text = sys.stdin.readline().strip()
    n = int(input())
    for i in range(n):
        patterns.append(sys.stdin.readline().strip())
    finder = AhoCorasick()
    finder.create_states(patterns)
    d = finder.find_all(text)
    for pair in d:
        print(pair[0]+1, pair[1]+1)


if __name__ == '__main__':
    main()