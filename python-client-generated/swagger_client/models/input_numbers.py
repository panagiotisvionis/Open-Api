# coding: utf-8

"""
    Prime Factorization API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InputNumbers(object):
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
        'input_numbers': 'list[int]'
    }

    attribute_map = {
        'input_numbers': 'input_numbers'
    }

    def __init__(self, input_numbers=None):  # noqa: E501
        """InputNumbers - a model defined in Swagger"""  # noqa: E501
        self._input_numbers = None
        self.discriminator = None
        self.input_numbers = input_numbers

    @property
    def input_numbers(self):
        """Gets the input_numbers of this InputNumbers.  # noqa: E501


        :return: The input_numbers of this InputNumbers.  # noqa: E501
        :rtype: list[int]
        """
        return self._input_numbers

    @input_numbers.setter
    def input_numbers(self, input_numbers):
        """Sets the input_numbers of this InputNumbers.


        :param input_numbers: The input_numbers of this InputNumbers.  # noqa: E501
        :type: list[int]
        """
        if input_numbers is None:
            raise ValueError("Invalid value for `input_numbers`, must not be `None`")  # noqa: E501

        self._input_numbers = input_numbers

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
        if issubclass(InputNumbers, dict):
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
        if not isinstance(other, InputNumbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
