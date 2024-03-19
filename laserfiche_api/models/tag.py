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

class Tag(object):
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
        'id': 'int',
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'is_secure': 'bool',
        'watermark': 'OneOfTagWatermark'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'is_secure': 'isSecure',
        'watermark': 'watermark'
    }

    def __init__(self, id=None, name=None, display_name=None, description=None, is_secure=None, watermark=None):  # noqa: E501
        """Tag - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._display_name = None
        self._description = None
        self._is_secure = None
        self._watermark = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if is_secure is not None:
            self.is_secure = is_secure
        if watermark is not None:
            self.watermark = watermark

    @property
    def id(self):
        """Gets the id of this Tag.  # noqa: E501

        The ID of the tag definition.  # noqa: E501

        :return: The id of this Tag.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tag.

        The ID of the tag definition.  # noqa: E501

        :param id: The id of this Tag.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Tag.  # noqa: E501

        The name of the tag definition.  # noqa: E501

        :return: The name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.

        The name of the tag definition.  # noqa: E501

        :param name: The name of this Tag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Tag.  # noqa: E501

        The localized name of the tag definition.  # noqa: E501

        :return: The display_name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Tag.

        The localized name of the tag definition.  # noqa: E501

        :param display_name: The display_name of this Tag.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Tag.  # noqa: E501

        The description of the tag definition.  # noqa: E501

        :return: The description of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Tag.

        The description of the tag definition.  # noqa: E501

        :param description: The description of this Tag.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_secure(self):
        """Gets the is_secure of this Tag.  # noqa: E501

        A boolean indicating whether or not the tag definition is classified as a security tag (true) or an informational tag (false).  # noqa: E501

        :return: The is_secure of this Tag.  # noqa: E501
        :rtype: bool
        """
        return self._is_secure

    @is_secure.setter
    def is_secure(self, is_secure):
        """Sets the is_secure of this Tag.

        A boolean indicating whether or not the tag definition is classified as a security tag (true) or an informational tag (false).  # noqa: E501

        :param is_secure: The is_secure of this Tag.  # noqa: E501
        :type: bool
        """

        self._is_secure = is_secure

    @property
    def watermark(self):
        """Gets the watermark of this Tag.  # noqa: E501

        The watermark properties associated with the tag definition.  # noqa: E501

        :return: The watermark of this Tag.  # noqa: E501
        :rtype: OneOfTagWatermark
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        """Sets the watermark of this Tag.

        The watermark properties associated with the tag definition.  # noqa: E501

        :param watermark: The watermark of this Tag.  # noqa: E501
        :type: OneOfTagWatermark
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
        if issubclass(Tag, dict):
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
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
