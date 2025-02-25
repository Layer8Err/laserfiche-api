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
from laserfiche_api.models.field_definition import FieldDefinition  # noqa: F401,E501

class TemplateFieldDefinition(FieldDefinition):
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
        'rule': 'object',
        'group_id': 'int',
        'group_name': 'str'
    }
    if hasattr(FieldDefinition, "swagger_types"):
        swagger_types.update(FieldDefinition.swagger_types)

    attribute_map = {
        'rule': 'rule',
        'group_id': 'groupId',
        'group_name': 'groupName'
    }
    if hasattr(FieldDefinition, "attribute_map"):
        attribute_map.update(FieldDefinition.attribute_map)

    def __init__(self, rule=None, group_id=None, group_name=None, *args, **kwargs):  # noqa: E501
        """TemplateFieldDefinition - a model defined in Swagger"""  # noqa: E501
        self._rule = None
        self._group_id = None
        self._group_name = None
        self.discriminator = None
        if rule is not None:
            self.rule = rule
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        FieldDefinition.__init__(self, *args, **kwargs)

    @property
    def rule(self):
        """Gets the rule of this TemplateFieldDefinition.  # noqa: E501

        A form logic rule associated with a Laserfiche template and field definition.  # noqa: E501

        :return: The rule of this TemplateFieldDefinition.  # noqa: E501
        :rtype: object
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this TemplateFieldDefinition.

        A form logic rule associated with a Laserfiche template and field definition.  # noqa: E501

        :param rule: The rule of this TemplateFieldDefinition.  # noqa: E501
        :type: object
        """

        self._rule = rule

    @property
    def group_id(self):
        """Gets the group_id of this TemplateFieldDefinition.  # noqa: E501

        The group id of the field in the template.  # noqa: E501

        :return: The group_id of this TemplateFieldDefinition.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this TemplateFieldDefinition.

        The group id of the field in the template.  # noqa: E501

        :param group_id: The group_id of this TemplateFieldDefinition.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this TemplateFieldDefinition.  # noqa: E501

        The name of field group.  # noqa: E501

        :return: The group_name of this TemplateFieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this TemplateFieldDefinition.

        The name of field group.  # noqa: E501

        :param group_name: The group_name of this TemplateFieldDefinition.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

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
        if issubclass(TemplateFieldDefinition, dict):
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
        if not isinstance(other, TemplateFieldDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
