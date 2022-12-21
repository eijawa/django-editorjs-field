from django.template.loader import render_to_string


class EditorJSTool(object):
    def __init__(self, name, url, template_name, class_name=None, **kwargs):
        self.name = name
        self.url = self.define_url(url)
        self.template_name = template_name

        self.class_name = name

        if class_name:
            self.class_name = class_name

        self._config = {"class": self.class_name, **kwargs}

    @property
    def config(self):
        return self._config

    def render(self, data):
        return render_to_string(self.template_name, data)

    def define_url(self, url):
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