# Import math Library
import math

class Solution (object):

    def count_bits (num: int) -> list[int]:
        
        count_bits = [0]*(num+1) 
        sig_bit_val = 1
        
        for i in range( num+1 ):
            
            if i == 0: continue
            
            if i == sig_bit_val*2:
                sig_bit_val = i
            count_bits[i] = 1 + count_bits[i-sig_bit_val]              
      
        return count_bits
    
def main() -> None: 
    
    input = [2, 5] 
    output = [[0,1,1],
              [0,1,1,2,1,2]]

    for index, nums in enumerate(input):
        print(f"The input: {input[index]}")
        print(f"The output: {Solution.count_bits(nums)}")
        print(f"The expected output: {output[index]}")
        
    

if __name__ == "__main__":
    main()