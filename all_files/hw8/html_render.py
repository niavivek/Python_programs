#!/usr/bin/env python

"""
Python class example.
"""

###############################################################################
#######################   Element and Its Sub Classes   #######################
###############################################################################

class Element(object):
	tag_name = ""
	indent = "\t"
	def __init__(self, content = None, **new_attributes):
		if content != None:
			self.content = [content]
		else:
			self.content = []
		self.new_attributes = new_attributes

	def append(self, new_content):
		try:
			self.content.append(new_content)
		except:
			print("Error occured.")
			exit(0)

	def render(self, file_out, ind = ""):
		file_out.write("\n" + ind  + "<" + self.tag_name)
		try:
			if self.new_attributes != "":
				for k,v in self.new_attributes.items():
					file_out.write(" " + k + "=" + "\"" + v + "\"")
		except:
			print("Error")
			exit(0)
		file_out.write(">")
		for items in self.content:
			try:
				if isinstance(items, str):
					file_out.write("\n" + ind + self.indent + items)
				else:
					items.render(file_out, ind + self.indent)
			except:
				print("Error occured.")
				exit(0)
		file_out.write("\n" + ind + "</" + self.tag_name + ">")


class Html(Element):
	tag_name = "html"
	def render(self, file_out, ind = ""):
		file_out.write("<!DOCTYPE html>")
		Element.render(self, file_out, ind)

class Body(Element):
	tag_name = "body"
	
class P(Element):
	tag_name = "p"

class Head(Element):
	tag_name = "head"

class OneLineTag(Element):
	def render(self, file_out, ind = ""):
		file_out.write("\n" + ind  + "<" + self.tag_name)
		try:
			if self.new_attributes != "":
				for k,v in self.new_attributes.items():
					file_out.write(" " + k + "=" + "\"" + v + "\"")
		except:
			print("Error")
			exit(0)
		file_out.write(">")
		for items in self.content:
			try:
				if isinstance(items, str):
					file_out.write(items)
				else:
					items.render(file_out)
			except:
				print("Error occured.")
				exit(0)
		file_out.write("</" + self.tag_name + ">")

class Title(OneLineTag):
	tag_name = "title"

class SelfClosingTag(Element):

	def render(self, file_out, ind = ""):
		file_out.write("\n" + ind  + "<" + self.tag_name)
		try:
			if self.new_attributes != "":
				for k,v in self.new_attributes.items():
					file_out.write(" " + k + "=" + "\"" + v + "\"")
		except:
			print("Error")
			exit(0)
		file_out.write(" />")
		

class Hr(SelfClosingTag):
	tag_name = "hr"

class Br(SelfClosingTag):
	tag_name = "br"

class Meta(SelfClosingTag):
	tag_name = "meta"

class A(OneLineTag):
	tag_name = "a"
	def __init__(self, link, content):
		OneLineTag.__init__(self, content, href=link)


class Ul(Element):
	tag_name = "ul"

class Li(Ul):
	tag_name = "li"


class H(OneLineTag):

	def __init__(self, value, content, **new_attributes):
		self.tag_name = "h" + str(value)
		OneLineTag.__init__(self, content, **new_attributes)
	