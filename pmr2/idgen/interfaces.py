import zope.interface
import zope.schema


class IIdGenerator(zope.interface.Interface):
    """\
    Generic PMR2 ID Generator.
    """

    def next():
        """\
        Gets the next value.
        """


class IAutoinc(zope.interface.Interface):
    """\
    Storage of the last
    """

    value = zope.schema.Int(
        title=u'Value',
        description=u'The current value of this counter.',
        default=0,
    )
