# template, top and bottom 
top = open("templates/top.html").read()
bottom = open("templates/bottom.html").read()

content = open("content/index.html").read()

# index 
index_html = top + content + bottom
open("docs/index.html", "w+").write(index_html)

# about 
content = open('content/about.html').read()
about_html = top + content + bottom
open('docs/about.html', 'w+').write(about_html)

# projects
content = open('content/projects.html').read()
projects_html = top + content + bottom
open('docs/projects.html', 'w+').write(projects_html)

# blog
content = open('content/blog.html').read()
blog_html = top + content + bottom
open('docs/blog.html', 'w+').write(blog_html)
