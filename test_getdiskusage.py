import unittest
from getdiskusage import output_json_string_from_path, is_good_path
import json

expected_json = {'files': [{'bytes': 2, 'path': './test/bar'}, {'bytes': 1, 'path': './test/foo'},
                           {'bytes': 3, 'path': './test/buzz'}]}


class TestGetDiskUsage(unittest.TestCase):

    def test_user_input(self):
        self.assertTrue(is_good_path("./test"))
        self.assertRaises(ValueError, is_good_path, "./fakeDirectory")

    def test_output_input(self):
        self.assertTrue(output_json_string_from_path("./test"))
        self.assertRaises(ValueError, output_json_string_from_path, "./fakeDirectory")

    def test_nested_directory(self):
        loaded_json = json.loads(output_json_string_from_path("./test/nested"))
        path = loaded_json["files"][0]["path"]
        byte = loaded_json["files"][0]["bytes"]
        self.assertEqual(path, "./test/nested/nestedfile")
        self.assertEqual(byte, 5)

    def test_correct_output_for_multiple_files(self):
        loaded_json = json.loads(output_json_string_from_path("./test"))
        self.assertEqual(loaded_json, expected_json)


if __name__ == '__main__':
    unittest.main()
