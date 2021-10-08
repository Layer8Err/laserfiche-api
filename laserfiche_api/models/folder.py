# coding: utf-8

"""
    Laserfiche API

    Welcome to the Laserfiche API Swagger Playground. You can try out any of our API calls against your live Laserfiche Cloud account. Visit the developer center for more details: <a href=\"https://developer.laserfiche.com\">https://developer.laserfiche.com</a><p><strong>Build# : </strong>650780</p>  # noqa: E501

    OpenAPI spec version: 1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from laserfiche_api.models.entry import Entry  # noqa: F401,E501

class Folder(Entry):
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
        'is_record_folder': 'bool',
        'is_under_record_series': 'bool',
        'children': 'list[Entry]'
    }
    if hasattr(Entry, "swagger_types"):
        swagger_types.update(Entry.swagger_types)

    attribute_map = {
        'is_record_folder': 'isRecordFolder',
        'is_under_record_series': 'isUnderRecordSeries',
        'children': 'children'
    }
    if hasattr(Entry, "attribute_map"):
        attribute_map.update(Entry.attribute_map)

    def __init__(self, is_record_folder=None, is_under_record_series=None, children=None, *args, **kwargs):  # noqa: E501
        """Folder - a model defined in Swagger"""  # noqa: E501
        self._is_record_folder = None
        self._is_under_record_series = None
        self._children = None
        self.discriminator = None
        if is_record_folder is not None:
            self.is_record_folder = is_record_folder
        if is_under_record_series is not None:
            self.is_under_record_series = is_under_record_series
        if children is not None:
            self.children = children
        Entry.__init__(self, *args, **kwargs)

    @property
    def is_record_folder(self):
        """Gets the is_record_folder of this Folder.  # noqa: E501

        A boolean indicating if the folder that this instance represents is known to be a record folder.  # noqa: E501

        :return: The is_record_folder of this Folder.  # noqa: E501
        :rtype: bool
        """
        return self._is_record_folder

    @is_record_folder.setter
    def is_record_folder(self, is_record_folder):
        """Sets the is_record_folder of this Folder.

        A boolean indicating if the folder that this instance represents is known to be a record folder.  # noqa: E501

        :param is_record_folder: The is_record_folder of this Folder.  # noqa: E501
        :type: bool
        """

        self._is_record_folder = is_record_folder

    @property
    def is_under_record_series(self):
        """Gets the is_under_record_series of this Folder.  # noqa: E501

        A boolean indicating if the folder that this instance represents is known to directly or indirectly under a record series in the repository.  # noqa: E501

        :return: The is_under_record_series of this Folder.  # noqa: E501
        :rtype: bool
        """
        return self._is_under_record_series

    @is_under_record_series.setter
    def is_under_record_series(self, is_under_record_series):
        """Sets the is_under_record_series of this Folder.

        A boolean indicating if the folder that this instance represents is known to directly or indirectly under a record series in the repository.  # noqa: E501

        :param is_under_record_series: The is_under_record_series of this Folder.  # noqa: E501
        :type: bool
        """

        self._is_under_record_series = is_under_record_series

    @property
    def children(self):
        """Gets the children of this Folder.  # noqa: E501

        The entries in this folder.  # noqa: E501

        :return: The children of this Folder.  # noqa: E501
        :rtype: list[Entry]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this Folder.

        The entries in this folder.  # noqa: E501

        :param children: The children of this Folder.  # noqa: E501
        :type: list[Entry]
        """

        self._children = children

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
        if issubclass(Folder, dict):
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
        if not isinstance(other, Folder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
