import utils 
import sys

# an array for command line arguments
print("This is argv: ", sys.argv)
command = sys.argv[1]
print(command)

if command == "build":
	print("Build was specified")
	# todo something here...
elif command == "new":
	print("New page was specified")
	# todo something more here!
else:
	print("Please specify 'build' or 'new'")

def main():

    pages = find_pages()
    create_pages(pages)

    print("the site has been successfully built")   