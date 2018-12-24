import os
import json


def load_data(path):
    data = []
    firma = []

    # Extract the directory of this file...
    base_dir = os.path.dirname(os.path.realpath(__file__))
    # Concatenate the directory with the file name...
    data_file = os.path.join(base_dir, path)
    # Open the file so we can read the data...
    with open(data_file, 'r') as f:
        # For each line in the file...
        d = json.load(f)
        # for i, entry in enumerate(d):
        #     # Append to the list of data...
        #     # print(entry['txtKontaktperson'])
        #     data.append(entry['txtKontaktperson'])
        #     firma.append(entry['txtFirmenname'])
        return d


#print(load_data("C:\\Users\\Stephan\\Google Drive\\BoaVista\\json_file.json"))