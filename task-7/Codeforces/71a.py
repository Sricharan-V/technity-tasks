def shorten_word(word):
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[-1]
    else:
        return word

def way_too_long_words(words):
    shortened_words = [shorten_word(word) for word in words]
    return shortened_words

word=[]
for _ in range(int(input())):
    word.append(input())

print('\n'.join(way_too_long_words(word)))