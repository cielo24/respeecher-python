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

class RecordingListResponse(object):
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
        'list': 'list[Recording]',
        'pagination': 'ProjectListResponsePagination'
    }

    attribute_map = {
        'list': 'list',
        'pagination': 'pagination'
    }

    def __init__(self, list=None, pagination=None):  # noqa: E501
        """RecordingListResponse - a model defined in Swagger"""  # noqa: E501
        self._list = None
        self._pagination = None
        self.discriminator = None
        if list is not None:
            self.list = list
        if pagination is not None:
            self.pagination = pagination

    @property
    def list(self):
        """Gets the list of this RecordingListResponse.  # noqa: E501


        :return: The list of this RecordingListResponse.  # noqa: E501
        :rtype: list[Recording]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this RecordingListResponse.


        :param list: The list of this RecordingListResponse.  # noqa: E501
        :type: list[Recording]
        """

        self._list = list

    @property
    def pagination(self):
        """Gets the pagination of this RecordingListResponse.  # noqa: E501


        :return: The pagination of this RecordingListResponse.  # noqa: E501
        :rtype: ProjectListResponsePagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this RecordingListResponse.


        :param pagination: The pagination of this RecordingListResponse.  # noqa: E501
        :type: ProjectListResponsePagination
        """

        self._pagination = pagination

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
        if issubclass(RecordingListResponse, dict):
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
        if not isinstance(other, RecordingListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
