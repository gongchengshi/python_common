import pysolr


def document_exists(self, id):
    results = self.search('id:%s' % id)
    return results.hits > 0


def extend_pysolr():
    pysolr.Solr.document_exists = document_exists
