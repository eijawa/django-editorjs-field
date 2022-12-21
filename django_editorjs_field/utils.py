from django.utils.safestring import mark_safe

from .field import EditorJSField


def render(obj: EditorJSField) -> str:
    """
    Method accepts an object and return it's EditorJSField HTML corresponding representation.

    ...

    Attributes
    ==========
    obj : django.models.Model
        django.models.Model instance.

    Raises
    ======
    AttributeError
        Field of type EditorJSField is not presented.
    """

    field = None

    for f in obj._meta.get_fields():
        if isinstance(f, EditorJSField):
            field = f
            break

    if not field:
        raise AttributeError("Field of type EditorJSField is not presented.")

    html = ""
    for block in getattr(obj, field.attname)["blocks"]:
        html += field.tools[block["type"]].render(block["data"])

    return mark_safe(html)
