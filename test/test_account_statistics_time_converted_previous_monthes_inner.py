# coding: utf-8

"""
    Respeecher API

    API for interacting with Respeecher services, including key and session management, and calibration functionalities.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from respeecher.models.account_statistics_time_converted_previous_monthes_inner import AccountStatisticsTimeConvertedPreviousMonthesInner

class TestAccountStatisticsTimeConvertedPreviousMonthesInner(unittest.TestCase):
    """AccountStatisticsTimeConvertedPreviousMonthesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountStatisticsTimeConvertedPreviousMonthesInner:
        """Test AccountStatisticsTimeConvertedPreviousMonthesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountStatisticsTimeConvertedPreviousMonthesInner`
        """
        model = AccountStatisticsTimeConvertedPreviousMonthesInner()
        if include_optional:
            return AccountStatisticsTimeConvertedPreviousMonthesInner(
                month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                duration = 56
            )
        else:
            return AccountStatisticsTimeConvertedPreviousMonthesInner(
        )
        """

    def testAccountStatisticsTimeConvertedPreviousMonthesInner(self):
        """Test AccountStatisticsTimeConvertedPreviousMonthesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
