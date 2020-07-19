class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        word_len = len(beginWord)
        d = collections.defaultdict(list)
        for w in wordList:
            for i in range(word_len):
                d[w[:i] + '*' + w[i+1:]].append(w)
        
        queue = [beginWord]
        visited = []
        level = 1
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur == endWord: return level
                if cur not in visited:
                    visited.append(cur)
                    for i in range(word_len):
                        queue.extend(d[cur[:i] + '*' + cur[i+1:]])
            level += 1
        return 0