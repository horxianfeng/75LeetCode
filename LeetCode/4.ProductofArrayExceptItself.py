class Solution (object):
    
    def product_except_itself(nums: list[int]) -> list:

        product = []        
        
        for product_index in range(len(nums)):
            product.append(1)
            for nums_index in range (len(nums)):
                if nums_index != product_index:
                    product[product_index] *= nums[nums_index]

        return product

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