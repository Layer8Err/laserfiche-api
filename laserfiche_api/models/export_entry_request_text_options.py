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

class ExportEntryRequestTextOptions(object):
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
        'include_redactions': 'bool',
        'redaction_character': 'str'
    }

    attribute_map = {
        'include_redactions': 'includeRedactions',
        'redaction_character': 'redactionCharacter'
    }

    def __init__(self, include_redactions=True, redaction_character='X'):  # noqa: E501
        """ExportEntryRequestTextOptions - a model defined in Swagger"""  # noqa: E501
        self._include_redactions = None
        self._redaction_character = None
        self.discriminator = None
        if include_redactions is not None:
            self.include_redactions = include_redactions
        if redaction_character is not None:
            self.redaction_character = redaction_character

    @property
    def include_redactions(self):
        """Gets the include_redactions of this ExportEntryRequestTextOptions.  # noqa: E501

        Indicates if redactions are included. The default value is true.  # noqa: E501

        :return: The include_redactions of this ExportEntryRequestTextOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_redactions

    @include_redactions.setter
    def include_redactions(self, include_redactions):
        """Sets the include_redactions of this ExportEntryRequestTextOptions.

        Indicates if redactions are included. The default value is true.  # noqa: E501

        :param include_redactions: The include_redactions of this ExportEntryRequestTextOptions.  # noqa: E501
        :type: bool
        """

        self._include_redactions = include_redactions

    @property
    def redaction_character(self):
        """Gets the redaction_character of this ExportEntryRequestTextOptions.  # noqa: E501

        The character that replaces the original character in a redacted text. The value must be a string of length 1 and must not be a whitespace character. The default value is 'X'.  # noqa: E501

        :return: The redaction_character of this ExportEntryRequestTextOptions.  # noqa: E501
        :rtype: str
        """
        return self._redaction_character

    @redaction_character.setter
    def redaction_character(self, redaction_character):
        """Sets the redaction_character of this ExportEntryRequestTextOptions.

        The character that replaces the original character in a redacted text. The value must be a string of length 1 and must not be a whitespace character. The default value is 'X'.  # noqa: E501

        :param redaction_character: The redaction_character of this ExportEntryRequestTextOptions.  # noqa: E501
        :type: str
        """

        self._redaction_character = redaction_character

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
        if issubclass(ExportEntryRequestTextOptions, dict):
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
        if not isinstance(other, ExportEntryRequestTextOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
