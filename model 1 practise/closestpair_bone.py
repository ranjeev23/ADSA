import math
import random
import time
#calculates distance between 2 points
def calculateDistance(p1,p2):
    #o/p is dist between 2 points
    dist =  ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
    print(dist)
    return dist
    

#bruteforce
def bruteForce(points: list):
    #o/p is tup of 2 points and min distance
    '''
    find min dist between 3 point
    '''
    min_dist,min_point = 100000,None
    for opoint_index in range(len(points)-1):
        for ipoint_index in range(opoint_index+1,len(points)):
            dist = calculateDistance(points[opoint_index],points[ipoint_index])
            if dist < min_dist:
                min_dist = dist
                min_point = (points[opoint_index],points[ipoint_index])
    print('bruteForce',points)
    print(min_dist,min_point)
    return (min_dist,min_point)


#sort points based on x
def sortPoints(points,cord):
    '''
    sort points based on cord
    '''
    if cord == 'x':
        points = sorted(points,key = lambda x:x[0])
    else:
        points = sorted(points, key = lambda x:x[1])
    print(points)
    return points

#Find the strip of points
def Strip(points,distance,midX):
    '''
    find stip of points whose x dist from mid of x is less than distance
    '''
    smallest_point = []
    for point in points:
        if abs(point[0]-midX) < distance:
            smallest_point.append(point)
    print('smallest points')
    print(points,distance,midX)
    print(smallest_point)
    return smallest_point


#find optimized points
def optimized_find_distance(points):
    #o/p is min of points
    '''
    if len of points is less than equal to 3 brute force

    sort point based on x axis

    find median point
    find its left array
    find its right array

    recursively find the optimal points and distance in leftarray and right array

    compare mdl and mdr and assign the min_point and min_dist accordingly

    find mid point by finding right element in left array and left element in right array div by 2

    with this find the points in the 2 parts where dist is less than min distance will find dist between the 2 strips

    sort the strip acc to y axis
    use brute force to find min distance between the points

    check if this min distance is lesser than original min dist if so pass this as ans
    else return other
    '''
    if len(points) <= 3:
        return bruteForce(points)
    
    points = sortPoints(points,'x')

    #find median,left,right
    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]

    print('mid left right')
    print(mid)
    print(left)
    print(right)

    #recurse to find optimal dist
    dl = optimized_find_distance(left)
    dr = optimized_find_distance(right)

    print('dl,dr')
    print(dl)
    print(dr)

    #set min_dist and min_points
    if dl[0] < dr[0]:
        min_dist,min_points = dl
    else:
        min_dist,min_points = dr

    #midpoint
    r = left[-1][0]
    l = right[0][0]
    print('right left',r,l)
    print(r,l)
    mp = (r+l)/2

    #find the closest strips
    hav_comp_points = Strip(points,min_dist,mp)
    print(hav_comp_points)

    hav_comp_points = sortPoints(hav_comp_points,'y')
    dp_tuple = bruteForce(hav_comp_points)

    #is the pairs in border have lesser distance return them as ans
    if dp_tuple[0]<min_dist:
        return dp_tuple

    else:
        return min_dist,min_points

points = [(1,2),(3,4),(5,7),(2.9,-0.75),(1,1.5),(3,-1)]

def generate_points():
    ranger = random.randint(1,10)
    points = []
    for i in range(ranger):
        n1 = random.randint(1,10)
        n2 = random.randint(1,10)
        points.append((n1,n2))
    return points



# calculateDistance(points[0],points[1])
# bruteForce(points)
# sortPoints(points,'x')
# sortPoints(points,'y')
# Strip(points,1,2)
points = generate_points()
print(points)
a1 = optimized_find_distance(points)
a2 = bruteForce(points)

print('ans')
print(a1)
print(a2)

