class Solution (object):

    def bit_sum (nums: list[int]) -> int:
        a = nums[0]
        b = nums[1]

        bitshorterner = 0xffffffff
        
        while (b & bitshorterner)>0:
            carry = (a & b)<<1
            add = a ^ b
            

            a = add
            b = carry


        
        return (add & bitshorterner) if b > 0 else a


def main() -> None: 
    
    input = [[1,2],
           [2,3],
           [100,10],
           [-1,1],
           [5,0]]
    output = [3,5,110,0,5]

    for index, nums in enumerate(input):
        print(f"The nums list is: {input[index]}")
        print(f"The calculated product list: {Solution.bit_sum(nums)}")
        print(f"The expected product list: {output[index]}")
        
    

if __name__ == "__main__":
    main()