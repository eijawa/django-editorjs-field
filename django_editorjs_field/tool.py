import urllib.request
import urllib.error
from urllib.parse import urlparse

from django.template.loader import render_to_string
from django.contrib.staticfiles import finders as static_finders


class EditorJSTool(object):
    """
    A class representing a EditorJS Tool (Plugin).

    ...

    Attributes
    ----------
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
    version : str | None
        Required plugin version.

    Properties
    ----------
    config : dict
        Read-only.
        A Tool configuration dictionary property.

    Methods
    -------
    render() -> str:
        Render Tool with appropriate template into HTML string.
    """

    def __init__(
        self,
        name: str,
        url: str,
        template_name: str,
        class_name: str | None = None,
        version: str | None = None,
        **kwargs
    ):
        """
        An EditorJSTool constructor

        ...

        Attributes
        ----------
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
        version : str | None
            Required plugin version.
        """

        self.name = name
        self.template_name = template_name
        self.version = version

        self.url = self.__define_url(url)

        self.class_name = name

        if class_name:
            self.class_name = class_name

        self._config = {"class": self.class_name, **kwargs}

    @property
    def config(self):
        """
        Read-only.
        A Tool configuration dictionary property.
        """

        return self._config

    def render(self, data: str) -> str:
        """Render Tool with appropriate template into HTML string."""

        return render_to_string(self.template_name, data)

    def __define_url(self, url: str) -> str:
        if not url:
            raise Exception("URL is not specified!")

        if url.startswith("//"):
            url = "https:" + url

        parsed_url = urlparse(url)
        if all([parsed_url.scheme, parsed_url.netloc]):
            # It's not a file, so we can apply version to it
            if self.version:
                splits = url.split("@")
                if len(splits) == 2:
                    _url = splits[0]
                else:
                    _url = "@".join(splits[:-1])

                url = _url + "@" + self.version

            try:
                req = urllib.request.Request(url, method="GET")
                response = urllib.request.urlopen(req)
                response.close()
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    raise Exception("Plugin is undefined or outdated!")

        return url

    # Поскольку названия плагинов должны быть уникальны,
    # тк именно они используются в блоке в качестве типа
    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
