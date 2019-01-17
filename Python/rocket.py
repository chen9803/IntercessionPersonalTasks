# 
"""
This section should see you print out a rocket ship to the console.  This is section
is meant to teach basic string concatination and adding human readability to output.

How to Run: python rocket.py

Desired Output:

   *
  * *
 *   *
*     *
=======
|     |
|     |
|     |
|     |
=======
=======
|     |
|     |
|     |
|     |
=======
=======
|     |
|     |
|     |
|     |
=======
   *
  * *
 *   *
*     *

"""

def main():
	rocket = ""

	rocket += rocket_head_and_tail()
	rocket += rocket_body()
	rocket += rocket_body()
	rocket += rocket_body()
	rocket += rocket_head_and_tail()

	print(rocket)

def rocket_head_and_tail():
	return "\n   *\n  * *\n *   *\n*     *"

def rocket_body():
	# TODO: Add code here.
	return "\n|     |\n|     |\n|     |\n|     |\n======="

if __name__ == '__main__':
    main()