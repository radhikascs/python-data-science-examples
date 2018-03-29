# variable with dirty data
dirty_data = "You're my best friend. She's your best friend too. But she's awesome!"

#Create a dictionary for data munging
APOSTROPHES = {"'s" : " is", "'re" : " are"}

#chop up the words
words = dirty_data.split()

#create a blank list to hold modified words
new_words = []

#looping
for word in words:
    for key in APOSTROPHES.keys():
        if key in word:
            word = word.replace(key, APOSTROPHES[key])
    new_words.append(word)

#reassemble the string

clean_data = " ".join(new_words)

#Output for data munging
print("After the process of data munging:")
print(clean_data)
