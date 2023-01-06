# Django EditorJS Field
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
> Django >4.* (Not tested in old versions)

An EditorJS Field with dependency injection of tools support for Django >4.*

## Features

- [x] Dependency injection for tools
- [x] Templatetag support
- [x] All EditorJS configuration supported
- [x] Without custom backend
- [x] Customized editor in admin
- [x] [Debug support](#about-debug-support)

## Installation and Usage

### Installation
> Some day it will be *django-editorjs-field*...

Install package via `pip`:

```
pip install django-editorjs-field-next
```

Add package to `INSTALLED_APPS`:

```
INSTALLED_APPS = [
    ...
    "django_editorjs_field"
]
```

### Usage

>**Note!**<br>If you will not provide configuration, you will have only default Paragraph Tool.

Example of field configuration:

```
from django_editorjs_field.tool import EditorJSTool as Tool


EditorJSField(
    tools=[
        Tool(name="Header", url="//cdn.jsdelivr.net/npm/@editorjs/header", template_name="tools/h.html"),
        Tool(
            name="Code",
            url="https://cdn.jsdelivr.net/npm/@editorjs/code@2.8.0",
            class_name="CodeTool",
            template_name="tools/code.html"
        )
    ]
)
```

**Any** kwargs that you add will pass to EditorJS configuration. For example, if you want `autofocus`, `placeholder` and `i18n`, you just add to field arguments:

```
autofocus=False,
placeholder="EditorJSPlaceholder",
i18n={
    "messages": {
        "toolNames": {
            "Heading": "Заголовок"
        }
    }
}
```

**templatetag**

Example of templatetag:

```
{% load editorjs %}

{% for article in articles_list %}
    <div>
        <h3>{{ article.title }}</h3>
        {% render article %}
    </div>
{% endfor %}
```

## Tools

All tools (plugins) are independent objects. Tool constructor define as:

```
def __init__(self, name: str, url: str, template_name: str, class_name: str | None = None, **kwargs):
    """
        An EditorJSTool constructor

        ...

        Attributes
        ==========
        name : str
            Must be unique!
            A name of a Tool. Used as a type in EditorJS.
        url : str
            A URL or Path to JS-file of Tool.
        template_name : str
            A Path to template for output rendering.
        class_name : str | None
            Name attribute is used by default.
            A class name of Tool, which JS need to call constructor for.
    """
```

### Override Paragraph Tool

In order to override Paragraph Tool you need to pass it as a tool into field. Example:

```
from django_editorjs_field.tool import EditorJSTool as Tool


EditorJSField(
    tools=[
        Tool(
            name="paragraph",
            url="//cdn.jsdelivr.net/npm/@editorjs/paragraph@2.0.2",
            class_name="Paragraph",
            template_name="tools/p.html"
        )
        Tool(name="Header", url="//cdn.jsdelivr.net/npm/@editorjs/header", template_name="tools/h.html"),
    ],
    ...
)
```

## License
MIT

## Authors
Evgeniy Gribanov

## FAQ
### About Debug support
If you run Django in DEBUG mode, your EditorJS inherit this mode too. It means that you will have usefull messages in your browser console about Editor Configuration and work.