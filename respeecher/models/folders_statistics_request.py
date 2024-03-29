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

class FoldersStatisticsRequest(object):
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
        'folder_ids': 'list[str]'
    }

    attribute_map = {
        'folder_ids': 'folder_ids'
    }

    def __init__(self, folder_ids=None):  # noqa: E501
        """FoldersStatisticsRequest - a model defined in Swagger"""  # noqa: E501
        self._folder_ids = None
        self.discriminator = None
        if folder_ids is not None:
            self.folder_ids = folder_ids

    @property
    def folder_ids(self):
        """Gets the folder_ids of this FoldersStatisticsRequest.  # noqa: E501


        :return: The folder_ids of this FoldersStatisticsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._folder_ids

    @folder_ids.setter
    def folder_ids(self, folder_ids):
        """Sets the folder_ids of this FoldersStatisticsRequest.


        :param folder_ids: The folder_ids of this FoldersStatisticsRequest.  # noqa: E501
        :type: list[str]
        """

        self._folder_ids = folder_ids

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
        if issubclass(FoldersStatisticsRequest, dict):
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
        if not isinstance(other, FoldersStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
