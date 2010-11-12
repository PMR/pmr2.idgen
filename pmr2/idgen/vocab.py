import zope.interface
import zope.component

from zope.schema.interfaces import IVocabulary, IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from pmr2.idgen.interfaces import *


class IdGeneratorVocab(SimpleVocabulary):
    """
    Retrieves a list of License documents stored within the CMS.
    """

    def __init__(self, context):
        terms = [SimpleTerm(key, key) for key, u in 
            zope.component.getUtilitiesFor(IIdGenerator, context=context)]
        super(IdGeneratorVocab, self).__init__(terms)

    def getTerm(self, value):
        try:
            return super(IdGeneratorVocab, self).getTerm(value)
        except LookupError:
            # should log the no longer registered utility.
            return SimpleTerm(value)

def IdGeneratorVocabFactory(context):
    return IdGeneratorVocab(context)
zope.interface.alsoProvides(IdGeneratorVocabFactory, IVocabularyFactory)
