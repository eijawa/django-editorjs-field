from devtools import debug

class EditorJSTool(object):
    def __init__(self, url, class_name=None, **kwargs):
        self.url = self.define_url(url)

        self._config = {
            "class": self.__class__.__name__
        }

        if class_name:
            self._config["class"] = class_name

        self._config.update(kwargs)

    @property
    def config(self):
        return self._config

    def render(self):
        raise NotImplementedError()

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

        return url

class Header(EditorJSTool):
    pass

if __name__ == "__main__":
    e = Header(class_name="header", inlineToolBar=True)
    debug(e.__dict__)
    debug(e.render())
    debug(e.config)