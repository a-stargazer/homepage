pages = [
	{
		"filename": "./content/index.html",
		"output": "./docs/index.html",
		"title": "Home",
	},
	{
		"filename": "./content/about.html",
		"output": "./docs/about.html",
		"title": "About Me",
	},
	{
		"filename": "./content/projects.html",
		"output": "./docs/projects.html",
		"title": "My Projects",
	},
    {
		"filename": "./content/blog.html",
		"output": "./docs/blog.html",
		"title": "My Blog",
	},
]

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