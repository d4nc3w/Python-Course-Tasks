
# 1st approach:
email1 = "s28113@pjwstk.edu.pl"
index1 = email1.index("@")
username = email1[:index1]
domain = email1[index1 + 1:]
print(f"Your username is {username} and your domain is {domain}")

#2nd approach:
email2 = "piotr@dancewicz.pl"
username = email2[:email2.index("@")]
domain = email2[email2.index("@") + 1: ]
print(f"Your username is {username} and your domain is {domain}")
