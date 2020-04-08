import glob
import os
from jinja2 import Template

def find_pages():
    pages = []
    all_content_docs = glob.glob("content/*.html")
    # create dictionary with input filepath, output filepath, and title
    for doc in all_content_docs:

    # define output dir path and filename
    	output_dir_path = "docs/"
    	file_name = os.path.basename(doc)

    	# remove extension to use filename as page title
        name_only, extension = os.path.splitext(file_name)
        print("name: ", name_only, ", extension: ", extension)

        page = {
            "input": doc, # content/index.html
            "output": output_dir_path + file_name, # docs/index.html
            "file_name": file_name, # ex.) index.html
            "title": "Home" if name_only == "index", 

            # or 
			# full_page = str("docs/" + name_only + ".html")
			# file_of_full_page = str(name_only + ".html")
			# pages.append(file_of_full_page)

        }

        pages.append(page)


# # pages list 

# pages = []
# all_html_files = glob.glob("content/*.html")
# print(all_html_files)

# # main
# def main():
#     index_html = open("./content/index.html").read()
#     template_html = open("./templates/base.html").read()
#     template = Template(template_html)
#     for page in all_html_files:
#     	# generate docs()
#     	content = open(page).read()

# # generate html pages from files in "content/"
#     page = "content/*.html"
#     page_name = os.path.basename(page)
    # name_only, extension = os.path.splitext(page_name)
#     full_page = str("docs/" + name_only + ".html")
#     file_of_full_page = str(name_only + ".html")

#     pages.append(file_of_full_page)

# # file name: file of full page
# final_html = template.render(
#         content = html,
# 	    title = title,
# 	    pages = pages,
# 	    file_name = full_page,
# )

# open(str("docs/" + name_only + ".html"), "w+").write(final_html)

# print(pages)

# invoking main
main()
print("the site has been built")