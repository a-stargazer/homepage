import glob
import os
from jinja2 import Template

# pages list 

pages = []
all_html_pages = []
all_html_pages = glob.glob("content/*.html")
print(all_html_pages)

# main
def main():
    index_html = open("./content/index.html").read()
    template_html = open("./templates/base.html").read()
    template = Template(template_html)
    for page in all_html_files:
    	# generate docs()
    	content = open(page).read()

# generate html pages from files in "content/"
    page = "content/*.html"
    page_name = os.path.basename(page)
    name_only, extension = os.path.splitext(page_name)
    full_page = str("docs/" + name_only + ".html")
    file_of_full_page = str(name_only + ".html")

    pages.append(file_of_full_page)

# file name: file of full page
final_html = template.render(
        content = html,
	    title = title,
	    pages = pages,
	    file_name = full_page,
)

open(str("docs/" + name_only + ".html"), "w+").write(final_html)

print(pages)

# ---------- Phase 3 ----------

# {% for page in pages %}
#     <a href="{{page.output_filename}}">{{page.title}}</a>
# {% endfor %}

# invoking main
main()
print("the site has been built")