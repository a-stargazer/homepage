# glob

import glob
all_html_files = glob.glob("content/*.html")
print(all_html_files)

# output: ['content/index.html', 'content/projects.html', 'content/about.html', 'content/blog.html']

# -------------------------------------------------

# os

import os

file_path = "content/blog.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)

# output: 
# blog.html
# blog


# -------------------------------------------------

# pages list

pages = []
pages.append({
	"filename": "content/index.html",
	"title": "Index",
	"output": "docs/index.html",
})
print(pages)

# output:
# [{'filename': 'content/index.html', 'title': 'Index', 'output': 'docs/index.html'}]

# -------------------------------------------------

# loop through list
def main():
	for page in pages:
		file_name = page["filename"]
		page_output = page["output"]
		page_title = page["title"]
		page_content = open(file_name).read()
		combined_page = apply_template(page_content, page_title)
		final_output = final_page_output(page_output, combined_page)

# replace {{content}} and {{title}} placeholders
def apply_template(page_content, page_title):
	template = open("./templates/base.html").read()
	finished_template_with_content = template.replace("{{content}}", page_content)
	combined_page = finished_template_with_content.replace("{{title}}", page_title)
	return combined_page

# output in the correct directory (/docs)
def final_page_output(page_output, combined_page):
	open(page_output, "w+").write(combined_page)

# invoking main
main()
print("the site has been built")