def filter_words(text1, text2):
    words_set = set(text1.split())
    filtered_text = ' '.join(word for word in text2.split() if word not in words_set)
    return filtered_text


text1 = "apple orange banana"
text2 = "banana cherry apple kiwi orange"
result_text = filter_words(text1, text2)
print(f"Текст після вилучення слів: {result_text}")
