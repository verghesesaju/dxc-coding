def fibonacci(number):
    a = 0
    b = 1
    count = 0
    while count < number:
        print(a)
        c = a+b
        a=b
        b=c
        count+=1

fibonacci(8)