#!/usr/bin/env python3
import re
from sys import argv
from optparse import OptionParser

comment_symbols = {'cpp': '//', 'py': '#', 'rb': '#', 'tex': '%'}

usage = "usage: %prog [options] FILE"
parser = OptionParser(usage=usage)
parser.add_option("-o", "--output-directory", dest="output_directory", default=".", help="write snippets to DIR", metavar="DIR")
(options, args) = parser.parse_args()

filepath = args[0]
filename = filepath.split("/")[-1]
basename, extension = filename.split(".")
comment_symbol = comment_symbols[extension]


# define states
RECORDING = 1
SEARCHING = 0

# define initial state
state = SEARCHING
region_name = ""
region_contents = []

with open(filepath) as f:
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
				snippet_path = "%s/%s.snippet.%s" % (options.output_directory, region_name, extension)
				with open(snippet_path, "w") as g:
					for snipped_line in region_contents:
						g.write(snipped_line)
				state = SEARCHING
				# @endregion
			else:
				region_contents.append(line)

