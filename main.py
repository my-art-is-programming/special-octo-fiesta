import argparse


arr = [0, 12, 29, 52, 60, 63, 70, 93, 99, 123, 130, 134, 139, 139, 182, 195, 212, 218, 222, 224, 228, 234, 235, 237,
       244, 255, 259, 269, 271, 288, 297, 297, 299, 310, 316, 332, 353, 377, 378, 387, 391, 418, 431, 442, 444, 459,
       460, 464, 490, 571, 599, 605, 634, 637, 647, 654, 656, 663, 669, 683, 689, 691, 710, 713, 715, 720, 722, 732,
       732, 738, 745, 752, 758, 764, 765, 771, 772, 806, 813, 818, 829, 870, 875, 885, 907, 921, 923, 923, 931, 931,
       941, 944, 951, 954, 959, 965, 974, 985, 988, 989]


def binarysearch(n: int, x: list):
    low = 0
    high = len(x) - 1

    while low <= high:
        mid = int((low + high) / 2)
        print(x[low:high], low, high, mid)
        if n == x[mid]:
            return mid
        elif n < x[mid]:
            high = mid - 1
        elif n > x[mid]:
            low = mid + 1


parser = argparse.ArgumentParser(description='Process some number.')
parser.add_argument('integers', type=int, help='number to find in array')
args = parser.parse_args()
print(args.integers)


if __name__ == '__main__':
    a = binarysearch(args.integers, arr)
    print(a)
