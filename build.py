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

# # loop through list
def main():
	for page in pages:
		file_name = page["filename"]
		page_output = page["output"]
		page_title = page["title"]
		page_content = open(file_name).read()
		combined_page = apply_template(page_content, page_title)
		final_output = final_page_output(page_output, combined_page)

# # replace {{content}} with actual page content to base.html
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

# --------------------------------------------------------------------------------
    
# Phase 3: String replacement templating
# Read base.html
# template = open("./templates/base.html").read()

# # index HTML page
# index_content = open("content/index.html").read()
# finished_index_page = template.replace("{{content}}", index_content)
# open("docs/index.html", "w+").write(finished_index_page)

# # about HTML page
# about_content = open("content/about.html").read()
# finished_about_page = template.replace("{{content}}", about_content)
# open("docs/about.html", "w+").write(finished_about_page)

# # projects HTML page
# projects_content = open("content/projects.html").read()
# finished_projects_page = template.replace("{{content}}", projects_content)
# open("docs/projects.html", "w+").write(finished_projects_page)

# # blog HTML page
# blog_content = open("content/blog.html").read()
# finished_blog_page = template.replace("{{content}}", blog_content)
# open("docs/blog.html", "w+").write(finished_blog_page)

		# content = open("./docs/index.html")
		# resulting_html_for_index = apply_template(content)