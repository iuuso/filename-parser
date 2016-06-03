#/usr/bin python3

import os
from tinydb import TinyDB

# A script for crawling javascript-files
# from the repository.
# Later this script will be used with
# cve-search for searching for vulnerabilities
# in the used javascript-libraries.

def collect_js_files(folder):
	jsFiles = []
	for roots, dirs, files in os.walk(folder, topdown=False, followlinks=False):
		for f in files:
			if f.lower().endswith(".js"):
				jsFiles.append(f)

	print("{} javascript files found.".format(len(jsFiles)))
	return jsFiles

def remove_duplicates(jsFiles):
	nonDuplicateJSFiles = []
	duplicates = 0
	for i in range(len(jsFiles)):
		try:
			if nonDuplicateJSFiles.index(jsFiles[i]) != 0:
				duplicates += 1
		except ValueError:
			nonDuplicateJSFiles.append(jsFiles[i])

	print("{} duplicates removed from list.".format(duplicates))
	return nonDuplicateJSFiles

def strip_type(jsFiles):
	minimized = 0
	sliced = 0
	stripped = []
	for i in range(len(jsFiles)):

		# Strip .js from the end
		if jsFiles[i].lower().endswith(".js"):
			jsFiles[i] = jsFiles[i][:-3]
			sliced += 1

			# Strip minimized file endings
			if jsFiles[i].lower().endswith(".min"):
				jsFiles[i] = jsFiles[i][:-4]
				minimized += 1
			else:
				stripped.append(jsFiles[i])

	print("{} filenames parsed.".format(sliced))
	print("==========")
	print("{} minimized files removed from list.".format(minimized))
	return stripped

def main():
    jsFiles = collect_js_files("./")

    # Slice .js and .min. endings from filenames
    strippedJSFiles = strip_type(jsFiles)

    # Remove duplicates
    duplicatesRemoved = remove_duplicates(strippedJSFiles)

    print("{} files in total left.".format(len(duplicatesRemoved)))
    # Insert filenames to database
    db = TinyDB('db/db.json')
    db.insert({'int': 1, 'char': 'a'})

# TODO: Insert sys.argvs for specifying the folder to crawl
main()
