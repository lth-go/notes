#!/usr/bin/env python
# encoding: utf-8


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        root = self.root
        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]

        root['end'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.root
        return self._search(word, root)

    def _search(self, word, root):
        if not word:
            return root.get('end', False)

        char = word[0]
        if char == '.':
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c in root:
                    ok = self._search(word[1:], root[c])
                    if ok:
                        return True
            return False
        else:
            if char not in root:
                return False

            return self._search(word[1:], root[char])
