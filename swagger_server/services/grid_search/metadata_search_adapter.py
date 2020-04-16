from swagger_server.models import Indexes


class NotFoundError(Exception):
        pass


class MetadataSearchAdapter:
    """Supports basic file properties asnd metadata search core Elastic search functions provided to the standard API"""

    def __init__(self):
        """
        Parameters

        """

        pass

    @staticmethod
    def describe_index():
        """
        Describe the capabilities of this particular index server
        :return: index
        """

        index_search = Indexes()
        index_search.id = "irods-default-props-and-metadata"
        index_search.name = "iRODS File Properties and Metadata"
        index_search.info = "Standard iRODS File Properties and Metadata Search API"
        indexes = []
        index_entry = Indexes()
        index_entry.id = "props-and-metadata"
        index_entry.es_id = "irods-props-and-metadata"
        index_entry.name = "iRODS Props and Metadata"
        index_entry.maintainer = "iRODS"
        index_entry.contact_email = "irods@irods.org"
        index_entry.info = "Generic file properties and metadata search"
        indexes.append(index_entry)

        index_search.indexes = indexes

        return index_search
