## Произвольное предложение
sentence = "the quick brown fox jumps over the lazy dog"
## Делим на слова
words = sentence.split()
## Создание списка с длинами слов
word_lengths = [len(word) for word in words if word != "the"]

## Выведем слова и их длины
print(words)
print(word_lengths)