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

class LinkCollectionResponse(object):
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
        'odata_next_link': 'str',
        'odata_count': 'int',
        'value': 'list[Link]'
    }

    attribute_map = {
        'odata_next_link': '@odata.nextLink',
        'odata_count': '@odata.count',
        'value': 'value'
    }

    def __init__(self, odata_next_link=None, odata_count=None, value=None):  # noqa: E501
        """LinkCollectionResponse - a model defined in Swagger"""  # noqa: E501
        self._odata_next_link = None
        self._odata_count = None
        self._value = None
        self.discriminator = None
        if odata_next_link is not None:
            self.odata_next_link = odata_next_link
        if odata_count is not None:
            self.odata_count = odata_count
        if value is not None:
            self.value = value

    @property
    def odata_next_link(self):
        """Gets the odata_next_link of this LinkCollectionResponse.  # noqa: E501

        A URL to retrieve the next page of the requested collection.  # noqa: E501

        :return: The odata_next_link of this LinkCollectionResponse.  # noqa: E501
        :rtype: str
        """
        return self._odata_next_link

    @odata_next_link.setter
    def odata_next_link(self, odata_next_link):
        """Sets the odata_next_link of this LinkCollectionResponse.

        A URL to retrieve the next page of the requested collection.  # noqa: E501

        :param odata_next_link: The odata_next_link of this LinkCollectionResponse.  # noqa: E501
        :type: str
        """

        self._odata_next_link = odata_next_link

    @property
    def odata_count(self):
        """Gets the odata_count of this LinkCollectionResponse.  # noqa: E501

        The total count of items within a collection.  # noqa: E501

        :return: The odata_count of this LinkCollectionResponse.  # noqa: E501
        :rtype: int
        """
        return self._odata_count

    @odata_count.setter
    def odata_count(self, odata_count):
        """Sets the odata_count of this LinkCollectionResponse.

        The total count of items within a collection.  # noqa: E501

        :param odata_count: The odata_count of this LinkCollectionResponse.  # noqa: E501
        :type: int
        """

        self._odata_count = odata_count

    @property
    def value(self):
        """Gets the value of this LinkCollectionResponse.  # noqa: E501


        :return: The value of this LinkCollectionResponse.  # noqa: E501
        :rtype: list[Link]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this LinkCollectionResponse.


        :param value: The value of this LinkCollectionResponse.  # noqa: E501
        :type: list[Link]
        """

        self._value = value

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
        if issubclass(LinkCollectionResponse, dict):
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
        if not isinstance(other, LinkCollectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
