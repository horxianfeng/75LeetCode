class Solution (object):

    def most_water (height: list[int]) -> int:
        most_water = 0
        for i, vertical in enumerate(height):
            l_start = i
            l_end = len(height)-1
            h_start = height[i]
            h_end = height[l_end]
            while i<l_end:
                l = l_end-l_start
                h = min(h_start,h_end)
                vol = l * h
                if vol > most_water: most_water=vol
                l_end-=1
                h_end = height[l_end]
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