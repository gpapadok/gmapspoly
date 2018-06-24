

class Point:
	
	type_name = 'Point'

	def __init__(self, name, coords):
		self.name = name
		self.coords = coords

	def getJSvar(self):
		jsvar = ''
		ind = 0
		while(1):
			jsvar += '{lng: '
			p1 = self.coords.find(',', ind)
			jsvar += self.coords[ind:p1].strip()
			ind = p1 + 1
			p1 = self.coords.find(',', ind)
			jsvar += ', lat: ' + self.coords[ind:p1] + '}'
			p1 = self.coords.find('\n', ind)
			ind = p1 + 1
			if self.coords.find(',', ind) == -1: break
			jsvar += ',\n'
		
		return jsvar


class Polygon:

	type_name = 'Polygon'

	def __init__(self, name, coords):
		self.name = name
		self.coords = coords

	def getJSpoint(self):
		jsvar = ''
		jsvar += '{lng: '
		p1 = self.coords.find(',')
		jsvar += self.coords[:p1].strip()
		p2 = self.coords.find(',', p1+1)
		jsvar += ', lat: ' + self.coords[p1+1:p2] + '}'
		return jsvar

	def getJSvar(self):
		jsvar = ''
		ind = 0
		while(1):
			jsvar += '{lng: '
			p1 = self.coords.find(',', ind)
			jsvar += self.coords[ind:p1].strip()
			ind = p1 + 1
			p1 = self.coords.find(',', ind)
			jsvar += ', lat: ' + self.coords[ind:p1] + '}'
			p1 = self.coords.find('\n', ind)
			ind = p1 + 1
			if self.coords.find(',', ind) == -1: break
			jsvar += ',\n'

		return jsvar


class KMLPlacemark:


	def __init__(self, kml_file):
		with open(kml_file) as f:
			kml_str = f.read()

		numOfP = self.countPlacemarks(kml_str)
		self.placemarks = [None for x in range(numOfP)]


		ind = 0
		i = 0
		for j in self.placemarks:

			p1 = kml_str.find('<Placemark>', ind)
			if p1 == -1: break
			p2 = kml_str.find('</Placemark>', p1)
			if p2 == -1: break
			kml_p = kml_str[p1+11:p2]

			self.placemarks[i] = self.parsekml(kml_p)

			i += 1
			ind = p2

	def countPlacemarks(self, kml_str):
		ind = 0
		numOfP = 0
		while(1):
			p1 = kml_str.find('</Placemark>', ind)
			ind = p1 + 12
			if p1 == -1: break
			numOfP += 1
		return numOfP

	def parsekml(self, kml_block):
		p1 = kml_block.find('<name>')
		p2 = kml_block.find('</name>')
		name = kml_block[p1+6:p2]

		p1 = kml_block.find('<coordinates>')
		p2 = kml_block.find('</coordinates>')
		coords = kml_block[p1+13:p2]

		poly = kml_block.find('<Polygon>')
		point = kml_block.find('<Point>')

		if poly > 0:
			return Polygon(name, coords)
		elif point > 0:
			return Point(name, coords)

	def getcoordinates(self, polyname):
		for mark in self.placemarks:
			if (mark.name == polyname and mark.type_name == 'Polygon'):
				poly = mark.getJSvar()
				point = mark.getJSpoint()
				return [point, poly]
