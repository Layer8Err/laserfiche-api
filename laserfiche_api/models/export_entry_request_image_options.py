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

class ExportEntryRequestImageOptions(object):
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
        'format': 'OneOfExportEntryRequestImageOptionsFormat',
        'j_peg_compression_level': 'int',
        'include_annotations': 'bool',
        'convert_pdf_annotations': 'bool',
        'page_prefix': 'str',
        'include_redactions': 'bool',
        'watermark': 'OneOfExportEntryRequestImageOptionsWatermark'
    }

    attribute_map = {
        'format': 'format',
        'j_peg_compression_level': 'jPEGCompressionLevel',
        'include_annotations': 'includeAnnotations',
        'convert_pdf_annotations': 'convertPdfAnnotations',
        'page_prefix': 'pagePrefix',
        'include_redactions': 'includeRedactions',
        'watermark': 'watermark'
    }

    def __init__(self, format=None, j_peg_compression_level=70, include_annotations=True, convert_pdf_annotations=True, page_prefix=', Page ', include_redactions=True, watermark=None):  # noqa: E501
        """ExportEntryRequestImageOptions - a model defined in Swagger"""  # noqa: E501
        self._format = None
        self._j_peg_compression_level = None
        self._include_annotations = None
        self._convert_pdf_annotations = None
        self._page_prefix = None
        self._include_redactions = None
        self._watermark = None
        self.discriminator = None
        if format is not None:
            self.format = format
        if j_peg_compression_level is not None:
            self.j_peg_compression_level = j_peg_compression_level
        if include_annotations is not None:
            self.include_annotations = include_annotations
        if convert_pdf_annotations is not None:
            self.convert_pdf_annotations = convert_pdf_annotations
        if page_prefix is not None:
            self.page_prefix = page_prefix
        if include_redactions is not None:
            self.include_redactions = include_redactions
        if watermark is not None:
            self.watermark = watermark

    @property
    def format(self):
        """Gets the format of this ExportEntryRequestImageOptions.  # noqa: E501

        The image format to export as. Options include: MultiPageTIFF, SinglePageTIFF, PNG, PDF and JPEG. The default value is MultiPageTIFF. MultiPageTIFF format is a single multi-page TIFF file. SinglePageTIFF format is multiple single-page TIFF files (in a single zip file).  # noqa: E501

        :return: The format of this ExportEntryRequestImageOptions.  # noqa: E501
        :rtype: OneOfExportEntryRequestImageOptionsFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ExportEntryRequestImageOptions.

        The image format to export as. Options include: MultiPageTIFF, SinglePageTIFF, PNG, PDF and JPEG. The default value is MultiPageTIFF. MultiPageTIFF format is a single multi-page TIFF file. SinglePageTIFF format is multiple single-page TIFF files (in a single zip file).  # noqa: E501

        :param format: The format of this ExportEntryRequestImageOptions.  # noqa: E501
        :type: OneOfExportEntryRequestImageOptionsFormat
        """

        self._format = format

    @property
    def j_peg_compression_level(self):
        """Gets the j_peg_compression_level of this ExportEntryRequestImageOptions.  # noqa: E501

        The quality level for JPEG compression when exporting images. The value must be between 0 and 100 (inclusive). The default value is 70.  # noqa: E501

        :return: The j_peg_compression_level of this ExportEntryRequestImageOptions.  # noqa: E501
        :rtype: int
        """
        return self._j_peg_compression_level

    @j_peg_compression_level.setter
    def j_peg_compression_level(self, j_peg_compression_level):
        """Sets the j_peg_compression_level of this ExportEntryRequestImageOptions.

        The quality level for JPEG compression when exporting images. The value must be between 0 and 100 (inclusive). The default value is 70.  # noqa: E501

        :param j_peg_compression_level: The j_peg_compression_level of this ExportEntryRequestImageOptions.  # noqa: E501
        :type: int
        """

        self._j_peg_compression_level = j_peg_compression_level

    @property
    def include_annotations(self):
        """Gets the include_annotations of this ExportEntryRequestImageOptions.  # noqa: E501

        Indicates if the annotations need to be included. The default value is true.  # noqa: E501

        :return: The include_annotations of this ExportEntryRequestImageOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_annotations

    @include_annotations.setter
    def include_annotations(self, include_annotations):
        """Sets the include_annotations of this ExportEntryRequestImageOptions.

        Indicates if the annotations need to be included. The default value is true.  # noqa: E501

        :param include_annotations: The include_annotations of this ExportEntryRequestImageOptions.  # noqa: E501
        :type: bool
        """

        self._include_annotations = include_annotations

    @property
    def convert_pdf_annotations(self):
        """Gets the convert_pdf_annotations of this ExportEntryRequestImageOptions.  # noqa: E501

        Indicates if the annotations on the image need to be converted to PDF annotations when exporting to PDF format. The default value is true. This option is only applicable when exporting to PDF format and IncludeAnnotations is true.  # noqa: E501

        :return: The convert_pdf_annotations of this ExportEntryRequestImageOptions.  # noqa: E501
        :rtype: bool
        """
        return self._convert_pdf_annotations

    @convert_pdf_annotations.setter
    def convert_pdf_annotations(self, convert_pdf_annotations):
        """Sets the convert_pdf_annotations of this ExportEntryRequestImageOptions.

        Indicates if the annotations on the image need to be converted to PDF annotations when exporting to PDF format. The default value is true. This option is only applicable when exporting to PDF format and IncludeAnnotations is true.  # noqa: E501

        :param convert_pdf_annotations: The convert_pdf_annotations of this ExportEntryRequestImageOptions.  # noqa: E501
        :type: bool
        """

        self._convert_pdf_annotations = convert_pdf_annotations

    @property
    def page_prefix(self):
        """Gets the page_prefix of this ExportEntryRequestImageOptions.  # noqa: E501

        The page prefix of the individual files, when exporting to multi-file format (e.g.zip). The value must have a length of at most 10 characters and only valid characters that can be included in file names are allowed. The default value is \", Page \".  # noqa: E501

        :return: The page_prefix of this ExportEntryRequestImageOptions.  # noqa: E501
        :rtype: str
        """
        return self._page_prefix

    @page_prefix.setter
    def page_prefix(self, page_prefix):
        """Sets the page_prefix of this ExportEntryRequestImageOptions.

        The page prefix of the individual files, when exporting to multi-file format (e.g.zip). The value must have a length of at most 10 characters and only valid characters that can be included in file names are allowed. The default value is \", Page \".  # noqa: E501

        :param page_prefix: The page_prefix of this ExportEntryRequestImageOptions.  # noqa: E501
        :type: str
        """

        self._page_prefix = page_prefix

    @property
    def include_redactions(self):
        """Gets the include_redactions of this ExportEntryRequestImageOptions.  # noqa: E501

        Indicates if redactions are included. The default value is true.  # noqa: E501

        :return: The include_redactions of this ExportEntryRequestImageOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_redactions

    @include_redactions.setter
    def include_redactions(self, include_redactions):
        """Sets the include_redactions of this ExportEntryRequestImageOptions.

        Indicates if redactions are included. The default value is true.  # noqa: E501

        :param include_redactions: The include_redactions of this ExportEntryRequestImageOptions.  # noqa: E501
        :type: bool
        """

        self._include_redactions = include_redactions

    @property
    def watermark(self):
        """Gets the watermark of this ExportEntryRequestImageOptions.  # noqa: E501

        The watermark element added to each image. No watermark will be added by default.  # noqa: E501

        :return: The watermark of this ExportEntryRequestImageOptions.  # noqa: E501
        :rtype: OneOfExportEntryRequestImageOptionsWatermark
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        """Sets the watermark of this ExportEntryRequestImageOptions.

        The watermark element added to each image. No watermark will be added by default.  # noqa: E501

        :param watermark: The watermark of this ExportEntryRequestImageOptions.  # noqa: E501
        :type: OneOfExportEntryRequestImageOptionsWatermark
        """

        self._watermark = watermark

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
        if issubclass(ExportEntryRequestImageOptions, dict):
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
        if not isinstance(other, ExportEntryRequestImageOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
