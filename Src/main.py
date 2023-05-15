from Core.Domain.Validation import ValidationException
from Infra.Services import ProcessCSVFile
from Infra.Services import ProcessXMLFile
from Infra.Database.InMemory import InMemoryImageRepo
import os

data_folder = './Src/Data/'

# Select all name on files in data folder

files = [
    os.path.join(data_folder, name) for name in os.listdir(data_folder) if
    os.path.isfile(os.path.join(data_folder, name))
]

try:
    # Image repository in memory to stores all images
    repo = InMemoryImageRepo()

    # CSV processor
    xml_processor = ProcessXMLFile(repo)

    # XML processor
    csv_processor = ProcessCSVFile(repo)

    for file in files:
        if file.endswith('.csv'):
            csv_processor.execute({'file': file})

        if file.endswith('.xml'):
            xml_processor.execute({'file': file})

    images = repo.all()

    if images:
        for image in images.get():
            print(image)

except ValidationException as e:
    print(e)
