import markdown
import os
import shutil

base_path = os.path.join("C:\\Documents and Settings\\Administrador\\DATOS\\documentacion_mierdas")
base_path_html = base_path + '-html'
project_path = os.path.join("C:\\Documents and Settings\\Administrador\\DATOS\\scripts\\python\\md_renderer")
# unix_type_project_path = project_path.replace('\\', '/')
html_header = '<html><head><meta charset="utf-8"><link rel="stylesheet" type="text/css" href="./style.css"></head><body><div id="main">'
html_footer = '</div></body></html>'

os.chdir(base_path)

if not os.path.exists(base_path_html):
    os.mkdir(base_path_html)

for path, dirs, files in os.walk("."):
    dir_html = os.path.join(base_path_html, path)
    if not os.path.exists(dir_html):
        os.mkdir(dir_html)
        
    # copy the css to every directory
    shutil.copyfile(os.path.join(project_path, 'style.css'), os.path.join(dir_html, 'style.css'))
       
    for filename in files:
        if filename.endswith(('md')):
            file_without_ext, ext = os.path.splitext(filename)
            rendered_file = dir_html + '\\' + file_without_ext + '.html'
            file_with_rel_path = os.path.join(path, filename)
            html =  markdown.markdownFromFile(file_with_rel_path, output=rendered_file)

            # add header to html file
            with open(rendered_file, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(html_header.rstrip('\r\n') + '\n' + content)

            # add footer to html file
            with open(rendered_file, 'a') as f:
                f.write(html_footer.rstrip('\r\n') + '\n')

