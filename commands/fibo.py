def fibo(n):
    a=0
    b= 1
    for _ in range(n):
        print(b)
        temp = b 
        b +=a 
        a =temp
        # OR a,b = b,a+b
    print(f"the {n} th term is {a}")



def run():
    n = int(input("Enter where to stop the sequence :"))
    fibo(n)
    
