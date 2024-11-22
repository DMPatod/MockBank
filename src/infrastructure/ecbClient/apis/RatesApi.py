from datetime import datetime

from src.infrastructure.ecbClient.models.Configuration import Configuration
from src.infrastructure.ecbClient.models.Rate import Rate
from xml.etree import ElementTree

class RatesApi:
    namespaces = {
        'gesmes': 'http://www.gesmes.org/xml/2002-08-01',
        'default': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'
    }

    def __init__(self):
        self.config = Configuration()

    async def api_currency_get_async(self):
        path = "/stats/eurofxref/eurofxref-daily.xml"
        self.config.httpClient.request("GET", path)
        response = self.config.httpClient.getresponse()
        if response.status != 200:
            raise Exception("Failed to get eurofxref request.")
        str_response = response.read().decode("utf-8")
        xml_response = ElementTree.fromstring(str_response)

        result = []

        cube_root = xml_response.find('.//default:Cube[@time]', self.namespaces)
        if cube_root is None:
            raise Exception("eurofxref request is invalid.")

        time = datetime.strptime(cube_root.attrib['time'], "%Y-%m-%d")

        for item in cube_root.findall('default:Cube', self.namespaces):
            result.append(
                Rate(currency=item.attrib['currency'], rate=float(item.attrib['rate']), time=time)
            )

        return result