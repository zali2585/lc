
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = collections.deque([(beginWord, 1)])

        #use bfs bc it progresses step by step, so ur guaranteed shortest amt of steps for solution u find
        #bfs is represented by while queue loop
        while queue:
            word, steps = queue.popleft()

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    # first segment doesnt include i
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word == endWord:
                        return steps + 1
                    if new_word in word_set:
                        queue.append((new_word, steps + 1))
                        word_set.remove(new_word)
        return 0



        