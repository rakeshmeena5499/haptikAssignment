'''
Write a function that reads from the file and returns the 3 most active users in the conversation.
'''

def most_active_user(chats_file):
	users = {}
	with open(chats_file, 'r') as file:
		for line in file:
			if line.split(':')[0] in users:
				users[line.split(':')[0]] += 1
			else:
				users[line.split(':')[0]] = 1

	sorted_dict = dict(sorted(users.items(), key=lambda x: x[1], reverse=True))
	ans = [user[1:-1] for user in list(sorted_dict)[:3]]
	return ans

print("Most Active Users from the given group chat are:", most_active_user('chats.txt'))