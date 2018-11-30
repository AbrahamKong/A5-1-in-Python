# A5/1 Cipher

import re
import collections


# def main(args):
	# Get input
key = input("Please enter a random number: ")
type(key)

print("The number will be used to generate the 64-bit keystream")

# Convert to Binary
key = format(key, '#064b')
# key = bin(key)
print("This is your number in binary: " + key)

# Create X, Y, and Z registers
key_x = key[2:21]
key_y = key[21:-25]
key_z = key[-25:]

# Print out to confirm the 3 registers
print("X: " + key_x)
print("Y: " + key_y)
print("Z: " + key_z)

# majority function
def maj(key_x, key_y, key_z):
	x = key_x[7] # Get the 8th bit
	y = key_y[9] # Get the 10th bit
	z = key_z[9] # Get the 10th bit
	vote = collections.Counter(x = x, y = y, z = z) #Counter for Clocking bits
	return max(vote[0], vote[1]) # Return the majority vote

print "maj vote: ", maj(key_x, key_y, key_z)

def step_x:
	