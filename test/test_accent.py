# coding: utf-8

"""
    Respeecher API

    API for interacting with Respeecher services, including key and session management, and calibration functionalities.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from respeecher.models.accent import Accent

class TestAccent(unittest.TestCase):
    """Accent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Accent:
        """Test Accent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Accent`
        """
        model = Accent()
        if include_optional:
            return Accent(
                id = '',
                is_default = True,
                native = True,
                info = respeecher.models.accent_info.Accent_info(
                    name = '', 
                    short_name = '', 
                    locale = '', ),
                tiers = [
                    respeecher.models.tier.Tier(
                        name = '', )
                    ],
                available = True,
                settings = respeecher.models.settings.settings()
            )
        else:
            return Accent(
        )
        """

    def testAccent(self):
        """Test Accent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
