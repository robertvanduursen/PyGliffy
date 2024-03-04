import operator, os, re, sys, inspect, time, datetime
import json


# def objectiver(dictToObj,baseName):
# 	'''
# 	loop through the object
# 	convert any dict to object classes
# 	add any non-dict as data to current object class
# 	'''
# 	newTypes = {}
#
# 	# this is a forward unroll -> going into depth only on the object
# 	def unrollDict(thingToParse,  diver =False, subMarine=False, newName=False):
# 		if isinstance(thingToParse, dict):
# 			newTypeName = newName if newName else diver.__name__
# 			if newTypeName not in newTypes.keys():
# 				newType = type(newName if newName else diver.__name__, (object,), dict())
# 			else:
# 				newType = newTypes[newTypeName]
# 			newDiver = newType()
# 			print 'newDiver:', newDiver,newType,'under', subMarine
# 			print subMarine,'&',diver,'&',newDiver
# 			print
# 			if isinstance(subMarine, object) and subMarine is not diver:
# 				setattr(subMarine, newDiver.__class__.__name__, newDiver)
# 				#subMarine = diver
# 				#diver = subMarine
# 				#subMarine = newDiver
#
# 			for name,things in thingToParse.items():
# 				leaf = unrollDict(things, newDiver, diver, str(name)) # final stop
# 				setattr(newDiver, name, leaf)
#
# 		elif isinstance(thingToParse, list):
# 			# todo: ok, dont know how to deal with this exactly
# 			# todo: this hasnt come up yet
# 			newList = []
# 			for y in thingToParse:
# 				newList.append(unrollDict(y, diver, subMarine))
# 			print 'new List',len(newList)
# 			setattr(diver, 'theList', newList)
# 		else:
# 			#print thingToParse, type(thingToParse)
# 			bottomThing = thingToParse
# 			return bottomThing # reached final depth -> leaf node
#
# 		return diver
#
# 	# baseName == first depth, the beach
# 	sub = type(baseName, (object,), dict())
# 	unrollDict(dictToObj, sub, sub, 'testMe') # parse the root
#
# 	#print 'childObj', sub
# 	#for x in sub.__dict__.items(): print '\t', x
#
# 	return sub
#
#
# def removeBrackets(stringIn):
# 	# print 'IN->',stringIn
# 	parsing = False
# 	chunk = []
# 	incr = 0
# 	start = 0
# 	while '<' in stringIn or '>' in stringIn and incr < 500:
# 		if stringIn[incr] == '<':
# 			parsing = True
# 			start = incr
# 		# print 'true @', start
# 		if stringIn[incr] == '>':
# 			parsing = False
# 			# print 'false @', incr
# 			toRemove = stringIn[start:incr + 1]
# 			# print 'toRemove', toRemove
# 			stringIn = stringIn.replace(toRemove, ' ')
# 			# print 'string1 ', string
# 			# reset
# 			incr = 1
# 			start = 0
# 		incr += 1
#
# 	return ' '.join(stringIn.split())

# class Node:
# 	name = False
# 	connections = False
#
# 	def __init__(self,data=False,diagram=False):
# 		if data: self.parse(data)
#
# 	def parse(self,data):
# 		"""
# 		print obj['children'][0]['graphic']['Text']['html']
# 		print removeBrackets(obj['children'][0]['graphic']['Text']['html'])
# 		"""
# 		print('NODE')
# 		# turn dictionaries into objects
# 		for item in data.items():
# 			self.__dict__[item[0]] = item[1]
#
# 		self.newChildren = []
# 		for idx,child in enumerate(self.children):
# 			#print 'child',child
# 			childObj = objectiver(child,'rootObj')
# 			self.newChildren.append(childObj)
#
# 		print 'first child'
# 		print self.newChildren[0]
#
# 		print data['children'][0]
#
# 		for x in data['children'][0]['graphic'].items(): print '\t',x
# 		print
# 		for x in self.newChildren[0].graphic.__dict__.items(): print '\t',x
# 		#for x in self.newChildren[0].testMe.Text.__dict__.items(): print '\t',x
#
# 		# if self.newChildren[0].graphic.type == 'Text':
# 		# 	print 'result',self.newChildren[0].graphic.Text.__dict__.items()
#
# 			#for x in self.newChildren[0].graphic.__dict__.items():
# 				#print '\t',x
# 		raise
# 		#self.name = removeBrackets(data['children'][0]['graphic']['Text']['html'])
# 		#raise
#
#
#
#
#
# 	# for x in data.items(): print '\t',x
#
# 	def new(self):
# 		self.newObj = {
# 			'graphic': {
# 				u'Shape': {u'opacity': 1.0, u'dashStyle': None, u'strokeWidth': 2.0, u'gradient': False,
# 						   u'shadowY': 0.0,
# 						   u'shadowX': 0.0, u'state': 0, u'fillColor': u'#FFFFFF',
# 						   u'tid': u'com.gliffy.stencil.round_rectangle.basic_v1', u'dropShadow': False,
# 						   u'strokeColor': u'#000000'},
# 				u'type': u'Shape'},
# 			'uid': 'com.gliffy.shape.uml.uml_v2.state_machine.state',
# 			'layerId': 'mhOf8ofbecEO',
# 			'children': [{u'graphic': {
# 				u'Text': {u'hposition': u'none', u'linePerpValue': None, u'paddingBottom': 8, u'vposition': u'none',
# 						  u'cardinalityType': None, u'outerPaddingBottom': 2, u'paddingLeft': 8,
# 						  u'html': u'<p style="text-align:center;"><span style="font-size:12px;font-weight:bold;text-decoration:none;font-family:Arial;"><span style="text-decoration:none;">{}<br /></span></span></p>',
# 						  u'outerPaddingTop': 6, u'tid': None, u'outerPaddingLeft': 6, u'paddingTop': 8,
# 						  u'valign': u'middle', u'lineTValue': None, u'overflow': u'none', u'paddingRight': 8,
# 						  u'type': u'fixed', u'outerPaddingRight': 6}, u'type': u'Text'}, u'uid': None,
# 				u'layerId': u'mhOf8ofbecEO', u'height': 28.0, u'hidden': False, u'width': 116.0,
# 				u'lockShape': False, u'lockAspectRatio': False, u'y': 0.0, u'x': 2.0, u'rotation': 0.0,
# 				u'order': u'auto', u'id': 15}],
# 			'height': 50.0,
# 			'hidden': False,
# 			'width': 120.0,
# 			'lockShape': False,
# 			'lockAspectRatio': False,
# 			'y': 2120.0,
# 			'x': 2410.0,
# 			'rotation': 0.0,
# 			'order': 4,
# 			'id': 14,
# 			'linkMap': []
# 		}

class Conn:
	def __init__(self,name,diagram):
		pass

class Gliffy(object):
	path = False
	data = False
	objects = list
	tree = False

	_nodes = False
	_connections = False

	def __init__(self, path=False):
		if path:
			self.path = path
			self.load()
			self.objects = []
			# self.breakDown()
		else:
			self.makeNew()

	stage = False


	def makeNew(self):
		self.data = {
			"contentType": "application/gliffy+json",
			"version": "1.3",
			"stage": {
				"objects": [
					 {"x": 534.0, "y": 124.0, "rotation": 0.0, "id": 37, "width": 120.0, "height": 50.0,
					  "uid": "com.gliffy.shape.uml.uml_v2.state_machine.state", "order": 2, "lockAspectRatio": False,
					  "lockShape": False, "graphic": {"type": "Shape",
													  "Shape": {"tid": "com.gliffy.stencil.round_rectangle.basic_v1",
																"strokeWidth": 2.0, "strokeColor": "#000000",
																"fillColor": "#FFFFFF", "gradient": False,
																"dashStyle": None, "dropShadow": False, "state": 0,
																"opacity": 1.0, "shadowX": 0.0, "shadowY": 0.0}},
					  "linkMap": [], "children": [
						 {"x": 2.0, "y": 0.0, "rotation": 0.0, "id": 38, "width": 116.0, "height": 28.0, "uid": None,
						  "order": 5, "lockAspectRatio": False, "lockShape": False, "graphic": {"type": "Text",
																								"Text": {
																									"overflow": "none",
																									"paddingTop": 8,
																									"paddingRight": 8,
																									"paddingBottom": 8,
																									"paddingLeft": 8,
																									"outerPaddingTop": 6,
																									"outerPaddingRight": 6,
																									"outerPaddingBottom": 2,
																									"outerPaddingLeft": 6,
																									"type": "fixed",
																									"lineTValue": None,
																									"linePerpValue": None,
																									"cardinalityType": None,
																									"html": "<p style=\"text-align:center;\"><span style=\"font-weight:bold;text-decoration:none;font-family:Arial;font-size:12px;\"><span style=\"text-decoration:none;\">Handkeyeded Animation<br /></span></span></p>",
																									"tid": None,
																									"valign": "middle",
																									"vposition": "none",
																									"hposition": "none"}},
						  "children": [], "hidden": False, "layerId": "R6qDJNEC9I4L"}
					 ], "hidden": False,
					  "layerId": "R6qDJNEC9I4L"},


					 {"x": 460.0, "y": 335.0, "rotation": 0.0, "id": 25, "width": 120.0, "height": 50.0,
					  "uid": "com.gliffy.shape.uml.uml_v2.state_machine.state", "order": 32, "lockAspectRatio": False,
					  "lockShape": False, "graphic": {"type": "Shape",
													  "Shape": {"tid": "com.gliffy.stencil.round_rectangle.basic_v1",
																"strokeWidth": 2.0, "strokeColor": "#000000",
																"fillColor": "#FFFFFF", "gradient": False,
																"dashStyle": None, "dropShadow": False, "state": 0,
																"opacity": 1.0, "shadowX": 0.0, "shadowY": 0.0}},
					  "linkMap": [], "children": [
						 {"x": 2.0, "y": 0.0, "rotation": 0.0, "id": 26, "width": 116.0, "height": 14.0, "uid": None,
						  "order": 35, "lockAspectRatio": False, "lockShape": False, "graphic": {"type": "Text",
																								 "Text": {
																									 "overflow": "none",
																									 "paddingTop": 8,
																									 "paddingRight": 8,
																									 "paddingBottom": 8,
																									 "paddingLeft": 8,
																									 "outerPaddingTop": 6,
																									 "outerPaddingRight": 6,
																									 "outerPaddingBottom": 2,
																									 "outerPaddingLeft": 6,
																									 "type": "fixed",
																									 "lineTValue": None,
																									 "linePerpValue": None,
																									 "cardinalityType": None,
																									 "html": "<p style=\"text-align:center;\"><span style=\"font-weight:bold;text-decoration:none;font-family:Arial;font-size:12px;\"><span style=\"text-decoration:none;\">Test<br /></span></span></p>",
																									 "tid": None,
																									 "valign": "middle",
																									 "vposition": "none",
																									 "hposition": "none"}},
						  "children": [], "hidden": False, "layerId": "R6qDJNEC9I4L"}], "hidden": False,
					  "layerId": "R6qDJNEC9I4L"},


					 {"x": 579.0, "y": 314.0, "rotation": 0.0, "id": 20, "width": 100.0, "height": 100.0,
					  "uid": "com.gliffy.shape.uml.uml_v2.use_case.generalization", "order": 46,
					  "lockAspectRatio": False, "lockShape": False, "constraints": {"constraints": [],
																					"startConstraint": {
																						"type": "StartPositionConstraint",
																						"StartPositionConstraint": {
																							"nodeId": 25, "py": 0.0,
																							"px": 0.925}},
																					"endConstraint": {
																						"type": "EndPositionConstraint",
																						"EndPositionConstraint": {
																							"nodeId": 37, "py": 1.0,
																							"px": 0.09166666666666666}}},
					  "graphic": {"type": "Line",
								  "Line": {"strokeWidth": 1.0, "strokeColor": "#000000", "fillColor": "none",
										   "dashStyle": None, "startArrow": 0, "endArrow": 4,
										   "startArrowRotation": "auto", "endArrowRotation": "auto",
										   "interpolationType": "linear", "cornerRadius": None,
										   "controlPath": [[-8.0, -179.0], [166.0, -140.0]], "lockSegments": {},
										   "ortho": False}}, "linkMap": [], "children": [], "hidden": False,
					  "layerId": "R6qDJNEC9I4L"}
				],
				},
			}

	def load(self):
		""" read/import """
		with open(self.path, 'r') as F: self.data = F.read()
		self.tree = json.loads(self.data)
		self._nodes = []
		self._connections = []

	def fileFormat(self):
		format = """
		JSON data
		
		all nodes of the file format can have <embedded resouces> and <metadata>
		
		file
			version: "1.3"
			contentType: "application/gliffy+json"
			metadata
			stage
			embeddedResources

		metadata
			exportBorder: False
			title: 'untitled'
			loadPosition: 'default'
			revision: 0
			autosaveDisabled: False
			libraries', library names (i.e. 'com.gliffy.libraries.flowchart.flowchart_v1.default')
			embeddedResources: more embedded data
			
		stage # main container for the scene
			embeddedResources':  
			imageCache', {}
			maxWidth', 5000)
			textStyles', False
			snapToGrid', True
			shapeStyles', {}
			height', 1137
			gridOn', True
			printGridOn', False
			exportBorder', False
			nodeIndex', 270
			pageBreaksOn', False
			width', 1602
			fitBB', {u'max': {u'y': 1137, u'x': 1602}, u'min': {u'y': 20, u'x': 20}}
			layers', [{u'nodeIndex': 244, u'locked': False, u'name': u'Layer 0', u'vsible': True, u'active': True, u'guid': u'NAaDBq7u7L0g', u'order': 0}]
			printShrinkToFit', False
			background', u'#FFFFFF'
			objects', 
			printModel', 
			printPortrait', False
			lineStyles', {u'global': {}}
			viewportType', u'default'
			autoFit', True
			maxHeight', 5000
			drawingGuidesOn', True
			printPaper', None
			themeData', None
		
		"""
		print(format)

	def save(self, newData=False):
		""" write/export """
		if newData:
			with open(self.path.replace('.gliffy', '_modded.gliffy'), 'w') as F:
				F.write(json.dumps(self.tree))
		else:
			with open(self.path.replace('.gliffy', '_modded.gliffy'), 'w') as F:
				F.write(self.data)

	def saveAs(self, filePath = ''):
		with open(filePath + r'\test.gliffy', 'w') as F:
			F.write(json.dumps(self.data))

	def append(self):
		""" placeholder function """
		pass

	def clear(self):
		""" placeholder function """
		self.tree = self.new()
		self.objects = False
		pass


	def find(self, query):
		""" placeholder function """
		pass

	def findall(self, query):
		""" placeholder function """
		pass

	def getchildren(self):
		""" placeholder function """
		pass


	# def breakDown(self):
	# 	self.objects = self.tree['stage']['objects']
	# 	for obj in self.objects:
	# 		pass
	# 		if 'children' in obj.keys():
	# 			newNode = Node(obj,self)
	# 			pass#self._nodes.append(newNode)
	# 		else:
	# 			newCon = Conn(obj,self)


	# def nodes(self):
	# 	print(len(self.objects))
	# 	for obj in self.objects:
	# 		try:
	# 			# print obj['children'][0]['graphic']['Text']['html']
	# 			print(removeBrackets(obj['children'][0]['graphic']['Text']['html']))
	#
	# 		# print obj['children'][0]['graphic']['Text']['html']#.split('none;">')[1]#.split('</span>')[0]
	# 		except:
	# 			pass  # print 'missed' # <- these will be the connections
	# 		# print obj

	def connections(self):
		pass

	def new(self):
		self.header = {"contentType": "application/gliffy+json",
				  "version": "1.3",
				  "stage":
					  {"background": "#FFFFFF",
					   "width": 'lol'}
				  }

		return self.header

	def addElement(self):
		for newName in ['lets', 'test this theory', 'right now']:
			self.newObj['children'][0]['graphic']['Text']['html'] = self.newObj['children'][0]['graphic']['Text'][
				'html'].format(newName)
			self.tree['stage']['objects'].append(self.newObj)

	def addNode(self):
		pass

	def parse(self):
		import _classes as classes

		if 'objects' in self.tree['stage']:
			# parse objects
			print(len(self.tree['stage']['objects']))
			for obj in self.tree['stage']['objects']:
				if 'constraints' in obj:  # oddly enough, this tag seems the only distinction
					classes.constraints()
					print(obj.keys())
				else:
					print(obj.keys())

	def _parse(self):
		import _classes as classes
		for name, value in self.tree.items():
			if name in dir(classes):
				newObj = eval("classes.%s" % name)()
				newObj.__dict__.update(value)
				self.objects.append(newObj)
				print(name, 'cool')
			else:
				print(name, 'not cool')

		for x in self.objects:
			print(x.__dict__)



def testsuite():
	# https://go.gliffy.com/go/html5/launch
	import webbrowser
	webbrowser.open(r"https://go.gliffy.com/go/html5/launch")



# root = r'C:\Users\rober\Google Drive\Experiments\FileParsing\gliffy\data\short2box1con.gliffy'
# emtpy = Gliffy(root)
# emtpy.parse()

# emtpy = Gliffy()
# emtpy.saveAs(r'C:\Users\rober\Google Drive\Experiments\FileParsing\gliffy\data')



emtpy = Gliffy()
emtpy.parse()