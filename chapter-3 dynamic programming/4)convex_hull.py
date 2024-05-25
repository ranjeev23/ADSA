# convex hull problem

'''
angle grater than 180 is convex
'''

# code
def quickhull(v):

    # if len of vertices is less than 2 return v
    if len(v) <= 2:
        return v

    convex_hull = []

    # sort based on x cordinate
    sort = sorted(v, key=lambda x:x[0])

    # find the lowest and highest x coordinate
    p1 = sort[0]
    p2 = sort[-1]

    # add the 2 poin ts to the convex hull
    convex_hull = convex_hull + [p1,p2]

    # remove the 2 points from the vertices
    sort.pop(0)
    sort.pop(-1)

    # determine the lines above and below the line
    above,below = create_segment(p1,p2,sort)

    # determine the lines above and below the line
    convex_hull = convex_hull + quickhull_2(p1,p2,above,'above')
    convex_hull = convex_hull + quickhull_2(p1, p2, below, 'below')

    return convex_hull

def quickhull_2(p1,p2,segment,flag):

    # base condition for recurrsion
    if segment == [] or p1 is None or p2 is None:
        return []

    # set a convex hull for the base
    convex_hull = []

    # find the farthest point from the line
    farthest_distance = -1
    farthest_point = None
    for point in segment:
        distance = find_distance(p1,p2,point)
        if distance>farthest_distance:
            farthest_distance = distance 
            farthest_point = point

    # add the farthest point to the convex hull
    convex_hull.append(farthest_point)

    # remove the point from the segment
    segment.remove(farthest_point)

    # Segments
    # find the above and below points from p1 to fartest point
    # find the above and below points from p2 to fartest point
    point1above,point1below = create_segment(p1,farthest_point,segment)
    point2above, point2below = create_segment(farthest_point, p2,segment)

    if flag == 'above':
        convex_hull = convex_hull + quickhull_2(p1,farthest_point,point1above,'above')
        convex_hull = convex_hull + quickhull_2(farthest_point,p2, point2above,'above')

    else:
        convex_hull = convex_hull + quickhull_2(p1, farthest_point, point1below,'below')
        convex_hull = convex_hull + quickhull_2(farthest_point, p2, point2below, 'below')

    return convex_hull


def create_segment(p1,p2,v):
    above = []
    below = []

    if p2[0] - p1[0] == 0:
        return above,below

    # calcualte m and c
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    c = -m * p1[0] + p1[1]

    for coordinate in v:

        #if y value is greater than mx + c then it lies above the line
        if coordinate[1] > m * (coordinate[0]) + c:
            above.append(coordinate)

        #if y value is less than mx + c then it lies below the line
        if coordinate[1] < m * (coordinate[0]) + c:
            below.append(coordinate)

    return above,below

def find_distance(p1,p2,p3):
    
    a = p1[1] - p2[1]
    b = p2[0] - p1[0]
    c = p1[0]*p2[1] - p2[0]*p1[1]

    return abs(a*p3[0] + b*p3[1] + c)/((a*a +b*b)**(0.5))


points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
hull = quickhull(points)
print("Convex Hull:", hull)

points = [(1, 1), (2, 5), (3, 3), (5, 3), (3, 2), (4, 5), (1, 2), (4, 1)]
hull = quickhull(points)
print("Convex Hull:", hull)
