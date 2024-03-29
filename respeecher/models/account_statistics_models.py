# coding: utf-8

"""
    Respeecher API

    API for interacting with Respeecher services, including key and session management, and calibration functionalities.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountStatisticsModels(object):
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
        'id': 'str',
        'name': 'str',
        'conversions_count': 'int',
        'converted_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'conversions_count': 'conversions_count',
        'converted_time': 'converted_time'
    }

    def __init__(self, id=None, name=None, conversions_count=None, converted_time=None):  # noqa: E501
        """AccountStatisticsModels - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._conversions_count = None
        self._converted_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if conversions_count is not None:
            self.conversions_count = conversions_count
        if converted_time is not None:
            self.converted_time = converted_time

    @property
    def id(self):
        """Gets the id of this AccountStatisticsModels.  # noqa: E501


        :return: The id of this AccountStatisticsModels.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountStatisticsModels.


        :param id: The id of this AccountStatisticsModels.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AccountStatisticsModels.  # noqa: E501


        :return: The name of this AccountStatisticsModels.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountStatisticsModels.


        :param name: The name of this AccountStatisticsModels.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def conversions_count(self):
        """Gets the conversions_count of this AccountStatisticsModels.  # noqa: E501


        :return: The conversions_count of this AccountStatisticsModels.  # noqa: E501
        :rtype: int
        """
        return self._conversions_count

    @conversions_count.setter
    def conversions_count(self, conversions_count):
        """Sets the conversions_count of this AccountStatisticsModels.


        :param conversions_count: The conversions_count of this AccountStatisticsModels.  # noqa: E501
        :type: int
        """

        self._conversions_count = conversions_count

    @property
    def converted_time(self):
        """Gets the converted_time of this AccountStatisticsModels.  # noqa: E501


        :return: The converted_time of this AccountStatisticsModels.  # noqa: E501
        :rtype: int
        """
        return self._converted_time

    @converted_time.setter
    def converted_time(self, converted_time):
        """Sets the converted_time of this AccountStatisticsModels.


        :param converted_time: The converted_time of this AccountStatisticsModels.  # noqa: E501
        :type: int
        """

        self._converted_time = converted_time

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
        if issubclass(AccountStatisticsModels, dict):
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
        if not isinstance(other, AccountStatisticsModels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
