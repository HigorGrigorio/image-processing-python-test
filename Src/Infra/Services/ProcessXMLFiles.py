import Src.Core.Infra.Service as ContractService
from Src.Core.Logic import success, fail, Result
from Src.Infra.Database.Contracts.ImageRepo import ImageRepo
from typing import TypedDict
import xml.etree.ElementTree as et


class ProcessXMLFileProps(TypedDict):
    file: str


class ProcessXMLFile(ContractService[ProcessXMLFileProps]):
    def __init__(
            self,
            repo: ImageRepo
    ):
        self.__repo = repo

    @classmethod
    def __remove_extension(cls, file: str) -> str:
        split = file.split('/')
        return split[len(split) - 1].split('.')[0]

    @classmethod
    def __find(cls, attr: str):
        schema = 'http://www.gisplan.com.br/xmlsat'
        return f'{{{schema}}}{attr}'

    def execute(self, args: ProcessXMLFileProps) -> Result:
        try:
            # Parse the XML file
            tree = et.parse(args['file'])
            root = tree.getroot()

            # Define the namespace dictionary
            namespace = {'ns': 'http://www.gisplan.com.br/xmlsat'}

            # Access the sunPosition element
            sun_position = root.find('.//ns:sunPosition', namespace)
            sun_elevation = sun_position.find('ns:elevation', namespace).text
            sun_azimuth = sun_position.find('ns:sunAzimuth', namespace).text

            # Access the viewing:begin element
            viewing_begin = root.find('.//ns:viewing/ns:begin', namespace)

            self.__repo.create({
                'id': f'{self.__remove_extension(args["file"])}',
                'date_acquired': viewing_begin.text,
                'azimuth': sun_azimuth,
                'sun_elevation': sun_elevation
            })

            return success()

        except Exception as e:
            return fail({
                'message': 'Error reading XML file',
                'error': {
                    'type': type(e).__name__,
                    'message': str(e)
                }
            })
