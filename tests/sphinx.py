"""Example module with Sphinx style docstrings.

This module demonstrates documentation as specified by the
`Sphinx Python Style Guide`_. Docstrings may extend over multiple lines.
Sections are created with a section header and a colon followed by a block of
indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks are also
implicitly created anytime a new section starts.

The :attr:`module_level_variable1` module level variables must be documented
in an inline docstring immediately following the variable.

.. todo::
    * For TODOs directive module
    * You have to also use ``sphinx.ext.todo`` extension

.. _Sphinx Python Style Guide:
    https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
"""

module_level_variable1 = 12345

module_level_variable2 = 98765
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified on
the first line, separated by a colon.
"""


def function_with_types_in_docstring(param1, param2):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    :param int param1: The first parameter.
    :param str param2: The second parameter.

    :rtype: bool
    :returns: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/
    """
    pass


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Example function with PEP 484 type annotations.

    :param param1: The first parameter.
    :param param2: The second parameter.
    :returns: The return value. True for success, False otherwise.
    """
    return True


def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.

    Function parameters should be documented using the ``:param:`` and
    ``:type:`` directives. The ``:type:`` directive is optional, and may be
    used to specify the type of the parameter being documented. Alternatively,
    this can be specified in the ``:param:`` directive just before the
    parameter name. The name of each parameter is required. The type and
    description of each parameter is optional, but should be included if not
    obvious.

    If \*args or \*\*kwargs are accepted, they should be listed as ``*args``
    and ``**kwargs``.

    The format for a parameter is::

        :param type name: some description
            The description may span multiple lines. Following lines should be
            indented. The "type" is optional. Multiple paragraphs are supported
            in parameter descriptions.

    :param int param1: The first parameter.
    :param str param2=None: The second parameter.
    :param args: Variable length argument list.
    :param kwargs: Arbitrary keyword arguments.

    :rtype: bool
    :returns: True if successful, False otherwise.

        The return type is optional and may be specified using the ``:rtype:``
        directive.

        The ``:returns:`` description may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``:returns:`` description supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    :raises AttributeError: The ``:raises:`` directives list all exceptions
        that are relevant to the interface.
    :raises ValueError: If `param2` is equal to `param1`.
    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True


def example_generator(n):
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    :param int n: The upper limit of the range to generate, from 0 to `n` - 1.
    :yields: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]
    """
    for i in range(n):
        yield i


class ExampleError(Exception):
    """Exceptions are documented in the same way as classes.

    The :meth:`__init__` method must be documented within its docstring while
    the class attributes are documented inline.
    """

    msg: str
    """Human readable string describing the exception."""

    code: int
    """Exception error code."""

    def __init__(self, msg, code):
        """Example of docstring on the :meth:`__init__` method.

        :param str msg: Human readable string describing the exception.
        :param int code=None: Error code.

        .. note::
            Do not include the `self` parameter in the ``:param:``directives.
        """
        self.msg = msg
        self.code = code


class ExampleClass(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they must be documented inline with
    the attribute's declaration (see :meth:`__init__` method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.
    """

    attr1: str
    """Description of `attr1`."""

    def __init__(self, param1, param2, param3):
        """Example of docstring on the :meth:`__init__` method.

        :param str param1: Description of `param1`.
        :param int param2=None: Description of `param2`. Multiple
            lines are supported.
        :param List[str] param3: Description of `param3`.

        .. note::
            Do not include the `self` parameter in the ``:param:``directives.
        """
        self.attr1 = param1
        self.attr2 = param2  #: Doc comment *inline* with attribute
        self.attr3 = param3  #: Doc comment *inline* with attribute

        #: list of str: Doc comment *before* attribute, with type specified
        self.attr4 = ['attr4']

        self.attr5 = None
        """str: Docstring *after* attribute, with type specified."""

    @property
    def readonly_property(self):
        """str: Properties should be documented in their getter method."""
        return 'readonly_property'

    @property
    def readwrite_property(self):
        """:obj:`list` of :obj:`str`: Properties with both a getter and setter
        should only be documented in their getter method.

        If the setter method contains notable behavior, it should be mentioned
        here.
        """
        return ['readwrite_property']

    @readwrite_property.setter
    def readwrite_property(self, value):
        value

    def example_method(self, param1, param2):
        """Class methods are similar to regular functions.

        :param str param1: The first parameter.
        :param int param2: The second parameter.
        :returns: True if successful, False otherwise.
        :rtype: bool

        .. note::
            Do not include the `self` parameter in the ``:param:``directives.
        """
        return True

    def __special__(self):
        """By default special members with docstrings are not included.

        Special members are any methods or attributes that start with and end
        with a double underscore. Any special member with a docstring will be
        included in the output, if ``napoleon_include_special_with_doc`` is set
        to True.

        This behavior can be enabled by changing the following setting in
        Sphinx's ``conf.py``::

            napoleon_include_special_with_doc = True
        """
        pass

    def __special_without_docstring__(self):
        pass

    def _private(self):
        """By default private members are not included.

        Private members are any methods or attributes that start with an
        underscore and are *not* special. By default they are not included in
        the output.

        This behavior can be changed such that private members *are* included
        by changing the following setting in Sphinx's ``conf.py``::

            napoleon_include_private_with_doc = True
        """
        pass

    def _private_without_docstring(self):
        pass

