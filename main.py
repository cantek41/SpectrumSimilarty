import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import datetime

from Similarty.FactorySimilarity import SimilarityFactory, SIMILARITY

Similarty = []


def createGraph(n, _mean):
    G = nx.Graph()
    s = n.shape[0]
    col = n.shape[0]
    for i in range(s):
        # G.add_node((n[i][0], n[i][1]))
        for j in range(i + 1, s):
            toplam = 0
            for k in range(col):
                toplam += abs(n[i] - n[j])
            if toplam < _mean:
                G.add_edge((n[i], n[j]), (n[j], n[i]))
    return G


def preperForGraph(dd):
    aa = np.array(dd)
    bb = aa.ravel()
    new_a = np.sort(bb)[::-1][0:100]
    _mean = np.mean(new_a)
    # print(new_a)
    # print("ortalama: ", _mean)
    G = createGraph(new_a, _mean)
    # print("vertex sayısı: ", G.number_of_nodes())
    return G


def element_ToGraph():
    import os
    pathFolder = "data/"
    filesArray = [x for x in os.listdir(pathFolder) if os.path.isfile(os.path.join(pathFolder, x))]
    destinationFolder = "db/"
    if not os.path.exists(destinationFolder):
        os.mkdir(destinationFolder)
    for file_name in filesArray:
        start = datetime.datetime.now()
        print("*********************************************")
        print("start Time:", start)
        file_name_no_extension = os.path.splitext(file_name)[0]
        print(file_name_no_extension)
        dd = pd.read_csv('data/' + file_name_no_extension + ".csv", usecols=['Sum'])
        G = preperForGraph(dd)
        end = datetime.datetime.now()
        diff = end - start
        print("Create Graph", file_name_no_extension, "time: ", diff.days * 86400 + diff.seconds, "second")

        print("==========================================")
        start = datetime.datetime.now()
        nx.write_gml(G, destinationFolder + file_name_no_extension + ".gml")
        end = datetime.datetime.now()
        diff = end - start
        print("element_ToGraph", file_name_no_extension, "time: ", diff.days * 86400 + diff.seconds, "second")


def similarty(graph1, graph2):
    print("==========================================")
    start = datetime.datetime.now()
    similartyEigenvector = SimilarityFactory.create(SIMILARITY.Eigenvector, graph1, graph2)
    sim = similartyEigenvector.getSimilarity()
    end = datetime.datetime.now()
    diff = end - start
    print("Eigenvector benzerlik oranı", sim, "time: ", (diff.days * 86400000) +
          diff.seconds, "second")

    print("==========================================")
    start = datetime.datetime.now()
    similartyCos = SimilarityFactory.create(SIMILARITY.Cosinus, graph1, graph2)
    sim = similartyCos.getSimilarity()
    end = datetime.datetime.now()
    diff = end - start
    print("Cos benzerlik oranı", sim, "time: ", (diff.days * 86400000) +
          diff.seconds, "second")


def test():
    Similarty.clear()
    import os
    pathFolder = "test/"
    test_filesArray = [x for x in os.listdir(pathFolder) if os.path.isfile(os.path.join(pathFolder, x))]
    destinationFolder = "db/"
    db_filesArray = [x for x in os.listdir(destinationFolder) if os.path.isfile(os.path.join(destinationFolder, x))]
    for file_name in test_filesArray:
        print("==========================================")
        print("Test", "\t", "Target", "\t", "EigSim", "\t", "cosSim")
        for db in db_filesArray:
            dd = pd.read_csv(pathFolder + file_name, usecols=['Sum'])
            G = preperForGraph(dd)
            G1 = nx.read_gml(destinationFolder + db)
            similartyEigenvector = SimilarityFactory.create(SIMILARITY.Eigenvector, G, G1)
            EigSim = similartyEigenvector.getSimilarity()
            similartyCos = SimilarityFactory.create(SIMILARITY.Cosinus, G, G1)
            cosSim = similartyEigenvector.getSimilarity()
            # Similarty.append([file_name, db, EigSim, cosSim])
            print(file_name, "\t", db, "\t",EigSim, "\t\t", cosSim)
            print("----------------------------------------------")


def printSim():
    print("==========================================")
    print(Similarty[0])


# aa = np.arange(15).reshape(5, 3)
# aa = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [8, 10, 11], [9, 10, 11]])


# element_ToGraph()
# G = nx.read_gml('db/Cll.gml')
# dd = pd.read_csv("test/Fe.csv", usecols=['Sum'])
# G = preperForGraph(dd)
# G1 = nx.read_gml('db/All.gml')
# similarty(G, G1)
# nx.draw_networkx(G, with_labels=False, node_size=50)
# plt.show()
test()
