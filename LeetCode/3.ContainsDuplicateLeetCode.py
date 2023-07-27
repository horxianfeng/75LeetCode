class Solution():

    def contain_duplicate (nums: list[int]) -> bool:
        nums_temporary = set()
        for number in nums:
            if number in nums_temporary:
                return True
            else:
                nums_temporary.add(number)
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