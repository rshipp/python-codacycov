import unittest
import codacy.reporter
import json

class ReporterTests(unittest.TestCase):

  def test_parser(self):
    def file_get_contents(filename):
      with open(filename) as f:
        return f.read()

    jsonContent = file_get_contents('tests/coverage.json')
    expected = json.loads(jsonContent)

    generated = codacy.reporter.parse_report_file('tests/cobertura.xml')
    self.assertEqual(generated, expected)

if __name__ == '__main__':
    unittest.main()
