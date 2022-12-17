package policy

# user-role assignments
user_roles := {"joe": ["admin", "manager"]}

default allow = false

allow {
	# lookup the list of roles for the user
	roles := user_roles[input.username]
    # for each role
    role := roles[_]
    # check if the user has the given role
	role == input.role
}