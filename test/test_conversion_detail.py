# coding: utf-8

"""
    Respeecher API

    API for interacting with Respeecher services, including key and session management, and calibration functionalities.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from respeecher.models.conversion_detail import ConversionDetail

class TestConversionDetail(unittest.TestCase):
    """ConversionDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConversionDetail:
        """Test ConversionDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConversionDetail`
        """
        model = ConversionDetail()
        if include_optional:
            return ConversionDetail(
                voice_id = '',
                narration_style_id = '',
                accent_id = '',
                semitones_correction = 56,
                label = ''
            )
        else:
            return ConversionDetail(
        )
        """

    def testConversionDetail(self):
        """Test ConversionDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()