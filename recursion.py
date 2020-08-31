nested_lists = [[["spam"],["eggs"],["ham"]], ["banana", "apple", "peach", ["fuji", "grannysmith"]]]

flat_list = []

def list_opener(some_list):
  for items in some_list:
    if type(items) == list:         
      list_opener(items) #calling itself recursively
    else:
      flat_list.append(items)

list_opener(nested_lists)

print(flat_list)
