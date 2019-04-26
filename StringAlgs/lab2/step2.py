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
            self.patterns += [pattern]
            node = self.root
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

    def find_joker(self, text, ind_patterns):
        d = [0]*len(text)
        node = self.root
        for i in range(len(text)):
            while node is not None and text[i] not in node.goto:
                node = node.failure
            if node is None:
                node = self.root
                continue
            node = node.goto[text[i]]
            for pat_num in node.out:
                ind = i - len(self.patterns[pat_num]) - ind_patterns[pat_num] + 1
                if 0 <= ind < len(d):
                    d[ind] += 1

        res = []
        for i in range(len(d)):
            if d[i] == len(ind_patterns):
                res += [i]
        return res


def prepare_patterns(orig_patterns, joker):
    prev_patterns = orig_patterns.split(joker)
    patterns = []
    ind_patterns = []
    ind = 0
    for pat in prev_patterns:
        if pat != '':
            ind_patterns += [ind]
            ind += len(pat)
            patterns += [pat]
        ind += 1
    return patterns, ind_patterns


def main():
    text = sys.stdin.readline().strip()
    mask_pattern = sys.stdin.readline().strip()
    joker = sys.stdin.readline().strip()
    patterns, ind_patterns = prepare_patterns(mask_pattern, joker)
    finder = AhoCorasick()
    finder.create_states(patterns)
    res = finder.find_joker(text, ind_patterns)
    res = [i+1 for i in res]
    print(*res, sep='\n')


if __name__ == '__main__':
    main()