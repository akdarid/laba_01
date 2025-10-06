def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return "ValueError"
    return(min(nums), max(nums))
print(min_max([]))

def unique_sorted(nums):
    return (set(nums))

a = [[1,2,3],[4,5,2],[7,5,9]]


def flatten(mat: list[list | tuple]) -> list:
    f = "1234567890"
    ans = []
    for i in mat:
        for j in i:
            if str(j) not in f:
                return ("mudak")
            else:
                ans.append(j)
    return ans




