# your code goes here!
class Anagram:
    # word_received represents the word for which we want to find its anagrams
    def __init__(self, word_received):
        # will return the sorted word in characters arranged by alphabetic order
        self.word = "".join(sorted(word_received))

    def match(self, words_list):
        # this will hold the anagrams of the word_received form the words_list provided
        matches = []
        # checks each word in the given list to see which matches the word_received
        for word in words_list:
            if "".join(sorted(word)) == self.word:
                matches.append(word)

        return matches    

listen = Anagram("listen")
print(listen.match(["enlists", "goole", 'inlets']))            