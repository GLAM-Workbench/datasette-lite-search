from datasette import hookimpl
from datasette.utils import is_url
from markupsafe import Markup, escape


@hookimpl
def render_cell(row, value):
    if not isinstance(value, str):
        return
    output = []
    for line in value.split("|"):
        stripped = line.strip()
        if is_url(stripped):
            output.append('<a href="{url}">{url}</a>'.format(url=escape(stripped)))
    if output:
        return Markup(" | ".join(output))
    else:
        # Return None if no urls so that non-url cells will be truncated according to the truncate_cells_html setting
        return None

