dataSources = ("http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data","http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test")

def downloadSource(path='dataset', urls=dataSources):
    if not os.path.exists(path):
        os.mkdir(path)

    for url in urls:
        response = requests.get(url)
        name = os.path.basename(url)
        with open(os.path.join(path, name), 'wb') as f:
            f.write(response.content)
