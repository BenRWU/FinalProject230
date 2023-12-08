import os
import requests

#sourcedata
dataSource = ("http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data","http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test")

def downloadSource(path='dataset', urls=dataSource):
    if not os.path.exists(path):
        os.mkdir(path)

    for i, url in enumerate(urls):
        response = requests.get(url)
        #save as adult 1 and 2
        filename = f'adult{i + 1}.csv'
        with open(os.path.join(path, filename), 'wb') as f:
            f.write(response.content)

downloadSource()
