import zope.interface
import zope.schema


class ICounter(zope.interface.Interface):

    value = zope.schema.Int(
        title=u'Value',
        description=u'The current value of this counter.',
        default=0,
    )

    def next():
        """\
        Gets the next value.
        """

    def last():
        """\
        Gets the last value.
        """
