"""
utility module for working with Gliffy
"""

import operator, os, re
import json


class Item(object):
    width = float
    height = float

    def __init__(self):
        self.width = 1.0
        self.height = 1.0


class Stage(Item):
    objects = False

    def __init__(self):
        super().__init__()
        self.objects = []

        self.background = '#FFFFFF'
        self.autoFit = True
        self.exportBorder = False
        self.gridOn = True


class Graphic:
    type = 'Shape'
    Shape = False

    def __init__(self, type):
        if type == 'Shape':
            self.Shape = {}
            self.type = 'Shape'
            self.Shape = {'tid': 'com.gliffy.stencil.round_rectangle.basic_v1', 'strokeWidth': 2.0,
                          'strokeColor': '#000000',
                          'fillColor': '#FFFFFF', 'gradient': False, 'dashStyle': None, 'dropShadow': False, 'state': 0,
                          'opacity': 1.0,
                          'shadowX': 0.0, 'shadowY': 0.0}
        if type == 'Text':
            self.Text = {}
            self.type = 'Text'
            self.Text = {'overflow': 'none', 'paddingTop': 8, 'paddingRight': 8, 'paddingBottom': 8, 'paddingLeft': 8,
                         'outerPaddingTop': 6, 'outerPaddingRight': 6, 'outerPaddingBottom': 2, 'outerPaddingLeft': 6,
                         'type': 'fixed', 'lineTValue': None, 'linePerpValue': None, 'cardinalityType': None,
                         'html': '<p style="text-align:center;"><span style="font-weight:bold;text-decoration:none;font-family:Arial;font-size:12px;"><span style="text-decoration:none;">{}<br /></span></span></p>',
                         'tid': None, 'valign': 'middle', 'vposition': 'none', 'hposition': 'none'}

    def serialize(self):
        return self.__dict__

    def setText(self, text):
        self.Text['html'] = self.Text['html'].format(text)  # 'Handkeyed Animation'


class Node(Item):
    id = False
    _text = False

    def __init__(self):
        super().__init__()

        self.hidden = False
        self._text = ''

        self.x = 10.0
        self.y = 10.0
        self.rotation = 0.0
        self.width = 120.0
        self.height = 50.0
        self.children = []

        self.uid = "com.gliffy.shape.uml.uml_v2.state_machine.state"

        # classAttr = [attr for attr in dir(self.__class__) if not attr.startswith('__')]
        # #print(self.__class__.__dict__)
        # for attr in classAttr:
        #     print(attr)
        #     # exec("self.{} = {}".format(attr, self.__class__.__dict__[attr]))

    def serialize(self):
        if hasattr(self, '_text'):
            del self._text
        if hasattr(self, 'graphic'):
            self.graphic = self.graphic.serialize()

        self.children = [child.serialize() for child in self.children]
        return self.__dict__

    def addText(self, text):
        newnode = Node()
        newnode.id = 10
        newnode.graphic = Graphic('Text')
        newnode.graphic.setText(text)
        self.children.append(newnode)


class Link:
    start = False
    end = False


class gliffyData:
    data = False

    def __init__(self, file=False):
        if file:
            self.load(file)

    def load(self, file):
        with open(file) as filedata:
            self.data = json.load(filedata)
            # print(str(self.data).count("'id':"))

    def iter(self, query):
        if query in str(self.data):
            print("found", query)
            print(str(self.data).count("{"))
            print(str(self.data).count("}"))

            import re
            pattern = r"'(.*?)': {(.*?)}"
            for item in re.findall(pattern, str(self.data)):
                print(item)
                print
                print

    @property
    def nodes(self):
        if not isinstance(self.data['stage'], dict):
            if all(isinstance(item, Node) for item in self.data['stage'].objects):
                return self.data['stage'].objects

        items = []
        for item in self.data['stage']['objects']:
            if not 'constraints' in item:
                # print(item)
                # break

                if item['children'][0]['graphic']['type'] == 'Text':
                    itemdata = item['children'][0]['graphic']['Text']['html']
                    # print(itemdata)
                    itemdata = re.search(r'one;">(.*?)<', itemdata)  # .groups()
                    if itemdata is not None:
                        newnode = Node()
                        newnode.id = item['id']
                        newnode._text = itemdata.groups()[0]
                        items.append(newnode)
        return items

    @property
    def links(self):
        items = []
        for item in self.data['stage']['objects']:
            if 'constraints' in item:
                if 'startConstraint' in item['constraints']:
                    newlink = Link()
                    newlink.start = item['constraints']['startConstraint']['StartPositionConstraint']['nodeId']
                    newlink.end = item['constraints']['endConstraint']['EndPositionConstraint']['nodeId']

                    items.append(newlink)

        return items

    def save_as(self, filePath=''):
        if os.path.isdir(filePath):
            path = filePath + r'\test.gliffy'
        else:
            path = filePath

        with open(path, 'w') as F:
            self.data['stage'].objects = [n.serialize() for n in self.nodes]
            self.data['stage'] = self.data['stage'].__dict__
            print(self.data)
            F.write(json.dumps(self.data, sort_keys=True, indent=4))

    def new(self):
        """ a brand new Gliffy """
        self.data = {}

        # self.data['contentType'] = "application/gliffy+json"
        # self.data['version'] = "1.3"
        # self.data['metadata'] = {'title': 'test', 'revision': 0}
        # self.data['embeddedResources'] = {'index': 0, 'resources': []}

        self.data['stage'] = Stage()

    def addNode(self, name):
        newnode = Node()
        newnode.id = len(self.nodes)
        newnode._text = name
        newnode.graphic = Graphic('Shape')
        newnode.addText(name)
        self.data['stage'].objects.append(newnode)

    def addLink(self, nodeFrom, nodeTo):
        pass

    def connect_nodes_by_name(self, nodeFrom, nodeTo):
        pass

    def connect_nodes_by_id(self, nodeFrom, nodeTo):
        pass
