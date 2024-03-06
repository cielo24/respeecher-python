# coding: utf-8

"""
    Respeecher API

    API for interacting with Respeecher services, including key and session management, and calibration functionalities.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from respeecher.models.project_request import ProjectRequest

class TestProjectRequest(unittest.TestCase):
    """ProjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectRequest:
        """Test ProjectRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectRequest`
        """
        model = ProjectRequest()
        if include_optional:
            return ProjectRequest(
                name = '',
                owner = '',
                models = None
            )
        else:
            return ProjectRequest(
        )
        """

    def testProjectRequest(self):
        """Test ProjectRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
