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

class FolderRequest(object):
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
        'project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'project_id': 'project_id'
    }

    def __init__(self, name=None, project_id=None):  # noqa: E501
        """FolderRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._project_id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id

    @property
    def name(self):
        """Gets the name of this FolderRequest.  # noqa: E501


        :return: The name of this FolderRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderRequest.


        :param name: The name of this FolderRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this FolderRequest.  # noqa: E501


        :return: The project_id of this FolderRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this FolderRequest.


        :param project_id: The project_id of this FolderRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

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
        if issubclass(FolderRequest, dict):
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
        if not isinstance(other, FolderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
