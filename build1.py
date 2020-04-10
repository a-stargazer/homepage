import glob
import os
from jinja2 import Template

def main():

    pages = find_pages()
    create_pages(pages)

    print("the site has been successfully built")    

# create pages list
def find_pages():
    pages = []
    all_html_pages = glob.glob("content/*.html") 

# create html pages from content files
    for page in all_html_pages:

# return basename of file, ex) if "/content/index.html" --> output: "index.html")
        page_name = os.path.basename(page) 
        name_only, extension = os.path.splitext(page_name) 
        full_page = str("docs/" + name_only + ".html")
        full_page_file = str(name_only + ".html")

        pages.append({
            "file_name": page,
            "output": full_page,
            "title": name_only,
        })

    print("pages: ", pages)

# create pages using base.html
def create_pages(pages):
    template_html = open("./templates/base.html").read()
    template = Template(template_html)

    # create pages with Jinja and generate docs()

    for page in pages:
        html_output = template.render(
            title = page["title"],
            content = open(page).read(),
            page = pages,
            file_name = full_page,
        )

        open(str("docs/" + name_only + ".html"), "w+").write(html_output)


# invoke main

main()
print("the site has been built")