def is_anagram(test, original):
    def getFrequencies(word):
        frequencies = {}
        for ch in word:
            ch = ch.lower()
            if frequencies.get(ch) != None:
                frequencies[ch] = frequencies[ch] + 1
            else:
                frequencies[ch] = 1
        return frequencies
    return getFrequencies(test) == getFrequencies(original)

print(is_anagram("foefet", "toffee"))
print(is_anagram("Buckethead", "DeathCubeK"))
print(is_anagram("Twoo", "WooT"))
print(is_anagram("dumble", "bumble"))
print(is_anagram("ound", "round"))
print(is_anagram("apple", "pale"))