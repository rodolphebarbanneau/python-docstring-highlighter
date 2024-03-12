# Python Docstring Highlighter

![GitHub issues](https://img.shields.io/badge/style-google-green)
![GitHub issues](https://img.shields.io/badge/style-numpy-green)
![GitHub issues](https://img.shields.io/badge/style-sphinx-green)
![GitHub issues](https://img.shields.io/badge/style-docblockr-red)

## Features

This extension is designed to **highlight docstrings** in **Python code**, making it easier to read and understand the source code. It does not provide any support for editing or creating docstrings. It is optimized for the **Google**, **NumPy**, and **Sphinx** styles docstring format, though it should work partially with other formats as well.

![Demo](https://raw.githubusercontent.com/rodolphebarbanneau/python-docstring-highlighter/main/assets/docstring.gif)

> **Technical Note**: The highlighting uses the VScode TextMate grammar injection feature, which means that it is compatible with any color theme and should not lead to performance issues (i.e. no custom scripts is executed). The extension uses a custom  grammar to match the docstring patterns and inject the appropriate scopes into the code editor.

> **Technical Note**: TextMate grammar injection can only match one-ligne regular expressions consistently. This means that the extension will not be able to match multi-line patterns in the docstring. This is a limitation of the TextMate grammar injection feature and cannot be worked around.

## Requirements

This extension is **only compatible** with the standard [VSCode Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python). It is not compatible with other language server like _Python for VSCode (deprecated)_.

## Extension Settings

This extensions does not provide specific settings. It is designed to work out of the box with the default color theme. However, you can customize the color theme by overriding the default color theme in yout `settings.json` file (see the [Customization](#customization) section).

### Available Scopes

Each highlighted token is associated with at least two TextMate scopes, a standard one used within VSCode by default for out of the box syntax highlighting, and an extension specific one that can be used to override the default color theme in the `settings.json` file (see the [Customization](#customization) section).

The following list shows the available scopes with their available sub-scopes specific to the extension with a brief description of their purpose. Scopes can be chained together to create a more specific match, for example `docstring.heading.begin` will match the beginning token of a docstring heading.

#### `docstring.heading`

Section headings in the docstring (e.g. `Args`, `Returns`, or `Raises`)

- `.python`
- `.begin.python`
- `.placeholder.python`
- `.end.python`

#### `docstring.directive`

Directives in the docstring (e.g. `.. note::`, or `.. warning::`).

- `.python`
- `.begin.python`
- `.placeholder.python`
- `.end.python`

#### `docstring.identifier`

Identifiers in the docstring (e.g. `:meth:`, or `:attr:`).

- `.python`
- `.begin.python`
- `.placeholder.python`
- `.end.python`

#### `docstring.literal`

Inline literals in the docstring (e.g. ``` ``"Sucssefully executed"`` ```).

- `.python`
- `.begin.python`
- `.placeholder.python`
- `.end.python`

#### `docstring.snippet`

Interpreted text for code snippets in the docstring (e.g. ``` :meth:`__init__` ```). Optionally, the snippet type can be specified as a sub-scope (e.g. `docstring.snippet.function`).

- `[.function|.type|.variable|.other]` + `.python`
- `.begin` + `[.function|.type|.variable|.other]` + `.python`
- `.placeholder` + `[.function|.type|.variable|.other]` + `.python`
- `.end` + `[.function|.type|.variable|.other]` + `.python`

#### `docstring.variable`

Variables in the docstring (e.g. `:param foo:`, `foo (int):`, or `foo : int`). Optionally, the  variable style can be specified as a sub-scope (e.g. `docstring.variable.google`).

- `[.google|.numpy|.sphinx]` + `.python`
- `.begin` + `[.google|.numpy|.sphinx]` + `.python`
- `.placeholder` + `[.google|.numpy|.sphinx]` + `.python`
- `.end` + `[.google|.numpy|.sphinx]` + `.python`

#### `docstring.type`

Type in the docstring (e.g. `"""type:`). Optionally, the type style can be specified as a sub-scope (e.g. `docstring.type.google`).

- `[.google|.numpy|.sphinx]` + `.python`
- `.begin` + `[.google|.numpy|.sphinx]` + `.python`
- `.placeholder` + `[.google|.numpy|.sphinx]` + `.python`
- `.end` + `[.google|.numpy|.sphinx]` + `.python`

### Customization

You can customize the color theme by overriding the default color theme in your `settings.json` file. For example, to change the color of the heading placeholders in the docstring, you can add the following to your `settings.json` file:

```json
"editor.tokenColorCustomizations": {
  "textMateRules": [
    {
      "scope": "docstring.heading.placeholder",
      "settings": {
        "fontStyle": "bold underline",
        "foreground": "#569cd6",
      }
    },
  ]
}
```

> See also the extension repository [tests/](https://github.com/rodolphebarbanneau/python-docstring-highlighter/blob/main/tests/.vscode/settings.json) folder for a detailed example of how to override the default color theme.

## Release Notes

### 0.2.0

- Added documentation
- Added raw docstring scope support
- Renamed extension specific scopes to have a more consistent naming convention
- Updated `google`, `numpy`, and `sphinx` variable token regex
- Updated tests

### 0.1.0

- Initial release
