from django.utils.safestring import mark_safe

from .field import EditorJSField


def render(obj) -> str:
    field = None
    for f in obj._meta.get_fields():
        if isinstance(f, EditorJSField):
            field = f
            break

    if not field:
        raise AttributeError("Field of type EditorJSField not found.")

    html = ""
    for block in getattr(obj, field.attname)["blocks"]:
        html += field.tools[block["type"]].render(block["data"])

    return mark_safe(html)


def render_multiple(objs) -> dict[str, str]:
    raise NotImplementedError()
