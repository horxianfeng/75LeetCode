class Solution (object):

    def hamming_weight (num: str) -> int:
        
        num = int(num, 2)
        num_of_one = 0
        print(num)

        while num != 0:
            if num % 2 == 1: num_of_one += 1
            num = num >> 1
      
        return num_of_one
    
def main() -> None: 
    
    input = ['00000000000000000000000000001011',
             '00000000000000000000000010000000',
             '11111111111111111111111111111101']
    output = [3,1,31]

    for index, nums in enumerate(input):
        print(f"The input: {input[index]}")
        print(f"The output: {Solution.hamming_weight(nums)}")
        print(f"The expected output: {output[index]}")
        
    

if __name__ == "__main__":
    main()