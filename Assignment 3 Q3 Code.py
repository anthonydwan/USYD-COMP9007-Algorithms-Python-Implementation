def merge(arr1, arr2):
    results = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i][0] < arr2[j][0]:
            results.append(arr1[i])
            i += 1
        elif arr1[i][0] == arr2[j][0]:  # if tiebreak, we pick the line with highest y_intercepts sorted
            if arr1[i][1] < arr2[j][1]:
                results.append(arr2[j])
                i += 1
                j += 1
            else:
                results.append(arr1[i])
                i += 1
                j += 1
        else:
            results.append(arr2[j])
            j += 1
    if i < len(arr1):
        results.extend(arr1[i:])
    if j < len(arr2):
        results.extend(arr2[j:])
    return results


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


def fish_bowl(arr, x_range):
    arr = merge_sort(arr)
    int_pts = []
    # remove lines in base cases
    if len(arr) ==1:
        int_pts.append([x_range[0], arr[0][0] * x_range[0] + arr[0][1]])
        int_pts.append([x_range[1], arr[0][0] * x_range[1] + arr[0][1]])
        return int_pts
    elif len(arr) == 2:  # if two lines
        a1, b1 = arr[0][0], arr[0][1]
        a2, b2 = arr[1][0], arr[1][1]
        x_value = ((b1 - b2) / (a2 - a1))

        if x_value <= x_range[1] and x_value >= x_range[0]:
            int_pts.append([x_range[0], a1 * x_range[0] + b1])
            int_pts.append([x_value, a1 * x_value + b1])
            int_pts.append([x_range[1], a2 * x_range[1] + b2])
        elif x_value > x_range[1]:
            int_pts.append([x_range[0], a1 * x_range[0] + b1])
            int_pts.append([x_range[1], a1 * x_range[1] + b1])
        else:
            int_pts.append([x_range[0], a2 * x_range[0] + b2])
            int_pts.append([x_range[1], a2 * x_range[1] + b2])

        return int_pts
    else:
        middle = (len(arr) // 2)
        left = fish_bowl(arr[:middle], x_range)
        right = fish_bowl(arr[middle:], x_range)
        return pts_merge(left, right, x_range)


def pts_merge(int_pt1, int_pt2,x_range):
    arr1_int_x = []
    arr2_int_x = []
    for points in int_pt1[1:-1]:
        arr1_int_x.append(points[0])  # taking out int pts at printing range of left set
    for points in int_pt2[1:-1]:
        arr2_int_x.append(points[0])  # taking out int pts at printing range of right set

    arr1 = []
    arr2 = []
    for i in range(len(int_pt1) - 1):  # there are at least 2 points in base case
        a1 = (int_pt1[i+1][1] - int_pt1[i][1])/(int_pt1[i+1][0] - int_pt1[i][0])
        b1 = a1*(-int_pt1[i][0]) + int_pt1[i][1]
        arr1.append([a1, b1])
    for j in range(len(int_pt2) - 1):  # there are at least 2 points in base case
        a2 = (int_pt2[j+1][1] - int_pt2[j][1])/(int_pt2[j+1][0] - int_pt2[j][0])
        b2 = a2*(-int_pt2[j][0]) + int_pt2[j][1]
        arr2.append([a2, b2])



    if len(arr1_int_x) ==0 and len(arr2_int_x) ==0:
        arr = []
        arr.extend(arr1)
        arr.extend(arr2)
        return fish_bowl(arr,x_range)

    i, j = 0, 0


    while i < len(arr1_int_x) or j < len(arr2_int_x):
        a1, b1 = arr1[i][0], arr1[i][1]
        a2, b2 = arr2[j][0], arr2[j][1]

        if i == len(arr1_int_x):
            if a1 * arr2_int_x[j] + b1 >= a2 * arr2_int_x[j] + b2:
                j += 1
            else:
                break
        elif j == len(arr2_int_x):
            if a1 * arr1_int_x[i] + b1 >= a2 * arr1_int_x[i] + b2:
                i += 1
            else:
                break
        elif arr1_int_x[i] < arr2_int_x[j]:
            if a1 * arr1_int_x[i] + b1 >= a2 * arr1_int_x[i] + b2:
                i += 1
            else:
                break
        else:
            if a1 * arr2_int_x[j] + b1 >= a2 * arr2_int_x[j] + b2:
                j += 1
            else:
                break

    int_pts = []
    a1, b1 = arr1[i][0], arr1[i][1]
    a2, b2 = arr2[j][0], arr2[j][1]
    new_x_value = ((b1 - b2) / (a2 - a1))
    new_y_value = a1 * new_x_value + b1

    if new_x_value < x_range[0]:
        int_pts = int_pt2
    elif new_x_value > x_range[1]:
        int_pts = int_pt1
    else:
        for pt in int_pt1[0:i + 1]:
            if len(int_pts) != 0:
                if pt[0] != int_pts[-1][0]:
                    int_pts.append(pt)
            else:
                int_pts.append(pt)
        if new_x_value != int_pts[-1][0]:
            int_pts.append([new_x_value, new_y_value])
        for pt in int_pt2[j+1:]:
            if pt[0] != int_pts[-1][0]:
                int_pts.append(pt)


    return int_pts



lines = [[-2,0],[0.5,3],[0,3]]
x = [-4, 4]

print(fish_bowl(arr=lines, x_range=[-4,4]))


#testing examples
# print(fish_bowl(arr=[[-3.1, -50], [-3, -70], [-3, -60], [-3, -50], [-3,-40], [-3, -20], [-3, -2.5], [-2.9, -50], [-2.9, -80], [-2.8, -50], [-2.7, -50], [-1.2, 7], [1, 7], [1.25, 5],[1.5, 3], [3, 3]], x_range=[-10, 10]))
# print(fish_bowl([[-3.1, -50], [-3, -2.5], [-1.2, 7], [1, 7], [1.25, 5], [3, 3]], x_range=[-25, -24]))
# print(fish_bowl([[-2.5,5],[-2.1,5],[-2,5],[1,5]], x_range=[-0.1, 25]))
# print(fish_bowl([[-0.4,-20],[0.5,-16],[-2,4],[-2,5],[-1.5,4],[-0.5,-1],[0,-8]], x_range=[-20, -15]))
# print(fish_bowl([[-3.1, 10],[-3, -70], [-3, -60], [-3, -50], [-3,-40], [-3, -20], [-3, -2.5], [-2.9, -50], [-2.9, 3000000], [-2.8, -50], [-2.7, -50], [-1.2, 7], [1, 7], [1.25, 5],[1.5, 3], [3, 3], [3, 300000000],[3.1,10000000],[0,4]], x_range=[-100, 100]))
