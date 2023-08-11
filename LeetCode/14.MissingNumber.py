class Solution (object):

    def missing_number (nums: list[int]) -> int:
        nums.sort()
        ans = 0

        if nums[len(nums)-1] != len(nums):
            return len(nums)

        for i in range(len(nums)):
            if i != nums[i]:
                ans = i
                break    
        return ans
        

    
def main() -> None: 
    
    input = [[3,0,1],
             [0,1],
             [9,6,4,2,3,5,7,0,1]] 
    output = [2,2,8]

    for index, nums in enumerate(input):
        print(f"The input: {input[index]}")
        print(f"The output: {Solution.missing_number(nums)}")
        print(f"The expected output: {output[index]}")
        
    

if __name__ == "__main__":
    main()