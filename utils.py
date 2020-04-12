import glob
import os
from jinja2 import Template

def find_pages():
    pages = []
    all_html_pages = glob.glob("content/*.html") 

# create html pages from content files
    for page in all_html_pages:

# return basename of file, ex) if "/content/index.html" --> output: "index.html")
        file_name = os.path.basename(page) 
        name_only, extension = os.path.splitext(file_name) 
 
        full_page = "docs/" + name_only + ".html"
        full_page_file = "content/" + name_only + ".html"

        pages.append({
            "file_name": full_page_file,
            "output": "docs/" + file_name,
            "input": page,
            "title": "home" if name_only == "index" else name_only, 
            "file_name": file_name, 
        })

    return pages

# create pages using base.html
def create_pages(pages):

    template_html = open("./templates/base.html").read()
    template = Template(template_html)

    for page in pages: 
        content_html = open(page["input"]).read()
        
        html_output = template.render(
            title = page["title"],
            content = content_html,
            pages = pages,
        )

        open(page["output"], "w+").write(html_output)

# create a new page if "python3 manage.py new" is run
def new_page(filename="new_content_page.html"):

    message = """
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <title>Page Title</title>
            <meta charset="utf-8">
          </head>
          <body>
            <h1>New Content!</h1>
            <p>New content...</p>
        </html>
        """

    open("content/" + filename, "w+").write(message)