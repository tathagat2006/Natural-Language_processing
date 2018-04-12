# ENDING UP WITH THE SYNONYM OF THE ACTUAL WORD. YOU MIGHT GET AN ENTIRELY DIFFERNET WORD BUT IT WILL HAVE THE SAME MEANING.
# The only major thing to note is that lemmatize takes a part of speech parameter, "pos." If not supplied, the default is "noun." 
# This means that an attempt will be made to find the closest noun,which can create trouble for you.Keep this in mind if you use lemmatizing!
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))