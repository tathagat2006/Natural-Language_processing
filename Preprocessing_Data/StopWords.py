from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_word = set(stopwords.words("english"))
words = word_tokenize(example_sent)
# filtered_sentence = []

# for w in words:
# 	if w not in stop_word:
# 		filtered_sentence.append(w)


# ALTERNATE OF ABOVE FOR LOOP AND STEP 8.
filtered_sentence = [w for w in words if not w in stop_word]
print(filtered_sentence)