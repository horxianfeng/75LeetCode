class Solution (object):

    def most_water (height: list[int]) -> int:
        most_water = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            most_water = max(most_water, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return most_water





def main() -> None: 
    
    input = [[1,8,6,2,5,4,8,3,7],
           [1,1],
           [1,2,5,4,3,100,10]]
    output = [49,1,300]

    for index, nums in enumerate(input):
        print(f"The nums list is: {input[index]}")
        print(f"The calculated product list: {Solution.most_water(nums)}")
        print(f"The expected product list: {output[index]}")
        
    

if __name__ == "__main__":
    main()