class Solution():

    def two_sum (nums: list[int], target: int) -> list:
         for index, number in enumerate(nums):
             diff = target - number
             if (diff in nums) and (diff in nums[index+1:]):
                return [index, nums[index+1:].index(diff)+index+1]
         

def main() -> None:

    nums = [[2,7,11,15],
            [3,2,4],
            [3,3]]

    target = [9,6,6]

    for index, test in enumerate (nums):
        print (f"\nThe nums list is: {nums[index]}")
        print (f"The target is: {target[index]}")
        print (f"The solution is: {Solution.two_sum(nums[index], target[index])}")
       

       
if __name__ == "__main__":
    main()            
             
             
                 






        