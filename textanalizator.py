
new_text = input('Введите текст: ')

text = new_text.lower()

punctutions = ['.', ',', '!', '?', ':', ';', '—']

for char in punctutions:
   text =  text.replace(char, '')

words = text.split()

print('Кол-во слов:', len(set(words)))

logest_word = words[0]

for word in words:
   if len(word) > len(logest_word):
      logest_word = word

print('Самое длинное слово:', logest_word)

short_word = words[0]
short_words = []

for word in words:
   if len(word) <= len(short_word):
      short_word = word
      short_words.append(word)

short = []

for i in short_words:
   if len(i) == len(short_word):
      short.append(i)

print('Самое короткое слово:', short)

word_frequency = {}

for word in words: 
   if word in word_frequency:
      word_frequency[word] += 1
   else:
      word_frequency[word] = 1

for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")

char_frequency = {}

for char in new_text: 
   if char in char_frequency:
      char_frequency[char] += 1
   else:
      char_frequency[char] = 1

for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")

# Волшебное слово рассказ Валентины Осеевой, в котором ребята могут узнать себя или своих знакомых. В нем представлена встреча расстроенного мальчика Павлика со стариком в парке. а
