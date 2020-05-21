# Jay shree satimaa 
final_edit_str = ""
least_edit_count  = float("inf")

def help(source, target, ans, edits):  
  # Recursion break 
  global least_edit_count 
  global final_edit_str     
  
  if edits > least_edit_count:
    return 
  
  if len(target) == 0 and len(source) == 0: 
    if edits < least_edit_count:
      final_edit_str = ans 
      least_edit_count = edits 
    return 
  
  if len(target) == 0 and len(source) > 0:
    help(source[1:], target[:], ans + "-" + str(source[0]), edits + 1)   
  elif len(source) == 0 and len(target) > 0:
    help(source[:], target[1:], ans + "+" + str(target[0]), edits + 1)   
  elif source[0] == target[0]:
    help(source[1:], target[1:], ans+ str(source[0]), edits)
  else:    
    help(source[1:], target[:], ans + "-" + str(source[0]), edits + 1)
    help(source[:], target[1:], ans + "+" + str(target[0]), edits + 1)
        
def diffBetweenTwoStrings(source, target):
  """
  @param source: str
  @param target: str
  @return: str[]
  """
  print (source)
  print (target)
  help(source, target, "", 0)
  return  final_edit_str.split("")
  
  