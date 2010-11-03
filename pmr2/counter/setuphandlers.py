from StringIO import StringIO

from pmr2.counter.interfaces import ICounter
from pmr2.counter.interfaces import IAutoinc


def add_default_counter(site):
    """\
    Add the default counter to the site.
    """

    out = StringIO()
    sm = site.getSiteManager()
    if not sm.queryUtility(ICounter):
        print >> out, 'PMR2 default auto-increment counter registered'
        sm.registerUtility(IAutoinc(site), ICounter, 'autoinc')
    return out.getvalue()

def remove_default_counter(site):
    """\
    Remove the default counter from the site.
    """

    out = StringIO()
    sm = site.getSiteManager()
    u = sm.queryUtility(ICounter)
    if u:
        print >> out, 'PMR2 default auto-increment counter unregistered'
        sm.unregisterUtility(u, ICounter, 'autoinc')
    return out.getvalue()

def importVarious(context):
    """\
    Install the various things needed to enable this package.
    """

    site = context.getSite()
    print add_default_counter(site)
