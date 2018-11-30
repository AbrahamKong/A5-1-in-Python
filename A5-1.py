# A5/1 Cipher

# Get input
key = input("Please enter a random number: ")
type(key)

# Convert to Binary
key = format(key, '#064b')
# key = bin(key)
print("This is your number in binary: " + key)

key_x = key[2:21]
key_y = key[21:-25]
key_z = key[-25:]

print("X: " + key_x)
print("Y: " + key_y)
print("Z: " + key_z) 