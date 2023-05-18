def get_standard_template_paths(resource_name):
    class tmpl:
        index = f"{resource_name}/index.jinja2"
        edit = f"{resource_name}/edit.jinja2"
        show = f"{resource_name}/show.jinja2"
        new = f"{resource_name}/new.jinja2"
    
    return tmpl
