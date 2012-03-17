#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
'''
This module includes the elements found in http://www.w3.org/TR/SVG/struct.html

(C) 2008, 2009 Kerim Mansour
For licensing information please refer to license.txt
'''
from attributes import *
from core import BaseElement, PointAttrib, DimensionAttrib


  
        
class g(BaseElement, CoreAttrib, ConditionalAttrib, StyleAttrib, ExternalAttrib, PresentationAttributes_All, GraphicalEventsAttrib):
    """
    Class representing the g element of an svg doc.
    """
    def __init__(self, **kwargs):
        BaseElement.__init__(self, 'g')
        self.setKWARGS(**kwargs)
    
    def set_transform(self, transform):
        self._attributes['transform'] = transform
    def get_transform(self):
        return self._attributes.get('transform')   

class defs(g):
    """
    Class representing the defs element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'defs')
	self.set_id('defs4')
        self.setKWARGS(**kwargs)

    def set_id(self, value):
	self._attributes['id'] = value

    def get_id(self):
	return self._attributes['id']

class desc(BaseElement, CoreAttrib, StyleAttrib):
    """
    Class representing the desc element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'desc')
        self.setKWARGS(**kwargs)

class title(desc):
    """
    Class representing the title element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'title')
        self.setKWARGS(**kwargs)

class rdfEl(BaseElement, CoreAttrib):
    """
    Class representing the rdf element of metadata element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'rdf:RDF')
        self.setKWARGS(**kwargs)

class ccEl(BaseElement, CoreAttrib):
    """
    Class representing the cc element of metadata element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'cc:Work')
	self.set_rdf_about('')
        self.setKWARGS(**kwargs)

    def set_rdf_about(self, value):
	self._attributes['rdf:about'] = value

    def get_rdf_about(self):
	return self._attributes['rdf:about']

class dcformatEl(BaseElement, CoreAttrib):
    """
    Class representing the dc:format element of metadata element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'dc:format')
	self.appendTextContent('image/svg+xml')
        self.setKWARGS(**kwargs)

class dctypeEl(BaseElement, CoreAttrib):
    """
    Class representing the dc:type element of metadata element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'dc:type')
	self.set_rdf_resource('http://purl.org/dc/dcmitype/StillImage')
        self.setKWARGS(**kwargs)

    def set_rdf_resource(self, value):
	self._attributes['rdf:resource'] = value

    def get_rdf_resource(self):
	return self._attributes['rdf:resource']

class dctitleEl(BaseElement, CoreAttrib):
    """
    Class representing the dc:format element of metadata element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'dc:title')
	self.appendTextContent('image/svg+xml')
        self.setKWARGS(**kwargs)

class metadata(BaseElement, CoreAttrib):
    """
    Class representing the metadata element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'metadata')
	self.set_id('metadata11')
        self.setKWARGS(**kwargs)

    def set_id(self, value):
	self._attributes['id'] = value

    def get_id(self):
	return self._attributes['id']

class sodipodiNamedViewEl(BaseElement, CoreAttrib):
    """
    Class representing the sodipodi:namedview element of an svg doc.

    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'sodipodi:namedview')
	self.set_pagecolor('#ffffff')
	self.set_bordercolor('#666666')
	self.set_borderopacity('1')
	self.set_objecttolerance('10')
	self.set_gridtolerance('10')
	self.set_guidetolerance('10')
	self.set_inkscape_pageopacity('0')
	self.set_inkscape_pageshadow('2')
	self.set_inkscape_window_width('640')
	self.set_inkscape_window_height('480')
	self.set_id('base')
	self.set_showgrid('false')
	self.set_inkscape_zoom('1.0000000')
	self.set_inkscape_cx('160.0000')
	self.set_inkscape_cy('1010.000')
	self.set_inkscape_window_x('0')
	self.set_inkscape_window_y('24')
	self.set_inkscape_window_maximized('0')
	self.set_inkscape_current_layer('svg2')
        self.setKWARGS(**kwargs)

    def set_id(self, value):
	self._attributes['id'] = value

    def get_id(self):
	return self._attributes['id']

    def set_pagecolor(self, value):
	self._attributes['pagecolor'] = value

    def get_pagecolor(self):
	return self._attributes['pagecolor']

    def set_bordercolor(self, value):
	self._attributes['bordercolor'] = value

    def get_bordercolor(self):
	return self._attributes['bordercolor']

    def set_borderopacity(self, value):
	self._attributes['borderopacity'] = value

    def get_borderopacity(self):
	return self._attributes['borderopacity']

    def set_objecttolerance(self, value):
	self._attributes['objecttolerance'] = value

    def get_objecttolerance(self):
	return self._attributes['objecttolerance']

    def set_gridtolerance(self, value):
	self._attributes['gridtolerance'] = value

    def get_gridtolerance(self):
	return self._attributes['gridtolerance']

    def set_guidetolerance(self, value):
	self._attributes['guidetolerance'] = value

    def get_guidetolerance(self):
	return self._attributes['guidetolerance']

    def set_inkscape_pageopacity(self, value):
	self._attributes['inkscape:pageopacity'] = value

    def get_inkscape_pageopacity(self):
	return self._attributes['inkscape:pageopacity']

    def set_inkscape_pageshadow(self, value):
	self._attributes['inkscape:pageshadow'] = value

    def get_inkscape_pageshadow(self):
	return self._attributes['inkscape:pageshadow']

    def set_inkscape_window_width(self, value):
	self._attributes['inkscape:window-width'] = value

    def get_inkscape_window_width(self):
	return self._attributes['inkscape:window-width']

    def set_inkscape_window_height(self, value):
	self._attributes['inkscape:window-height'] = value

    def get_inkscape_window_height(self):
	return self._attributes['inkscape:window-height']

    def set_showgrid(self, value):
	self._attributes['showgrid'] = value

    def get_showgrid(self):
	return self._attributes['showgrid']

    def set_inkscape_zoom(self, value):
	self._attributes['inkscape:zoom'] = value

    def get_inkscape_zoom(self):
	return self._attributes['inkscape:zoom']

    def set_inkscape_cx(self, value):
	self._attributes['inkscape:cx'] = value

    def get_inkscape_cx(self):
	return self._attributes['inkscape:cx']

    def set_inkscape_cy(self, value):
	self._attributes['inkscape:cy'] = value

    def get_inkscape_cy(self):
	return self._attributes['inkscape:cy']

    def set_inkscape_window_x(self, value):
	self._attributes['inkscape:window-x'] = value

    def get_inkscape_window_x(self):
	return self._attributes['inkscape:window-x']

    def set_inkscape_window_y(self, value):
	self._attributes['inkscape:window-y'] = value

    def get_inkscape_window_y(self):
	return self._attributes['inkscape:window-y']

    def set_inkscape_window_maximized(self, value):
	self._attributes['inkscape:window-maximized'] = value

    def get_inkscape_window_maximized(self):
	return self._attributes['inkscape:window-maximized']

    def set_inkscape_current_layer(self, value):
	self._attributes['inkscape:current-layer'] = value

    def get_inkscape_current_layer(self):
	return self._attributes['inkscape:current-layer']

class symbol(BaseElement, CoreAttrib, StyleAttrib, ExternalAttrib, PresentationAttributes_All, GraphicalEventsAttrib):
    """
    Class representing the symbol element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'symbol')
        self.setKWARGS(**kwargs)
    
    def set_viewBox(self, viewBox):
        self._attributes['viewBox'] = viewBox
    
    def get_viewBox(self):
        return self._attributes['viewBox']
    
    def set_preserveAspectRatio(self, preserveAspectRatio):
        self._attributes['preserveAspectRatio'] = preserveAspectRatio
    
    def get_preserveAspectRatio(self):
        return self._attributes['preserveAspectRatio']

class use(BaseElement, CoreAttrib, StyleAttrib, ConditionalAttrib, PointAttrib, DimensionAttrib, XLinkAttrib, PresentationAttributes_All, GraphicalEventsAttrib):
    """
    Class representing the use element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'use')
        self.setKWARGS(**kwargs)

    def set_transform(self, transform):
        self._attributes['transform'] = transform
    def get_transform(self):
        return self._attributes.get('transform')

class svg(BaseElement, CoreAttrib, StyleAttrib, ConditionalAttrib, PointAttrib, DimensionAttrib, XLinkAttrib, PresentationAttributes_All, GraphicalEventsAttrib, DocumentEventsAttrib):
    """
    Class representing the svg element of an svg doc.
    """
    def __init__(self, x=None, y=None, width=None, height=None, fileName=None, **kwargs):
        BaseElement.__init__(self, 'svg')
	self.set_xmlns_dc('http://purl.org/dc/elements/1.1/')
	self.set_xmlns_cc('http://creativecommons.org/ns#')
	self.set_xmlns_rdf('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
	self.set_xmlns_svg('http://www.w3.org/2000/svg')
        self.set_xmlns('http://www.w3.org/2000/svg')
	self.set_xmlns_sodipodi('http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
	self.set_xmlns_inkscape('http://www.inkscape.org/namespaces/inkscape')
        #self.set_xmlns_xlink('http://www.w3.org/1999/xlink')
        self.set_version('1.1')
        #self.set_x(x)
        #self.set_y(y)
        self.set_width(width)
        self.set_height(height)
	self.set_id('svg2')
	if fileName is None:
		self.set_sodipodi_docname('filename.svg')
	if not fileName is None:
		self.set_sodipodi_docname(fileName)		
	self.setKWARGS(**kwargs)

    def set_id(self, value):
	self._attributes['id'] = value

    def get_id(self):
	return self._attributes['id']

    def set_xmlns_svg(self, value):
	self._attributes['xmlns:svg'] = value

    def get_xmlns_svg(self):
	return self._attributes['xmlns:svg']

    def set_xmlns_rdf(self, value):
	self._attributes['xmlns:rdf'] = value

    def get_xmlns_rdf(self):
	return self._attributes['xmlns:rdf']

    def set_xmlns_cc(self, value):
	self._attributes['xmlns:cc'] = value

    def get_xmlns_cc(self):
	return self._attributes['xmlns:cc']

    def set_xmlns_dc(self, value):
	self._attributes['xmlns:dc'] = value

    def get_xmlns_dc(self):
	return self._attributes['xmlns:sodipodi']

    def set_xmlns_sodipodi(self, value):
	self._attributes['xmlns:sodipodi'] = value

    def get_xmlns_sodipodi(self):
	return self._attributes['xmlns:sodipodi']

    def set_xmlns_inkscape(self, value):
	self._attributes['xmlns:inkscape'] = value

    def get_xmlns_inkscape(self):
	return self._attributes['xmlns:inkscape']

    def set_sodipodi_docname(self, value):
	self._attributes['sodipodi:docname'] = value

    def get_sodipodi_docname(self):
	return self._attributes['sodipodi:docname']
        
    def set_version(self, version):
        self._attributes['version'] = version
    
    def get_version(self):
        return self._attributes['version']
    
    def set_xmlns(self, xmlns):
        self._attributes['xmlns'] = xmlns
    
    def get_xmlns(self):
        return self._attributes['xmlns']
    
    def set_xmlns_xlink(self, xmlns_xlink):
        self._attributes['xmlns:xlink'] = xmlns_xlink
    
    def get_xmlns_xlink(self):
        return self._attributes.get('xmlns:xlink')
        
    def set_viewBox(self, viewBox):
        self._attributes['viewBox'] = viewBox
    def get_viewBox(self):
        return self._attributes['viewBox']
    
    def set_preserveAspectRatio(self, preserveAspectRatio):
        self._attributes['preserveAspectRatio'] = preserveAspectRatio
    def get_preserveAspectRatio(self):
        return self._attributes['preserveAspectRatio']
    
    def set_transform(self, transform):
        self._attributes['transform'] = transform
    def get_transform(self):
        return self._attributes.get('transform') 
   
    def set_zoomAndPan(self, zoomAndPan):
        self._attributes['zoomAndPan'] = zoomAndPan
    def get_zoomAndPan(self):
        return self._attributes['zoomAndPan']
    
    def set_contentScriptType(self, contentScriptType):
        self._attributes['contentScriptType'] = contentScriptType
    def get_contentScriptType(self):
        return self._attributes['contentScriptType']
    
    def set_contentStyleType(self, contentStyleType):
        self._attributes['contentStyleType'] = contentStyleType
    def get_contentStyleType(self):
        return self._attributes['contentStyleType']  
    
    def set_baseProfile(self, baseProfile):
        self._attributes['baseProfile'] = baseProfile
    def get_baseProfile(self):
        return self._attributes['baseProfile']
#todo: check color.attrib and colorprofile.attrib. supposedly in image
class image(BaseElement, CoreAttrib, ConditionalAttrib, StyleAttrib, ViewportAttrib, PaintAttrib, OpacityAttrib, GraphicsAttrib, ClipAttrib, MaskAttrib, FilterAttrib, GraphicalEventsAttrib, CursorAttrib, XLinkAttrib, ExternalAttrib, PointAttrib, DimensionAttrib):
    """
    Class representing the image element of an svg doc.
    """
    def __init__(self, x=None, y=None, width=None, height=None, preserveAspectRatio=None,**kwargs):
        BaseElement.__init__(self, 'image')
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)
        self.set_width(width)
        self.set_preserveAspectRatio(preserveAspectRatio)
        self.setKWARGS(**kwargs)
    
    #def set_embedded(self,embedded):
    #    self._attributes['embedded']=embedded
        
    def set_preserveAspectRatio(self, preserveAspectRatio):
        self._attributes['preserveAspectRatio'] = preserveAspectRatio
    def get_preserveAspectRatio(self):
        return self._attributes['preserveAspectRatio']
    
    def set_transform(self, transform):
        self._attributes['transform'] = transform
    def get_transform(self):
        return self._attributes.get('transform') 

class switch(BaseElement, CoreAttrib, ConditionalAttrib, StyleAttrib, PresentationAttributes_All, GraphicalEventsAttrib, ExternalAttrib):
    """
    Class representing the switch element of an svg doc.
    """
    def __init__(self,**kwargs):
        BaseElement.__init__(self, 'switch')
        self.setKWARGS(**kwargs)
        
    def set_transform(self, transform):
        self._attributes['transform'] = transform
    def get_transform(self):
        return self._attributes.get('transform') 

class clipPath(BaseElement, CoreAttrib, ConditionalAttrib, StyleAttrib, ExternalAttrib, PresentationAttributes_All, GraphicalEventsAttrib):
    """
    Class representing the clipPath element of an svg doc.
    """
    def __init__(self, id=None, transform=None, clipPathUnits=None,**kwargs):
        BaseElement.__init__(self, 'clipPath')
        self.set_id(id)
        self.set_transform(transform)
        self.set_clipPathUnits(clipPathUnits)
        self.setKWARGS(**kwargs)
        
    
    def set_transform(self, transform):
        self._attributes['transform'] = transform
    def get_transform(self):
        return self._attributes.get('transform') 
    
    def set_clipPathUnits(self, clipPathUnits):
        self._attributes['clipPathUnits'] = clipPathUnits
        
    def get_clipPathUnits(self):
        return self._attributes['clipPathUnits']
