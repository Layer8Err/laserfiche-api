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

class FieldDefinition(object):
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
        'display_name': 'str',
        'id': 'int',
        'description': 'str',
        'field_type': 'OneOfFieldDefinitionFieldType',
        'length': 'int',
        'default_value': 'str',
        'is_multi_value': 'bool',
        'is_required': 'bool',
        'constraint': 'str',
        'constraint_error': 'str',
        'list_values': 'list[str]',
        'format': 'OneOfFieldDefinitionFormat',
        'currency': 'str',
        'format_pattern': 'str'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'id': 'id',
        'description': 'description',
        'field_type': 'fieldType',
        'length': 'length',
        'default_value': 'defaultValue',
        'is_multi_value': 'isMultiValue',
        'is_required': 'isRequired',
        'constraint': 'constraint',
        'constraint_error': 'constraintError',
        'list_values': 'listValues',
        'format': 'format',
        'currency': 'currency',
        'format_pattern': 'formatPattern'
    }

    def __init__(self, name=None, display_name=None, id=None, description=None, field_type=None, length=None, default_value=None, is_multi_value=None, is_required=None, constraint=None, constraint_error=None, list_values=None, format=None, currency=None, format_pattern=None):  # noqa: E501
        """FieldDefinition - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._display_name = None
        self._id = None
        self._description = None
        self._field_type = None
        self._length = None
        self._default_value = None
        self._is_multi_value = None
        self._is_required = None
        self._constraint = None
        self._constraint_error = None
        self._list_values = None
        self._format = None
        self._currency = None
        self._format_pattern = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if field_type is not None:
            self.field_type = field_type
        if length is not None:
            self.length = length
        if default_value is not None:
            self.default_value = default_value
        if is_multi_value is not None:
            self.is_multi_value = is_multi_value
        if is_required is not None:
            self.is_required = is_required
        if constraint is not None:
            self.constraint = constraint
        if constraint_error is not None:
            self.constraint_error = constraint_error
        if list_values is not None:
            self.list_values = list_values
        if format is not None:
            self.format = format
        if currency is not None:
            self.currency = currency
        if format_pattern is not None:
            self.format_pattern = format_pattern

    @property
    def name(self):
        """Gets the name of this FieldDefinition.  # noqa: E501

        The name of the field.  # noqa: E501

        :return: The name of this FieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldDefinition.

        The name of the field.  # noqa: E501

        :param name: The name of this FieldDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this FieldDefinition.  # noqa: E501

        The localized name of the field.  # noqa: E501

        :return: The display_name of this FieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FieldDefinition.

        The localized name of the field.  # noqa: E501

        :param display_name: The display_name of this FieldDefinition.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this FieldDefinition.  # noqa: E501

        The ID of the field.  # noqa: E501

        :return: The id of this FieldDefinition.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FieldDefinition.

        The ID of the field.  # noqa: E501

        :param id: The id of this FieldDefinition.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this FieldDefinition.  # noqa: E501

        The description of the field.  # noqa: E501

        :return: The description of this FieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FieldDefinition.

        The description of the field.  # noqa: E501

        :param description: The description of this FieldDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def field_type(self):
        """Gets the field_type of this FieldDefinition.  # noqa: E501

        The type of the field.  # noqa: E501

        :return: The field_type of this FieldDefinition.  # noqa: E501
        :rtype: OneOfFieldDefinitionFieldType
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this FieldDefinition.

        The type of the field.  # noqa: E501

        :param field_type: The field_type of this FieldDefinition.  # noqa: E501
        :type: OneOfFieldDefinitionFieldType
        """

        self._field_type = field_type

    @property
    def length(self):
        """Gets the length of this FieldDefinition.  # noqa: E501

        The length of the field for variable length data types.  # noqa: E501

        :return: The length of this FieldDefinition.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this FieldDefinition.

        The length of the field for variable length data types.  # noqa: E501

        :param length: The length of this FieldDefinition.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def default_value(self):
        """Gets the default_value of this FieldDefinition.  # noqa: E501

        The default value of the field for new entries that are assigned to a template the represented field is a member of.  # noqa: E501

        :return: The default_value of this FieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this FieldDefinition.

        The default value of the field for new entries that are assigned to a template the represented field is a member of.  # noqa: E501

        :param default_value: The default_value of this FieldDefinition.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def is_multi_value(self):
        """Gets the is_multi_value of this FieldDefinition.  # noqa: E501

        A boolean indicating if the represented template field supports multiple values.  # noqa: E501

        :return: The is_multi_value of this FieldDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_multi_value

    @is_multi_value.setter
    def is_multi_value(self, is_multi_value):
        """Sets the is_multi_value of this FieldDefinition.

        A boolean indicating if the represented template field supports multiple values.  # noqa: E501

        :param is_multi_value: The is_multi_value of this FieldDefinition.  # noqa: E501
        :type: bool
        """

        self._is_multi_value = is_multi_value

    @property
    def is_required(self):
        """Gets the is_required of this FieldDefinition.  # noqa: E501

        A boolean indicating if the represented field must have a value set on entries assigned to a template that the field is a member of.  # noqa: E501

        :return: The is_required of this FieldDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this FieldDefinition.

        A boolean indicating if the represented field must have a value set on entries assigned to a template that the field is a member of.  # noqa: E501

        :param is_required: The is_required of this FieldDefinition.  # noqa: E501
        :type: bool
        """

        self._is_required = is_required

    @property
    def constraint(self):
        """Gets the constraint of this FieldDefinition.  # noqa: E501

        The constraint for values stored in the represented field.  # noqa: E501

        :return: The constraint of this FieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        """Sets the constraint of this FieldDefinition.

        The constraint for values stored in the represented field.  # noqa: E501

        :param constraint: The constraint of this FieldDefinition.  # noqa: E501
        :type: str
        """

        self._constraint = constraint

    @property
    def constraint_error(self):
        """Gets the constraint_error of this FieldDefinition.  # noqa: E501

        The error string that will be returned when the field constraint is violated when setting a value for this field.  # noqa: E501

        :return: The constraint_error of this FieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._constraint_error

    @constraint_error.setter
    def constraint_error(self, constraint_error):
        """Sets the constraint_error of this FieldDefinition.

        The error string that will be returned when the field constraint is violated when setting a value for this field.  # noqa: E501

        :param constraint_error: The constraint_error of this FieldDefinition.  # noqa: E501
        :type: str
        """

        self._constraint_error = constraint_error

    @property
    def list_values(self):
        """Gets the list_values of this FieldDefinition.  # noqa: E501

        The list of items assigned to the represented field.  # noqa: E501

        :return: The list_values of this FieldDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._list_values

    @list_values.setter
    def list_values(self, list_values):
        """Sets the list_values of this FieldDefinition.

        The list of items assigned to the represented field.  # noqa: E501

        :param list_values: The list_values of this FieldDefinition.  # noqa: E501
        :type: list[str]
        """

        self._list_values = list_values

    @property
    def format(self):
        """Gets the format of this FieldDefinition.  # noqa: E501

        The display format of the represented field.  # noqa: E501

        :return: The format of this FieldDefinition.  # noqa: E501
        :rtype: OneOfFieldDefinitionFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this FieldDefinition.

        The display format of the represented field.  # noqa: E501

        :param format: The format of this FieldDefinition.  # noqa: E501
        :type: OneOfFieldDefinitionFormat
        """

        self._format = format

    @property
    def currency(self):
        """Gets the currency of this FieldDefinition.  # noqa: E501

        The name of the currency that will be using when formatting the represented field when the Format property is set to the Currency member of the WFieldFormat enumeration.  # noqa: E501

        :return: The currency of this FieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this FieldDefinition.

        The name of the currency that will be using when formatting the represented field when the Format property is set to the Currency member of the WFieldFormat enumeration.  # noqa: E501

        :param currency: The currency of this FieldDefinition.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def format_pattern(self):
        """Gets the format_pattern of this FieldDefinition.  # noqa: E501

        The custom format pattern for fields that are configured to use a custom format.  # noqa: E501

        :return: The format_pattern of this FieldDefinition.  # noqa: E501
        :rtype: str
        """
        return self._format_pattern

    @format_pattern.setter
    def format_pattern(self, format_pattern):
        """Sets the format_pattern of this FieldDefinition.

        The custom format pattern for fields that are configured to use a custom format.  # noqa: E501

        :param format_pattern: The format_pattern of this FieldDefinition.  # noqa: E501
        :type: str
        """

        self._format_pattern = format_pattern

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
        if issubclass(FieldDefinition, dict):
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
        if not isinstance(other, FieldDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
