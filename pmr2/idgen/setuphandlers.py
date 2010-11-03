from StringIO import StringIO

from pmr2.idgen.interfaces import IIdGenerator
from pmr2.idgen.interfaces import IAutoinc


def add_default_counter(site):
    """\
    Add the default counter to the site.
    """

    out = StringIO()
    sm = site.getSiteManager()
    if not sm.queryUtility(IIdGenerator):
        print >> out, 'PMR2 default auto-increment counter registered'
        sm.registerUtility(IAutoinc(site), IIdGenerator, 'autoinc')
    return out.getvalue()

def remove_default_counter(site):
    """\
    Remove the default counter from the site.
    """

    out = StringIO()
    sm = site.getSiteManager()
    u = sm.queryUtility(IIdGenerator)
    if u:
        print >> out, 'PMR2 default auto-increment counter unregistered'
        sm.unregisterUtility(u, IIdGenerator, 'autoinc')
    return out.getvalue()

def importVarious(context):
    """\
    Install the various things needed to enable this package.
    """

    site = context.getSite()
    print add_default_counter(site)
