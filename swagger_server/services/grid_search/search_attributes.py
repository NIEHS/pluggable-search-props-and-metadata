from swagger_server.models import IndexSearchAttributes, SearchAttributes


class SearchAttributes:

    # ToDo: Currently attributes are hardcoded need to see if information can be directly retrieved from ES
    # ToDo: Add a field to contain example of each search attribute
    @staticmethod
    def search_attributes():
        """
        Parse index attribute and an particular index
        :return: searchAttributes
        """
        result = SearchAttributes()
        result.id = 'props-and-metadata'
        result.info = 'File properties and metadata index'
        result.name = 'File Properties and Metadata'
        result.attributes = []

        result.attributes.append(IndexSearchAttributes(
            attrib_name='FileName',
            attrib_example='result.text',
            attrib_type='String',
            attrib_path='PropsAndMetadata.Properties.FileName',
            info='File Name or collection name, the last part of the path',
            shortcut_text='file_name'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='FileAbsolutePath',
            attrib_example='/an/absolute/path.result.text',
            attrib_type='String',
            attrib_path='PropsAndMetadata.Properties.AbsolutePath',
            info='Absolute iRODS path',
            shortcut_text='file_absolute_path'
        ))

        return result
