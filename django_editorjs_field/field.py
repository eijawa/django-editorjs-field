from django.db import models

from functools import cached_property

from .tool import EditorJSTool as Tool
from .widget import EditorJSWidget


def no_tools_provided_warning():
    from warnings import warn

    warn(
        "You are running EditorJSField without any plugins! Only default - Paragraph - will be available."
    )


class EditorJSField(models.JSONField):
    description = "An EditorJS field."

    def __init__(self, *args, **kwargs):
        unexceptable_kwargs = ["holderId", "holder", "onReady", "onChange"]

        for u_k in unexceptable_kwargs:
            if u_k in kwargs.keys():
                del kwargs[u_k]

        self.config = kwargs.copy()

        self.__paragraph_tool = None
        if "tools" in self.config.keys():
            self.config["tools"] = list(set(self.config["tools"]))

            if not len(self.config["tools"]):
                no_tools_provided_warning()

            for tool_idx in range(len(self.config["tools"])):
                if self.config["tools"][tool_idx].class_name == "Paragraph":
                    self.__paragraph_tool = self.config["tools"].pop(tool_idx)
                    break
        else:
            no_tools_provided_warning()

        kwargs.clear()
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        # Удаление созданных в конструкторе полей

        return name, path, args, kwargs

    def formfield(self, **kwargs):
        kwargs["widget"] = EditorJSWidget(config=self.config)
        return super().formfield(**kwargs)

    @property
    def non_db_attrs(self):
        return super().non_db_attrs + ("tools",)

    @cached_property
    def tools(self):
        return {
            tool.name: tool
            for tool in [self.__get_paragraph_tool(), *self.config["tools"]]
        }

    def __get_paragraph_tool(self):
        if not self.__paragraph_tool:
            self.__paragraph_tool = Tool(
                name="paragraph",
                class_name="Paragraph",
                url="//cdn.jsdelivr.net/npm/@editorjs/paragraph",
                template_name="django_editorjs_field/tools/p.html",
            )

        return self.__paragraph_tool
