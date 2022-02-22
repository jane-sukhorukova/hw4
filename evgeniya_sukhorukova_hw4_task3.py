shop_list = [item for item in input("Enter the list items : ").split()]
longest_item = max(shop_list, key=len)
result = 'The longest item is {} and its length is {} symbols'.format(longest_item, len(longest_item))
print(result)
