import json
import logging
import re
from swagger_server.api import APIUtils
from swagger_server.models.search_data_linkset import SearchDataLinkset, SearchDataLinksetLinks
from swagger_server.models.index_schema_description import IndexSchemaDescription
from swagger_server.models.search_data import SearchData
from swagger_server.models.search_data_search_result import SearchDataSearchResult
from swagger_server.services.grid_search.search_attributes import SearchAttributes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)

INDEX = 'props-and-metadata'
SEARCH_ATTRIBUTES_PATTERN = re.compile("[a-zA-Z0-9]*:")


class GenericSearch:
    """
    service class to handle all the rest api controller calls
    """

    def __init__(self):
        self.api = APIUtils()
        self.indexed_terms = self.get_index_search_attribute_list(INDEX)

    def generic_search(self, index_name, dsl_query):
        """
        Generic Search on index if found any search associated runs/projects
        :param dsl_query: elastic search query dsl
        :param index_name: name of index on which search is to be performed
        :return: result data if any hits
        """

        dsl_json = {}
        return dsl_json

    @staticmethod
    def get_index_search_attribute_list(index_name):
        search_attributes = None
        search_attribute_dict = {}
        search_attributes = SearchAttributes().search_attributes()

        if search_attributes is not None:
            attributes = search_attributes.attributes
            for entry in attributes:
                search_attribute_dict[entry.attrib_name] = entry.attrib_path
            return search_attribute_dict
        else:
            return None

