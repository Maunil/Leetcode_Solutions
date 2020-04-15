class Solution:
    def help(self, A, prefix, suffix, result):
         # Base case 
        if len(suffix) == 0:
            result.append(list(prefix))
            return 
    
        for i in range(len(suffix)):
            prefix.append(suffix[i])
            self.help(A, prefix, suffix[0:i] + suffix[i+1:] , result) 
            prefix.pop() 

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.help(nums, [], nums, result)
        return result
        

'''
For string 

def help(A, prefix, suffix, result):
  # Base case 
  if len(suffix) == 0:
    result.append((prefix))
    return 
  
  for i in range(len(suffix)):
    help(A, prefix + suffix[i] , suffix[0:i] + suffix[i+1:] , result) 


def main():
  a = "123"
  result = []
  help(a, "", a, result)
  return result

print (main())

##Execution 
#F ("" , "ABC") -> F("A" , "BC") -> F("AB" , "C") -> F("ABC", "")
#                                -> F("AC", "B")
                          '''
