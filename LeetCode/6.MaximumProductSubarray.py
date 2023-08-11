class Solution (object):

    def maxproduct_subarray(nums: list[int]) -> int:

        maxproduct = cur_max = cur_min = prev_max = pre_min = nums[0]

        for i, number in enumerate(nums):
            
            #Skip if number is initial number: nums[0]
            if i == 0:
                continue

            #If the previous number is 0, reiterate for the next maxproduct
            if nums[i-1] == 0:
                cur_max = cur_min = prev_max = pre_min = 1 

            #Keep storing the maximum value
            cur_max = max(number, pre_min*number, prev_max*number)
            
            #Store the min value till meet the next -ve number in order to become the largest +ve number
            cur_min = min(number, pre_min*number, prev_max*number)
            
            #Update the pre_max and pre_min
            prev_max = cur_max
            pre_min = cur_min

            #Update the maxproduct if the new max value is found 
            maxproduct = max(maxproduct, cur_max)
        
        return maxproduct




def main() -> None: 
    
    input = [[2,3,-2,4],
             [-2,0,-1],
             [-3,-1,-1],
             [0,2],
             [3,-1,4],
             [2,-5,-2,-4,3],
             [-2,3,-4],
             [1,2,-1,-2,2,1,-2,1,4,-5,4],
             [1,0,-1,2,3,-5,-2]]
    output = [6,0,3,2,4,24,24,1280,60]

    # input = [[1,0,-1,2,3,-5,-2]]
    # output = [60]



    for index, nums in enumerate(input):
        print(f"The nums list is: {input[index]}")
        print(f"The calculated max_subarray: {Solution.maxproduct_subarray(nums)}")
        print(f"The expected max_subarray: {output[index]}")
        
    

if __name__ == "__main__":
    main()