def sum(lst, n):
    # Your code here!
    l = len(lst)
    sum = 0
    for i in range(l):
        sum += lst[i]
    if sum == n:
        return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
