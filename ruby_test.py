import os

def snippet_exists_test():
	os.system("python3 regional.py example.rb")
	assert(os.path.isfile("ReopenExistingClass.snippet.rb"))

def extracts_correct_region_test():
	os.system("python3 regional.py example.rb")
	expected_contents = "class Doofus\n\tdef self.greet_differently\n\t\tgreet\n\t\tputs \"... my friend\"\n\tend\nend\n"
	with open("ReopenExistingClass.snippet.rb") as f:
		actual_contents = "".join(f.readlines())
	assert(expected_contents == actual_contents)
