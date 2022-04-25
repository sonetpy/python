class Instagram:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.follower += 1
        self.following += 1

user_1 = Instagram('001', "abhinav")
user_2 = Instagram('002', "surabhi")
print("{} is going to follow {}".format(user_1.username, user_2.username))

user_1.follow(user_2)
#print(user_1.follower)
#print(user_1.following)

user_3 = Instagram('003', "samsung")
user_3.follow(user_2)
print(user_3.follower)
print(user_3.following)
