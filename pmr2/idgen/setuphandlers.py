from StringIO import StringIO

from pmr2.idgen.interfaces import IIdGenerator
from pmr2.idgen.interfaces import IAutoinc
from pmr2.idgen.interfaces import IAutoincHex

_counters = (
    (IAutoinc, 'autoinc'),
    (IAutoincHex, 'autohex'),
)


def add_default_counter(site):
    """\
    Add the default counter to the site.
    """

    out = StringIO()
    sm = site.getSiteManager()

    for iface, key in _counters:
        if not sm.queryUtility(IIdGenerator, key):
            print >> out, 'annotation for `%s` registered' % key
            sm.registerUtility(iface(site), IIdGenerator, key)

    return out.getvalue()

def remove_default_counter(site):
    """\
    Remove the default counter from the site.
    """

    out = StringIO()
    sm = site.getSiteManager()

    for iface, key in _counters:
        u = sm.queryUtility(IIdGenerator, key)
        if u:
            print >> out, 'annotation for `%s` unregistered' % key
            sm.unregisterUtility(u, IIdGenerator, key)

    return out.getvalue()

def importVarious(context):
    """\
    Install the various things needed to enable this package.
    """

    site = context.getSite()
    print add_default_counter(site)
