"""
Girilen bir metin içinde aranan kelimeyi bulan fonksiyon 
"""

x = input("Please enter a text:")
word= input("Please enter a word:")
def find_word(sentence):
    words_list=x.split(" ")
    for i in words_list:
        if i == word :
            return "True"

print("result",find_word(x))