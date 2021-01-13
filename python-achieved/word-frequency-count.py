from collections import Counter
texts = '你到底知不知道知道里面有一个知一个道，我知道你知道知道里面一个知道'
texts_counts = Counter(texts)
top_three_text = texts_counts.most_common(3)
print(top_three_text)
