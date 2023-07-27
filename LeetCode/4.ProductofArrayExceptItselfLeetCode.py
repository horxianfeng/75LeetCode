class Solution (object):
    
    def product_except_itself(nums: list[int]) -> list:

        result = [1]*len(nums)
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
 
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1]*nums[i]

        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i+1]*nums[i]
        
        # print(prefix)
        # print(postfix)

        for i in range(len(nums)):
            if i == 0:
                result[i] = postfix[i+1]
            elif i == len(nums)-1:
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1]*postfix[i+1]

        return result







def main() -> None: 
    
    input = [[1,2,3,4],
            [-1,1,0,-3,3]]
    output = [[24,12,8,6],
              [0,0,9,0,0]]

    for index, nums in enumerate(input):
        print(f"The nums list is: {input[index]}")
        print(f"The calculated product list: {Solution.product_except_itself(nums)}")
        print(f"The expected product list: {output[index]}")
        
    

if __name__ == "__main__":
    main()