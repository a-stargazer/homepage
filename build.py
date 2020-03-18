# templates/top.html + content/index.html + templates/bottom.html > docs/index.html
# templates/top.html + content/about.html + templates/bottom.html > docs/about.html
# templates/top.html + content/projects.html + templates/bottom.html > docs/projects.html
# templates/top.html + content/blog.html + templates/bottom.html > docs/blog.html

# template, top and bottom 
top = open("templates/top.html").read()
bottom = open("templates/bottom.html").read()

content = open("content/index.html").read()

index_html = top + content + bottom
open("docs/index.html", "w+").write(index_html)

# about 

content = open('content/about.html').read()
about_html = top + content + bottom
open('docs/about.html', 'w+').write(about_html)

# projects

content = open('content/projects.html').read()
project_html = top + content + bottom
open('docs/projects.html', 'w+').write(projects_html)

# blog

content = open('content/blog.html').read()
blog_html = top + content + bottom
open('docs/blog.html', 'w+').write(blog_html)
