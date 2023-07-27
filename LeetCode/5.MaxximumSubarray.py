class Solution (object):

    def max_subarray(nums: list[int]) -> int:

        max_val = nums[0] #maximum value
        cur_val = int() #current value
 
        for number in nums:
            
            #Keep iterating
            cur_val += number

            #Keep updating the max_value
            max_val = max(max_val, cur_val)
            
            #Iteration restart if the current value becomes negative after cumilative addtion
            if cur_val<0 :
                cur_val = 0
                continue
            

        return max_val



def main() -> None: 
    
    input = [[-2,1,-3,4,-1,2,1,-5,4],
            [1],
            [5,4,-1,7,8],
            [-1],
            [-2,-1],
            [-2,1,-3,4,-1,2,1,-5,4]]
    output = [6,1,23,-1,-1,6]

    for index, nums in enumerate(input):
        print(f"The nums list is: {input[index]}")
        print(f"The calculated max_subarray: {Solution.max_subarray(nums)}")
        print(f"The expected max_subarray: {output[index]}")
        
    

if __name__ == "__main__":
    main()