class Solution():

    def contain_duplicate (nums: list[int]) -> bool:
        for index, number in enumerate(nums):
            numsListAfterIndex = nums[index+1:]
            if number in numsListAfterIndex:
                return True
        return False


def main() -> None: 
    
    input = [[1,2,3,1],
            [1,2,3,4],
            [1,1,1,3,3,4,3,2,4,2]]
    output = [True, False, True]

    for index, nums in enumerate(input):
        print(f"The nums list is: {nums}")
        print(f"The list contains duplicate: {Solution.contain_duplicate(nums)}")
        
    

if __name__ == "__main__":
    main()