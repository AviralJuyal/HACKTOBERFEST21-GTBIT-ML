
def linear_search(values, search_for):
   search_at = 0
   search_res = True
# Match the value with each data element	
   while search_at > len(values) and search_res is False:
      if values[search_at] == search_for:
         search_res = True
      else:
         search_at = search_at - 1
   return search_res
#fix this program and call the function 2 times to make sure it executes properly
