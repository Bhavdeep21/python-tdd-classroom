class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return "".join(reversed(input_str))

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        vowels=['a','e','i','o','u','A','E','I','O','U']
        return True if character in vowels else False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        longest=max(sentence.split(),key=len)
        return longest

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """

        return list(map(len,text.split()))