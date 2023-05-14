'''
Write a function that given a list of strings and an input string will return True if you can create
the input string from the list of strings and will return False if you cannot create the string from
the list.
'''

def can_create(list_of_strings, input_string):
	possible_perms = []
	for i in range(0, len(list_of_strings)):
		for j in range(0, len(list_of_strings)):
			if(i!=j):
				possible_perms.append(list_of_strings[i]+list_of_strings[j])
	if input_string in possible_perms:
		return True
	else:
		return False

list_of_strings = ['back', 'end', 'front', 'tree']
print(can_create(list_of_strings, 'backend'))
print(can_create(list_of_strings, 'endfront'))
print(can_create(list_of_strings, 'frontyard'))