; (function () {
    addEventListener("DOMContentLoaded", initDjangoEditorJSField);

    function initDjangoEditorJSField() {
        const fields = document.querySelectorAll("[data-editorjs-textarea]");

        for (let field of fields) {
            initFormFieldEditor(field.getAttribute("id"));
        }
    }

    function initFormFieldEditor(fieldId) {
        const dataStorage = document.getElementById(fieldId);
        const editorHolder = document.getElementById(fieldId + "_editorjs_holder");
        const editorConfig = JSON.parse(editorHolder.getAttribute("data-editorjs-config"));
        const tools = editorConfig.tools;

        for (let plugin in editorConfig.tools) {
            cls = tools[plugin].class;

            if (cls && window[cls] != undefined) {
                tools[plugin].class = eval(cls);
                continue
            }

            delete tools[plugin]
            console.error(`Not found error:\nPlugin ${plugin} is not presented!]`);
        }

        editorConfig.tools = tools;

        const editor = new EditorJS({
            holder: fieldId + "_editorjs_holder",
            data: JSON.parse(dataStorage.value),
            onChange: (api, event) => editor.save().then(outputData => dataStorage.value = JSON.stringify(outputData)), 
            ...editorConfig 
        });
    }
})();