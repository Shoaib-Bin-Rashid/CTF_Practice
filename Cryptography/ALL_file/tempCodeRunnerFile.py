import matplotlib.pyplot as plt
import numpy as np
import random
import time


def repeat_quick(pt_lst, pt1, pt2):
    max_pt = max_point(pt_lst, pt1, pt2)
    if max_pt is None:
        return []
    part1 = [pt for pt in pt_lst if isleft(pt, pt1, max_pt) > 0]
    part2 = [pt for pt in pt_lst if isleft(pt, max_pt, pt2) > 0]
    return repeat_quick(part1, pt1, max_pt) + [max_pt] + repeat_quick(part2, max_pt, pt2)

def quickhull(pt_lst):
    if len(pt_lst) < 3:
        return pt_lst
    min_pt = min(pt_lst, key=lambda pt: pt[0])
    max_pt = max(pt_lst, key=lambda pt: pt[0])
    upper_pts = [pt for pt in pt_lst if isleft(pt, min_pt, max_pt) > 0]
    lower_pts = [pt for pt in pt_lst if isleft(pt, max_pt, min_pt) > 0]
    upper_hull = repeat_quick(upper_pts, min_pt, max_pt)
    lower_hull = repeat_quick(lower_pts, max_pt, min_pt)
    return [min_pt] + upper_hull + [max_pt] + lower_hull

def graham_scan(pt_lst):
    ref_pt = min(pt_lst, key=lambda pt: (pt[1], pt[0]))
    pt_lst.pop(pt_lst.index(ref_pt))
    pt_lst = sorted(pt_lst, key=lambda pt: (np.arctan2(pt[1] - ref_pt[1], pt[0] - ref_pt[0]), -distsq(ref_pt, pt)))
    pt_lst.insert(0, ref_pt)
    hull_stack = [pt_lst[0], pt_lst[1], pt_lst[2]]
    for i in range(3, len(pt_lst)):
        while len(hull_stack) > 1 and position(hull_stack[-2], hull_stack[-1], pt_lst[i]) != 2:
            hull_stack.pop()
        hull_stack.append(pt_lst[i])
    return hull_stack


    
def distance(pt, pt1, pt2):
    return abs((pt2[1] - pt1[1]) * pt[0] - (pt2[0] - pt1[0]) * pt[1] + pt2[0] * pt1[1] - pt2[1] * pt1[0])

def max_point(pt_lst, pt1, pt2):
    max_dist = -1
    max_pt = None
    for pt in pt_lst:
        dist = distance(pt, pt1, pt2)
        if dist > max_dist:
            max_dist = dist
            max_pt = pt
    return max_pt

def isleft(pt, pt1, pt2):
    return (pt2[1] - pt1[1]) * (pt[0] - pt1[0]) - (pt2[0] - pt1[0]) * (pt[1] - pt1[1])




def position(pt1, pt2, pt3):
    val = (pt2[1] - pt1[1]) * (pt3[0] - pt2[0]) - (pt2[0] - pt1[0]) * (pt3[1] - pt2[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def distsq(pt1, pt2):
    return (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2



def main_program():
    while True:
        n = int(input("Enter number of points: "))
        if n >= 3:
            break
        print("At least 3 points required to draw convex hull.")

    pts = [(random.uniform(1, 20), random.uniform(1, 20)) for _ in range(n)]
    print("All Points:")
    for idx, pt in enumerate(pts, 1):
        print(f"Point {idx}: {pt}")

    while True:
        print("\nChoose Operation:")
        print("1. Convex Hull with Graham Scan")
        print("2. Convex Hull with Quickhull")
        print("3. Exit")
        user_choice = int(input("Your choice: "))

        if user_choice == 1:
            start = time.perf_counter()
            result_hull = graham_scan(pts)
            end = time.perf_counter()
            t = (end - start) * 1_000_000
            print(f"\nGraham Scan Execution time : {t:.2f} microseconds")
            

        elif user_choice == 2:
            start = time.perf_counter()
            result_hull = quickhull(pts)
            end = time.perf_counter()
            t = (end - start) * 1_000_000
            print(f"\nQuickhull Execution time: {t:.2f} microseconds")

        elif user_choice == 3:
            print("Thank You for using our program")
            break

        else:
            print("Invalid choice.")
            continue

        plt.figure(figsize=(8, 8))
        plt.scatter(*zip(*pts), label="Points")
        result_hull.append(result_hull[0])
        plt.plot(*zip(*result_hull), 'r-', label="Convex Hull")
        plt.scatter(*zip(*result_hull), color="red")
        plt.legend()
        plt.title(f"Convex Hull with {'Quickhull' if user_choice == 2 else 'Graham Scan'}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

if __name__ == "__main__":
    main_program()
