texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

texto = texto.lower()
texto = texto.replace('.','')
texto = texto.replace(',','')
texto = texto.replace(':','')
texto = texto.split()

words_list = []
words_many = 0
for palavra in texto:
    x = 0
    while x<len(palavra):
        if palavra[x] in 'python' and len(palavra)>4:
            words_many += 1
            words_list.append(palavra)
            break
        else:
            x=x+1
print(words_many)
print(words_list)
