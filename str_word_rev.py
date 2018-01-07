input_sent = input("enter a sentence:").split(" ")
word_list = []
for word in input_sent:
    word = word[::-1]
    word_list.append(word)
print(" ".join(word_list))

