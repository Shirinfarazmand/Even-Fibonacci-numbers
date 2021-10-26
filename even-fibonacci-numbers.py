def fibo():
    first = 1
    second = 2
    even_sum = 0
    while(first < 4000000):
        n =first + second
        first = second
        second = n
        if n % 2 == 0 :
            even_sum += n
            
        
    print(even_sum + 2)

fibo()
