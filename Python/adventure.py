
"""
This section will be about accessing information inside json files.

How to Run: python adventure.py

Desired Output:

	Contents of example.json should be outputted with new fields added.

"""

import json

def main():
	data = ""
	with open("example.json") as in_file:
		data = json.load(in_file)

	# TODO: Add a field with the key "Description" with a data inside example.json
	# TODO: Output the Description to the console by formatting it with base_string (you will need to edit it)
	base_string = "{0} has {1} HP. Described as {2}"

	for key in data["Actors"]:
		output_string = base_string.format(
				key, 
				data["Actors"][key]["HP"],
				data["Actors"][key]["Description"])
		print(output_string)

	# TODO: Output Weapons with Damage and Description
	base_string = "{0} has {1} strength. Its description is {2}"

	for key in data["Weapons"]:
		output_string = base_string.format(
				key, 
				data["Weapons"][key]["Damage"],
				data["Weapons"][key]["Description"])
		print(output_string)
	# TODO: Add a new data category along side Actors and Weapons, put in any relevant data.
		baseString = "Jordan is sad because he is {0} and {1}. There are probably other reasons but {2}"

	for key in data["Why Jordan is so sad"]:
		outputString = baseString.format(
				key, 
				data["Why Jordan is so sad"][key]["Your Lie in April"],
				data["Why Jordan is so sad"][key]["Probably something else"])
		print(outputString)

if __name__ == '__main__':
    main()