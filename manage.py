import utils 
import sys

def main():

    try:
	    command = sys.argv[1]

	    # build the site 
	    if command == "build":
		    pages = utils.find_pages()
		    utils.create_pages(pages)
		    print("Build was specified")

	    # create "content/new_content_page.html"
	    elif command == "new":
		    utils.new_page()
		    print("New page was specified")

	    else:
		    print("Please specify 'build' or 'new'")

    except:
        print("""
Usage:
	Rebuild site:    python manage.py build
	Create new page: python manage.py new
	""")

# invoke main
main()

