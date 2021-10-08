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

class CreateConnectionRequest(object):
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
        'session_key': 'str',
        'saml_token': 'str',
        'username': 'str',
        'password': 'str',
        'application_name': 'str'
    }

    attribute_map = {
        'session_key': 'sessionKey',
        'saml_token': 'samlToken',
        'username': 'username',
        'password': 'password',
        'application_name': 'applicationName'
    }

    def __init__(self, session_key=None, saml_token=None, username=None, password=None, application_name=None):  # noqa: E501
        """CreateConnectionRequest - a model defined in Swagger"""  # noqa: E501
        self._session_key = None
        self._saml_token = None
        self._username = None
        self._password = None
        self._application_name = None
        self.discriminator = None
        if session_key is not None:
            self.session_key = session_key
        if saml_token is not None:
            self.saml_token = saml_token
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if application_name is not None:
            self.application_name = application_name

    @property
    def session_key(self):
        """Gets the session_key of this CreateConnectionRequest.  # noqa: E501

        Authenticate using a session key.  # noqa: E501

        :return: The session_key of this CreateConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._session_key

    @session_key.setter
    def session_key(self, session_key):
        """Sets the session_key of this CreateConnectionRequest.

        Authenticate using a session key.  # noqa: E501

        :param session_key: The session_key of this CreateConnectionRequest.  # noqa: E501
        :type: str
        """

        self._session_key = session_key

    @property
    def saml_token(self):
        """Gets the saml_token of this CreateConnectionRequest.  # noqa: E501

        Authenticate using a saml token.  # noqa: E501

        :return: The saml_token of this CreateConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._saml_token

    @saml_token.setter
    def saml_token(self, saml_token):
        """Sets the saml_token of this CreateConnectionRequest.

        Authenticate using a saml token.  # noqa: E501

        :param saml_token: The saml_token of this CreateConnectionRequest.  # noqa: E501
        :type: str
        """

        self._saml_token = saml_token

    @property
    def username(self):
        """Gets the username of this CreateConnectionRequest.  # noqa: E501

        Authenticate username.  # noqa: E501

        :return: The username of this CreateConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateConnectionRequest.

        Authenticate username.  # noqa: E501

        :param username: The username of this CreateConnectionRequest.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this CreateConnectionRequest.  # noqa: E501

        Authenticate password.  # noqa: E501

        :return: The password of this CreateConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateConnectionRequest.

        Authenticate password.  # noqa: E501

        :param password: The password of this CreateConnectionRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def application_name(self):
        """Gets the application_name of this CreateConnectionRequest.  # noqa: E501

        An optional application name that will be used for audit trail.  # noqa: E501

        :return: The application_name of this CreateConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this CreateConnectionRequest.

        An optional application name that will be used for audit trail.  # noqa: E501

        :param application_name: The application_name of this CreateConnectionRequest.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

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
        if issubclass(CreateConnectionRequest, dict):
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
        if not isinstance(other, CreateConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
