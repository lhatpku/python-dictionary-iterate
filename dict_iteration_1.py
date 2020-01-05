# Example Dictionary

example = {
    'color': 'red',
    'fruit': 'apple',
    'species': 'dog',
}

# example key-value access
example['color']

# Use below to inspect your local environment
# Notice that this is a dictionary!
locals()

# Can't use un-hashable types as keys
# Should throw TypeError!
un_hashable = {[1, 2, 3]: "HI!"}

# Vice-versa is fine
string_key = {"HI!": [1, 2, 3]}

# Use hashable analogues of un-hashable types
# i.e. tuple for list, etc.
with_hashable = {(1, 2, 3): "HI!"}



