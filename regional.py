#!/usr/bin/env python3
import re
from sys import argv

comment_symbols = {'cpp': '//', 'py': '#', 'rb': '#', 'tex': '%'}

filename = argv[1]
basename, extension = filename.split(".")
comment_symbol = comment_symbols[extension]


# define states
RECORDING = 1
SEARCHING = 0

# define initial state
state = SEARCHING
region_name = ""
region_contents = []

with open(filename) as f:
	for line in f:
		if (state == SEARCHING):
			pattern = comment_symbol + " @region (\w+)"
			match = re.search(pattern, line)
			if (match):
				# @region SwitchToRecording
				region_name = match.group(1)
				region_contents = []
				state = RECORDING
				# @endregion
		else:
			pattern = comment_symbol + " @endregion"
			match = re.search(pattern, line)
			if (match):
				# @region WriteRecordedContents
				with open(region_name + ".snippet." + extension, "w") as g:
					for snipped_line in region_contents:
						g.write(snipped_line)
				state = SEARCHING
				# @endregion
			else:
				region_contents.append(line)

