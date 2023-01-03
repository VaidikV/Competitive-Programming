T = int(input())
 
for i in range(T):
    word = str(input())
    word_len = len(word)
    if word_len > 10:
        print(str(word[0])+str(word_len-2)+str(word[word_len-1]))
    else:
        print(word)
