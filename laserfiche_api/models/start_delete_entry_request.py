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

class StartDeleteEntryRequest(object):
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
        'audit_reason_id': 'int',
        'audit_reason_comment': 'str'
    }

    attribute_map = {
        'audit_reason_id': 'auditReasonId',
        'audit_reason_comment': 'auditReasonComment'
    }

    def __init__(self, audit_reason_id=None, audit_reason_comment=None):  # noqa: E501
        """StartDeleteEntryRequest - a model defined in Swagger"""  # noqa: E501
        self._audit_reason_id = None
        self._audit_reason_comment = None
        self.discriminator = None
        if audit_reason_id is not None:
            self.audit_reason_id = audit_reason_id
        if audit_reason_comment is not None:
            self.audit_reason_comment = audit_reason_comment

    @property
    def audit_reason_id(self):
        """Gets the audit_reason_id of this StartDeleteEntryRequest.  # noqa: E501

        The reason id for this audit event.  # noqa: E501

        :return: The audit_reason_id of this StartDeleteEntryRequest.  # noqa: E501
        :rtype: int
        """
        return self._audit_reason_id

    @audit_reason_id.setter
    def audit_reason_id(self, audit_reason_id):
        """Sets the audit_reason_id of this StartDeleteEntryRequest.

        The reason id for this audit event.  # noqa: E501

        :param audit_reason_id: The audit_reason_id of this StartDeleteEntryRequest.  # noqa: E501
        :type: int
        """

        self._audit_reason_id = audit_reason_id

    @property
    def audit_reason_comment(self):
        """Gets the audit_reason_comment of this StartDeleteEntryRequest.  # noqa: E501

        The comment for this audit event.  # noqa: E501

        :return: The audit_reason_comment of this StartDeleteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._audit_reason_comment

    @audit_reason_comment.setter
    def audit_reason_comment(self, audit_reason_comment):
        """Sets the audit_reason_comment of this StartDeleteEntryRequest.

        The comment for this audit event.  # noqa: E501

        :param audit_reason_comment: The audit_reason_comment of this StartDeleteEntryRequest.  # noqa: E501
        :type: str
        """

        self._audit_reason_comment = audit_reason_comment

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
        if issubclass(StartDeleteEntryRequest, dict):
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
        if not isinstance(other, StartDeleteEntryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
