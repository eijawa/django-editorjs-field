from django.template.loader import render_to_string


class EditorJSTool(object):
    """
    A class representing a EditorJS Tool (Plugin).

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

    Properties
    ==========
    config : dict
        Read-only.
        A Tool configuration dictionary property.

    Methods
    =======
    render() -> str:
        Render Tool with appropriate template into HTML string.
    """

    def __init__(
        self,
        name: str,
        url: str,
        template_name: str,
        class_name: str | None = None,
        **kwargs
    ):
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

        self.name = name
        self.url = self.__define_url(url)
        self.template_name = template_name

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

        # TODO: Проверить URL на:
        # 1. Это юрл?
        # 1.1 Это абсолютная ссылка?
        # 1.2 Это относительная ссылка?
        # 2. Это путь к файлу?
        # 2.1 Это абсолютный путь к файлу?
        # 2.2 Это относительный путь к файлу?

        # TODO: Добавить версию плагина, если это абсолютный юрл

        # TODO: Если есть версия плагина, то проверить, возможно ли его скачать, если нет - вывести ошибку

        return url

    # Поскольку названия плагинов должны быть уникальны,
    # тк именно они используются в блоке в качестве типа
    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
