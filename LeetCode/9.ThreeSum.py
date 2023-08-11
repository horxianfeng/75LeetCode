class Solution (object):

    def three_sum (nums : list[int]) -> list:
        
        result = []
        
        # Sort the num list in ascending order
        nums.sort()
        
        for i, number in enumerate(nums):
            l, r = i +1, len(nums)-1            
            while l<r:
                print (l,r)
                three_sum = number + nums[l] + nums[r]
                if three_sum > 0: r-=1
                if three_sum < 0: l+=1
                if three_sum == 0:
                    result.append([number, nums[l], nums[r]])
                    l += 1
    
        
        # Exclude the duplicate
        result_without_duplicate = []
        for combinations in result:
            if combinations not in result_without_duplicate: result_without_duplicate.append(combinations)
        
        return result_without_duplicate








def main() -> None: 
    
    input = [[-1,0,1,2,-1,-4],
           [0,1,1],
           [0,0,0]]
    output = [[[-1,-1,2],[-1,0,1]],
              [],
              [0,0,0]]

    for index, nums in enumerate(input):
        print(f"The nums list is: {input[index]}")
        print(f"The calculated product list: {Solution.three_sum(nums)}")
        print(f"The expected product list: {output[index]}")
        
    

if __name__ == "__main__":
    main()