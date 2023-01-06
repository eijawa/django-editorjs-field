import sys

# Only for testing and development purpose!
sys.path.append(".")

import pytest

from django_editorjs_field.tool import EditorJSTool as Tool


def test_simple_tool():
    t = Tool(
        name="Header",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )

    assert isinstance(t, Tool)


def test_tool_without_url():
    with pytest.raises(Exception):
        t = Tool(name="Header", template_name="tools/h.html")


def test_tool_with_none_url():
    with pytest.raises(Exception):
        t = Tool(name="Header", url=None, template_name="tools/h.html")


def test_tools_unique_set_with_same_name():
    h1 = Tool(
        name="Header",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )
    h2 = Tool(
        name="Header",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )
    h3 = Tool(
        name="Header",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )

    tools = list(set([h1, h2, h3]))

    assert len(tools) == 1


def test_tools_unique_set_with_different_names():
    h1 = Tool(
        name="Header",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )
    h2 = Tool(
        name="Header1",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )
    h3 = Tool(
        name="Header2",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )

    tools = list(set([h1, h2, h3]))

    assert len(tools) == 3


def test_tools_unique_set_with_same_name_different_class_name():
    h1 = Tool(
        name="Header",
        class_name="heading1",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )
    h2 = Tool(
        name="Header",
        class_name="heading2",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )
    h3 = Tool(
        name="Header",
        class_name="heading3",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )

    tools = list(set([h1, h2, h3]))

    assert len(tools) == 1


def test_tools_unique_set_with_different_name_same_class_name():
    h1 = Tool(
        name="Header",
        class_name="heading1",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )
    h2 = Tool(
        name="Header1",
        class_name="heading1",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )
    h3 = Tool(
        name="Header2",
        class_name="heading1",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )

    tools = list(set([h1, h2, h3]))

    assert len(tools) == 3


def test_outdated_tool():
    with pytest.raises(Exception):
        h1 = Tool(
            name="Header",
            class_name="heading1",
            url="//cdn.jsdelivr.net/npm/@editorjs/header@2.0.0",
            template_name="tools/h.html",
        )


def test_latest_tool():
    h1 = Tool(
        name="Header",
        class_name="heading1",
        url="//cdn.jsdelivr.net/npm/@editorjs/header",
        template_name="tools/h.html",
    )


def test_tool_url_with_different_version():
    h1 = Tool(
        name="Header",
        class_name="heading1",
        url="//cdn.jsdelivr.net/npm/@editorjs/header@2.6.0",
        template_name="tools/h.html",
        version="2.7.0",
    )

    assert h1.url == "https://cdn.jsdelivr.net/npm/@editorjs/header@2.7.0"
