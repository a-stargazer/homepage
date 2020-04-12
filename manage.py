import utils 
import sys

def main():

    command = sys.argv[1]

    # build the site 
    if command == "build":
        pages = utils.find_pages()
        utils.create_pages(pages)
        print("Build was specified")

    # create content/new_content_page.html 
    elif command == "new":
        utils.new_page()
        print("New page was specified")

    # prints out commands to either rebuild site or create new page
    elif command == "help":
        print("""
    Example commands:
            Rebuild site:    python manage.py build
            Create new page: python manage.py new
        """)

    else:
            print("Please specify 'build' or 'new'")

# invoke main
main()

