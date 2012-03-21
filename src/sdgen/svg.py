# -*- coding: utf-8 -*-
import os
import sys
import cairosvg
from sdgen.fixes import *
from sdgen.views import *
from sdgen.configuration import *

def find_non_terminals(data):
    result = []
    if data["view"] == "NonTerminal":
        result.append(data)
    if "children" in data:
        for child in data["children"]:
            result.extend(find_non_terminals(child))
    return result

def as_svg(data, path=None, conf=None):
    '''
    Generate a svg image(s). This function can generate multiple images.
    @param data: input data
    @param path: path were to save files;
                             if the value is None no file is saved, overwriting is forbidden (raise exception)
    @param conf: configuration to substitute the default one
    @return: a list of tuples, each tuple contains two fields: a name and an image in svg format
    '''
    views_to_render = [data]
    views_to_render.extend(find_non_terminals(data))
    result = []
    for view in views_to_render:
        result.append((view["name"], create_diagram(view, Configuration(conf))))

    if path != None:
        for image in result:
            # replace spaces to underscores
            fstr = image[0].replace(" ", "_")

            file_name = os.path.join(path, fstr + ".svg")
            #if os.path.exists(file_name):
            #    raise Exception, "File already exists!"
            with open(file_name, 'w') as f:
                f.write(image[1].encode('utf-8'))

 	    #command = 'python CairoSVG-0.3.1//cairosvg.py file_name -f png -o ' + os.path.join(path, image[0] + ".png"
	    #os.system(command);
	    cairosvg.main(file_name, 'png', 300, os.path.join(path, fstr + ".png"))

    return result
