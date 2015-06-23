import markdown
import os
import shutil

base_path = os.path.join("C:\\Documents and Settings\\Administrador\\DATOS\\documentacion_mierdas")
base_path_html = base_path + '-html'
project_path = os.path.join("C:\\Documents and Settings\\Administrador\\DATOS\\scripts\\python\\md_renderer")
# unix_type_project_path = project_path.replace('\\', '/')
html_header = '<head><meta charset="utf-8"><link rel="stylesheet" type="text/css" href="./style.css"></head>'

os.chdir(base_path)

if not os.path.exists(base_path_html):
    print("No existe", base_path_html, "creando ...")
    os.mkdir(base_path_html)

shutil.copyfile(os.path.join(project_path, 'style.css'), os.path.join(base_path_html, 'style.css'))

for path, dirs, files in os.walk("."):
    dir_html = os.path.join(base_path_html, path)
    if not os.path.exists(dir_html):
        print("no existe:", dir_html, " creando ...")
        os.mkdir(dir_html)

    for filename in files:
        if filename.endswith(('md')):
            file_without_ext, ext = os.path.splitext(filename)
            rendered_file = dir_html + '\\' + file_without_ext + '.html'
            html =  markdown.markdownFromFile(filename, output=rendered_file)

            # add header to html file
            with open(rendered_file, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(html_header.rstrip('\r\n') + '\n' + content)
