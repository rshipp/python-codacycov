"""Submit Python coverage report to Codacy."""

import sys
from xml.dom import minidom

import requests


XML_DOC = 'coverage.xml'
URL = 'https://www.codacy.com/api/coverage/{token}/{commit}'


def main(token, commit, xml_file=XML_DOC):
    """Parse XML file and POST it to the Codacy API"""

    # Convert decimal string to floored int percent value
    percent = lambda s: int(float(s)*100)

    # Parse the XML into the format expected by the API
    xmldoc = minidom.parse(xml_file)

    data = {
        'total': percent(xmldoc.getElementsByTagName('coverage')[0].attributes['line-rate'].value),
        'fileReports': [],
    }

    classes = xmldoc.getElementsByTagName('class')
    for cls in classes:
        file_report = {
            'filename': cls.attributes['filename'].value,
            'total': percent(cls.attributes['line-rate'].value),
            'coverage': {},
        }
        lines = cls.getElementsByTagName('line')
        for line in lines:
            hits = int(line.attributes['hits'].value)
            if hits >= 1:
                # The API assumes 0 if a line is missing
                file_report['coverage'][line.attributes['number'].value] = hits
        data['fileReports'] += [file_report]

    # Try to send the data, raise an exception if we fail
    r = requests.post(URL.format(token=token, commit=commit), data=data)
    r.raise_for_status()


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 3:
        print("usage: codacycov.py TOKEN COMMIT [COVERAGE_XML]")
        print("if COVERAGE_XML is not specified, default is coverage.xml")
    elif argc < 4:
        main(sys.argv[1], sys.argv[2])
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
