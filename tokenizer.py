vocab = ["i", "like", "love", "apples", "bananas", "mangoes"]
tokenid_sample = {}
tokenid = {}
converted = {}
for i in range(len(vocab)):
    tokenid[vocab[i]] = i
for words in tokenid:
    converted[tokenid.get(words)] = words

embeddings = {0 : [0.12, 0.69, -0.99],
              1 : [0.24, -0.27, -0.18],
              2 : [0.37, 0,23, -0.18],
              3 : [-0.37, -0.28, -0.01],
              4 : [-0.29, 0.57, 0.74],
              5 : [0.19, 0.99, 0.28] }

word = ["i", "like"]
combine_vector = []

for i in range(3):
    vector1 = embeddings.get(tokenid.get(word[0]))
    vector2 = embeddings.get(tokenid.get(word[1]))
    combine_vector.append((vector1[i] + vector2[i]) / 2)
print(combine_vector) 