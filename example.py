import os, gliffy_datastructure

if __name__ == '__main__':

    path = os.path.dirname(__file__)
    root = os.path.join(path, 'data')

    file = os.path.join(root, 'Dependencies.gliffy')
    test = gliffy_datastructure.gliffyData(file)
    nodeDict ={n.id: n._text for n in test.nodes}
    print(len(test.nodes))
    for item in test.nodes:
        print(item.id, item._text)

    print()
    for item in test.links:
        if item.start in nodeDict and item.end in nodeDict:
            print("%s --> %s" % (nodeDict[item.start],nodeDict[item.end]))
    print()

    # Or, write a completely new
    glif = gliffy_datastructure.gliffyData()
    glif.new()
    glif.addNode('foo')
    glif.addNode('bar')
    glif.connect_nodes_by_name('bar')
    for item in glif.nodes:
        print(item.id, item._text)

    newFile = os.path.join(root, 'cleanGen.gliffy')
    glif.save_as(newFile)


    test = gliffy_datastructure.gliffyData(newFile)
    nodeDict ={n.id: n._text for n in test.nodes}
    print(len(test.nodes))
    for item in test.nodes:
        print(item.id, item._text)

    print()
    for item in test.links:
        if item.start in nodeDict and item.end in nodeDict:
            print("%s --> %s" % (nodeDict[item.start],nodeDict[item.end]))
    print()