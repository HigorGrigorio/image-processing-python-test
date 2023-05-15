import Src.Core.Infra.Service as ContractService
from Src.Core.Logic import success, fail, Result
from Src.Infra.Database.Contracts.ImageRepo import ImageRepo
from typing import TypedDict
import pandas


class ProcessCSVFileProps(TypedDict):
    file: str


class ProcessCSVFile(ContractService[ProcessCSVFileProps]):
    def __init__(
            self,
            repo: ImageRepo
    ):
        self.__repo = repo

    @classmethod
    def __remove_extension(cls, file: str) -> str:
        split = file.split('/')
        return split[len(split) - 1].split('.')[0]

    def execute(self, args: ProcessCSVFileProps) -> Result:
        try:
            # Read the file
            pd = pandas.read_csv(args['file'])

            # Strip all header of file
            pd = pd.applymap(lambda x: x.strip() if type(x) is str else x)

            # Extract columns
            cols = ['Date Acquired', 'Sun Azimuth L1', 'Sun Elevation L1']
            selected = pd[cols]

            for index, row in selected.iterrows():
                self.__repo.create({
                    'id': f'{self.__remove_extension(args["file"])}-{index}]',
                    'date_acquired': row['Date Acquired'],
                    'azimuth': row['Sun Azimuth L1'],
                    'sun_elevation': row['Sun Elevation L1']
                })

            return success()
        except Exception as e:
            return fail({
                'message': 'Error reading CSV file',
                'error': {
                    'type': type(e).__name__,
                    'message': str(e)
                }
            })
