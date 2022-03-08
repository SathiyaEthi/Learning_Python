import unittest
import datetime
import DateDiffCalc


class TestDateDiffCalc(unittest.TestCase):

    def test_date_diff(self):
        first_date = "01/01/2022"
        last_date = "01/02/2022"
        result = DateDiffCalc.final(first_date, last_date)
        self.assertEqual(result, (
                datetime.datetime.strptime(last_date, "%d/%m/%Y") - datetime.datetime.strptime(first_date,
                                                                                               "%d/%m/%Y")).days,
                         "Valid Input date difference Result should be 31")

    def test_oneday_diff(self):
        first_date = "01/01/2022"
        last_date = "02/01/2022"
        result = DateDiffCalc.final(first_date, last_date)
        self.assertEqual(result, (
                datetime.datetime.strptime(last_date, "%d/%m/%Y") - datetime.datetime.strptime(first_date,
                                                                                               "%d/%m/%Y")).days,
                         "Valid Input date difference.Result should be 1")

    def test_same_day_diff(self):
        first_date = "01/01/2022"
        last_date = "01/01/2022"
        result = DateDiffCalc.final(first_date, last_date)
        self.assertEqual(result, (
                datetime.datetime.strptime(last_date, "%d/%m/%Y") - datetime.datetime.strptime(first_date,
                                                                                               "%d/%m/%Y")).days,
                         "Valid Input date difference Result should be 0")

    def test_leapyear_diff(self):
        first_date = "01/01/2000"
        last_date = "01/01/2001"
        result2 = DateDiffCalc.final(first_date, last_date)
        self.assertEqual(result2, (
                datetime.datetime.strptime(last_date, "%d/%m/%Y") - datetime.datetime.strptime(first_date,
                                                                                               "%d/%m/%Y")).days,
                         "Valid Input date difference Result should be 366")

    def test_invalid_month_exception(self):
        first_date = "01/13/2000"
        with self.assertRaises(ValueError):
            result = DateDiffCalc.verify_date_format(DateDiffCalc.dateformat(first_date))

    def test_invalid_date(self):
        first_date = "32/1/2000"
        with self.assertRaises(ValueError):
            result = DateDiffCalc.verify_date_format(DateDiffCalc.dateformat(first_date))

    def test_invalid_year(self):
        first_date = "01/12/20000"
        with self.assertRaises(ValueError):
            result = DateDiffCalc.verify_date_format(DateDiffCalc.dateformat(first_date))

    def test_wrong_date_order_exception(self):
        first_date = "01/1/2000"
        last_date = "31/12/1999"
        with self.assertRaises(ValueError):
            result = DateDiffCalc.input_date_validation(DateDiffCalc.dateformat(first_date),
                                                        DateDiffCalc.dateformat(last_date))

    def test_date_format_exception(self):
        first_date = "233/012/20221"
        with self.assertRaises(ValueError):
            result = DateDiffCalc.verify_date_format(DateDiffCalc.dateformat(first_date))


if __name__ == '__main__':
    unittest.main()
