# Import the libraries select, sys
import sys
import select

# Print the question or any line you want
print("Who is your best friend?")
print("\nYou have ten seconds to answer!")

# Return 3 new list containing subset of content
# with timeout after which statement returns
a, b, c = select.select([sys.stdin], [], [], 10)

# Run if statement till the time is running
if (a):

	# Read the input and print result
	print("\nYou stated your best friend name as: ",
		sys.stdin.readline().strip())

# Run else when time is over
else:

	# Print the timeout statement
	print("\nYour time got over")

