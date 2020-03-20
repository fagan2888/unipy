def func(*args, **kwargs):
    """
    Summary

    This function splits an Iterable into the given size of multiple chunks.
    The items of An iterable should be the same type.

    Parameters
    ----------
    iterable: Iterable
        An Iterable to split.

    how: {'equal', 'remaining'}
        The method to split.
        'equal' is to split chunks with the approximate length
        within the given size.
        'remaining' is to split chunks with the given size,
        and the remains are bound as the last chunk.

    size: int
        The number of chunks.

    Returns
    -------
    list
        A list of chunks.

    See Also
    --------

    Examples
    --------
    >>> up.splitter(list(range(10)), how='equal', size=3)
    [(0, 1, 2, 3), (4, 5, 6), (7, 8, 9)]

    >>> up.splitter(list(range(10)), how='remaining', size=3)
    [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)]

    """
    pass


class ReusableGenerator(object):
    """Temporary Interface to re-use generator for convenience.

    Once assigned, It can be infinitely consumed
    **as long as an input generator remains un-exhausted.

    Attributes
    ----------
    _source: generator
        A source generator.

    See Also
    --------
    generator
    ``itertools.tee``

    Examples
    --------
    >>> from unipy.utils.generator import ReusableGenerator
    >>> gen = (i for i in range(10))
    >>> gen
    <generator object <genexpr> at 0x11120ebf8>
    >>> regen = ReusableGenerator(gen)
    >>> regen
    <unipy.utils.generator.ReusableGenerator object at 0x1061a97f0>
    >>> list(regen)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(regen)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(gen)  # If the source is used, copied one will be exhausted too.
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(gen)
    []
    >>> list(regen)
    []

    """

    def __init__(self, generator):
        pass
