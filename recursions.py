# simple recusive functions with limit


def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n

    return n + fibonacci(n-1)

def reverse_word(word):
    if len(word) == 0:
        return word


    return reverse(word[1:]) + word[0]

def gen_vakya(wordlist, index, vakya):
    if index == len(wordlist):
        print(vakya)
        return

    for word in wordlist[index]:
        vakya.append(word)
        gen_vakya(wordlist, index + 1, vakya )
        vakya.pop()

    
