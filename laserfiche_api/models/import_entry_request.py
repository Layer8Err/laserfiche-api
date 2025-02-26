# coding: utf-8

"""
    Laserfiche Repository API

    Welcome to the Laserfiche API Swagger Playground. You can try out any of our API calls against your live Laserfiche Cloud account. Visit the developer center for more details: <a href=\"https://developer.laserfiche.com\">https://developer.laserfiche.com</a><p>Visit the changelog for the list of changes: <a href=\"/repository/v2/changelog\">/repository/v2/changelog</a></p><p><strong>Build# : </strong>41a7347c0662989661d7ab8105a70d36cb42518e_.20240124.4</p>  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ImportEntryRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'auto_rename': 'bool',
        'pdf_options': 'OneOfImportEntryRequestPdfOptions',
        'import_as_electronic_document': 'bool',
        'metadata': 'OneOfImportEntryRequestMetadata',
        'volume_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'auto_rename': 'autoRename',
        'pdf_options': 'pdfOptions',
        'import_as_electronic_document': 'importAsElectronicDocument',
        'metadata': 'metadata',
        'volume_name': 'volumeName'
    }

    def __init__(self, name=None, auto_rename=False, pdf_options=None, import_as_electronic_document=False, metadata=None, volume_name=None):  # noqa: E501
        """ImportEntryRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._auto_rename = None
        self._pdf_options = None
        self._import_as_electronic_document = None
        self._metadata = None
        self._volume_name = None
        self.discriminator = None
        self.name = name
        if auto_rename is not None:
            self.auto_rename = auto_rename
        if pdf_options is not None:
            self.pdf_options = pdf_options
        if import_as_electronic_document is not None:
            self.import_as_electronic_document = import_as_electronic_document
        if metadata is not None:
            self.metadata = metadata
        if volume_name is not None:
            self.volume_name = volume_name

    @property
    def name(self):
        """Gets the name of this ImportEntryRequest.  # noqa: E501

        The name for the imported entry.  # noqa: E501

        :return: The name of this ImportEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportEntryRequest.

        The name for the imported entry.  # noqa: E501

        :param name: The name of this ImportEntryRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def auto_rename(self):
        """Gets the auto_rename of this ImportEntryRequest.  # noqa: E501

        Indicates if the entry should be automatically renamed if an entry already exists with the given name in the folder. The default value is false.  # noqa: E501

        :return: The auto_rename of this ImportEntryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_rename

    @auto_rename.setter
    def auto_rename(self, auto_rename):
        """Sets the auto_rename of this ImportEntryRequest.

        Indicates if the entry should be automatically renamed if an entry already exists with the given name in the folder. The default value is false.  # noqa: E501

        :param auto_rename: The auto_rename of this ImportEntryRequest.  # noqa: E501
        :type: bool
        """

        self._auto_rename = auto_rename

    @property
    def pdf_options(self):
        """Gets the pdf_options of this ImportEntryRequest.  # noqa: E501

        The options applied when importing a PDF.  # noqa: E501

        :return: The pdf_options of this ImportEntryRequest.  # noqa: E501
        :rtype: OneOfImportEntryRequestPdfOptions
        """
        return self._pdf_options

    @pdf_options.setter
    def pdf_options(self, pdf_options):
        """Sets the pdf_options of this ImportEntryRequest.

        The options applied when importing a PDF.  # noqa: E501

        :param pdf_options: The pdf_options of this ImportEntryRequest.  # noqa: E501
        :type: OneOfImportEntryRequestPdfOptions
        """

        self._pdf_options = pdf_options

    @property
    def import_as_electronic_document(self):
        """Gets the import_as_electronic_document of this ImportEntryRequest.  # noqa: E501

        Indicates if the document should be imported as an electronic document (true) or as image pages (false). The default value is false. This option is only applicable when importing the following document types: txt, tif, tiff, bmp, pcx, jpg, jpeg, gif, png.  # noqa: E501

        :return: The import_as_electronic_document of this ImportEntryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._import_as_electronic_document

    @import_as_electronic_document.setter
    def import_as_electronic_document(self, import_as_electronic_document):
        """Sets the import_as_electronic_document of this ImportEntryRequest.

        Indicates if the document should be imported as an electronic document (true) or as image pages (false). The default value is false. This option is only applicable when importing the following document types: txt, tif, tiff, bmp, pcx, jpg, jpeg, gif, png.  # noqa: E501

        :param import_as_electronic_document: The import_as_electronic_document of this ImportEntryRequest.  # noqa: E501
        :type: bool
        """

        self._import_as_electronic_document = import_as_electronic_document

    @property
    def metadata(self):
        """Gets the metadata of this ImportEntryRequest.  # noqa: E501

        The metadata that will be assigned to the entry.  # noqa: E501

        :return: The metadata of this ImportEntryRequest.  # noqa: E501
        :rtype: OneOfImportEntryRequestMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ImportEntryRequest.

        The metadata that will be assigned to the entry.  # noqa: E501

        :param metadata: The metadata of this ImportEntryRequest.  # noqa: E501
        :type: OneOfImportEntryRequestMetadata
        """

        self._metadata = metadata

    @property
    def volume_name(self):
        """Gets the volume_name of this ImportEntryRequest.  # noqa: E501

        The name of the volume to use. Will use the default parent entry volume if not specified. This is ignored in Laserfiche Cloud.  # noqa: E501

        :return: The volume_name of this ImportEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this ImportEntryRequest.

        The name of the volume to use. Will use the default parent entry volume if not specified. This is ignored in Laserfiche Cloud.  # noqa: E501

        :param volume_name: The volume_name of this ImportEntryRequest.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ImportEntryRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportEntryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
