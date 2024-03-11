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

The :attr:`module_level_variable1` module level variables may be documented
in either the ``Attributes`` section of the module docstring, or in an inline
docstring immediately following the variable.

Either form is acceptable, but the two should not be mixed. Choose one
convention to document module level variables and be consistent with it.

.. todo::
    * For TODOs directive module
    * You have to also use ``sphinx.ext.todo`` extension

.. _Sphinx Python Style Guide:
   https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
"""

module_level_variable1 = 12345

module_level_variable2 = 98765
""":obj:`int`: Module level variable documented inline.

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

    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    If *args or **kwargs are accepted, they should be listed as ``*args`` and
    ``**kwargs``.

    The format for a parameter is::

        ``:param (type) name: description``
            The description may span multiple lines. Following lines should be
            indented. The "(type)" is optional. Multiple paragraphs are
            supported in parameter descriptions.

    :param int param1: The first parameter.
    :param str param2=None: The second parameter.
    :param args: Variable length argument list.
    :param kwargs: Arbitrary keyword arguments.

    :rtype: bool
    :returns: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    :raises AttributeError: The ``Raises`` section is a list of all exceptions
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

    The :meth:`__init__` method may be documented in either the class level
    docstring, or as a docstring on the :meth:`__init__` method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the :meth:`__init__` method and be consistent with
    it.

    Attributes:
    * :attr:`msg` is a human readable string describing the exception.
    * :attr:`code` stores an exception error code.
    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
