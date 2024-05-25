'''
Prioblem statement:
params: n and k
return binomial coefficent of c(n,k)


formula:
C(n,k) = c(n-1,k-1) + c(n-1,k)

c(n,0) = c(n,n) = 1

here always n>k
'''

'''
Base conditions

k>n;return 0
k=0; return 1
k=n;return 1


tree(4,2)
4,2
    3,1
        2,0 -> 1
    1,1 -> 1
2,2 ->1






'''

def binomial_coefficients(n,k):

    print(n, k)

    # always n>k
    if k>n:
        return 0
    elif k==n or k==0:
        print('adding 1')
        return 1

    return binomial_coefficients(n-1,k-1)+binomial_coefficients(n-1,k)

print(binomial_coefficients(5,2))
