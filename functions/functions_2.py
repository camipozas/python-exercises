'''
Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
'''


def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentence: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase sentence.
    '''
    return {word: len(word) for word in sentence.split()}


print(length_words('Welcome to Python'))
