def word_weight(word):
    return sum(ord(ch.lower())-ord('a') + 1 for ch in word)

def  vowel_info(word):
    vowels = "aeiou"
    priority_map = {'a':5, 'e':4, 'i':3, 'o':2, 'u':1}
    count = sum(ch.lower() in vowels for ch in word)
    max_priority = 0
    for ch in word:
        ch_lower = ch.lower()
        if ch_lower in priority_map:
            max_priority = max(max_priority, priority_map[ch_lower])
    return max_priority

def insertion_sort(words,mode):
    for i in range(1,len(words)):
        key = words[i]
        j = i - 1
        while j >= 0:
            if mode == 'W':
                cond = word_weight(words[j]) > word_weight(key)
            else:
                cond = vowel_info(words[j]) > vowel_info(key)
            if cond:
                words[j+1] = words[j]
                j -= 1
            else:
                break
        words[j+1]  = key
    print(' '.join(words))



print("***Fun with Word***")
word , mode = input("Enter Input : ").split('/')
word = list(word.split())
insertion_sort(word,mode)
