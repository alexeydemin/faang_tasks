# from solution import parse_csv
import csv
import io
from unittest import TestCase

TestCase.maxDiff = None


def parse_csv(csv_string: str, separator: str = ',', quote: str = '"') -> list:
    if not csv_string:
        return [['']]
    csvfile = io.StringIO(csv_string)
    myreader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
    res = []
    for row in myreader:
        res.append(row)
    return res


class TestExampleTests(TestCase):
    def test_should_handle_simple_inputs(self):
        "should handle simple inputs"
        self.assertEqual(parse_csv("1,2,3\n4,5,6", ",", "\""), [["1", "2", "3"], ["4", "5", "6"]])

    def test_should_handle_quoted_fields(self):
        "should handle quoted fields"
        self.assertEqual(parse_csv("1,\"two was here\",3\n4,5,6", ",", "\""),
                         [["1", "two was here", "3"], ["4", "5", "6"]])

    def test_should_handle_alternate_separators(self):
        "should handle alternate separators"
        self.assertEqual(parse_csv("1\t2\t3\n4\t5\t6", "\t", "\""), [["1", "2", "3"], ["4", "5", "6"]])

    def test_should_handle_an_empty_file(self):
        "should handle an empty file"
        self.assertEqual(parse_csv("", ",", "\""), [[""]])
