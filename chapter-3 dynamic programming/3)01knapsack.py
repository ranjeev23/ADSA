# 0/1 knapsack problem

'''
given a set of objects which have both value and a weifht (vi,wi) what is the mximum value we can obtain by selecting
subset of objects such that sum of weights sum of weights does not succed a certain capacity?
'''

'''
allowed weight: 7kg
o1: 5$,4kg 
o2: 2$,3kg 
o3: 3$,2kg 
o4: 2$,1kg 
o5: 4$,3kg
'''

'''
i = item, the row we are in
w = max Weight, the  coulumn that we are in

V[i][w]=max{v[i-1][w],v[i-1][w-wi]+vi},
        v[i-1][w] other wise

0,1,2,3,4,5[tha eallowed wights]
0,0,0,0,0,60
0,0,0,50,50,60
0,0,0,50,70,70
0,0,30,50,70,80
'''

# code
def knapsack(W,wt,value,n):

    # base case
    if n==0 or W==0:
        return 0

    '''
    if weight of the nth item is 
    more than knapsack capacity W,
    then the item cannot be included in the optimal solution
    '''

    """
    choose val[current_product] + best(val[prev_product]) with subtracting weight of current product
      or
    choose best(val[prev_product]) without subtracting weight
    """
    if wt[n-1]>W:
        return knapsack(W,wt,value,n-1)
    else:
        return max(value[n-1] + knapsack(W-wt[n-1],wt,value,n-1),knapsack(W,wt,value,n-1))

profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(profit)
print(knapsack(W, weight, profit, n))
