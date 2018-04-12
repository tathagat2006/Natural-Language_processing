#  THIS IS MAINLY PREPROCESSING DATA.


from nltk.tokenize import word_tokenize , sent_tokenize
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

for i in word_tokenize(EXAMPLE_TEXT):
	print(i + "---------")