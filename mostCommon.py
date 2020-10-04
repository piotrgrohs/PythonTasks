stop_words =  ["a", "about"]

text_1 = '''Python vs Java – Which Programming Language is Ruling in 2020
Programming Languages are an essential piece of computer science; they are elementary tools in a programmer’s toolkit and vital to nearly every programming activity. Do you know there are even websites which can help you with your assignments? Find a good programmer and get your job done! In this plenitude of programming languages reigning the IT globe, there are two hottest names that are combating against each other and are experiencing serious comparison – Python vs Java! Yes! So, which programming language will continue to be in demand in 2020 and beyond? This scenario is a brief comparison making your selection smooth and easy. Let us go through the intricate details of both, to understand them better.
'''
import re
from collections import Counter

def rm_stop_words(text,stop_words): 
    text = re.sub(r"\b{}\b".format(stop_words[-1]),'',text, flags=re.IGNORECASE)
    stop_words.pop()
    if len(stop_words) > 0:
        return rm_stop_words(text,stop_words)
    else:
        return text

def rm_lessthan(text):
    return re.sub(r"\b\w{1,3}\b",'',text)

def rm_specialchar(text):
    return re.sub("[^A-Za-z0-9\s]",'',text)

def strToList(text):
    return list(text.split())

def main(text):
    text = rm_stop_words(text,stop_words)
    text = rm_lessthan(text)
    text = rm_specialchar(text)
    text = strToList(text.lower())
    return [text for text in Counter(text).most_common(10)]
    
print(main(text_1))
