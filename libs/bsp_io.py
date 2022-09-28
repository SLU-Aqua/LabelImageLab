import xml.etree.ElementTree as ET
from xml.dom import minidom
import os


XML_EXT = ".xml"


class BspWriter:
    def __init__(
        self,
        folder_name,
        filename,
        img_size,
        database_src="Unknown",
        local_img_path=None,
    ):
        self.folder_name = folder_name
        self.filename = filename
        self.database_src = database_src
        self.img_size = img_size
        self.box_list = []
        self.local_img_path = local_img_path
        self.verified = False

    def prettify(self, elem):
        # """
        # Return a pretty-printed XML string for the Element.
        # """

        """Return a pretty-printed XML string for the Element."""
        rough_string = ET.tostring(elem, encoding="unicode", method="xml")
        reparsed = minidom.parseString(rough_string)
        prettyxml = reparsed.toprettyxml(indent="  ")
        # TODO: Fix to remove empty lines introduced by xml.dom.minidom.toprettyxml. This is awful.
        prettyxml = os.linesep.join([s for s in prettyxml.splitlines() if s.strip()])
        return prettyxml

    def gen_xml(self):
        """
        Return XML root
        """
        # Check conditions
        if self.filename is None or self.img_size is None:
            return None

        # top = Element("annotation")
        root = ET.Element("annotation")

        if self.verified:
            root.set("verified", "yes")

        # filename
        filename = ET.Element("filename")
        filename.text = self.filename
        root.append(filename)

        # source
        source = ET.Element("source")
        root.append(source)
        filename = ET.SubElement(source, "filename")
        filename.text = "TBD"  # source_path.name
        path = ET.SubElement(source, "path")
        path.text = "TBD"  # str(source_path.parent)

        # size
        size = ET.Element("size")
        root.append(size)
        width = ET.SubElement(size, "width")
        width.text = str(str(self.img_size[1]))
        height = ET.SubElement(size, "height")
        height.text = str(str(self.img_size[0]))
        depth = ET.SubElement(size, "depth")
        if len(self.img_size) == 3:
            depth.text = str(self.img_size[2])
        else:
            depth.text = "1"

        return root

    # def add_bnd_box(self, x_min, y_min, x_max, y_max, name, difficult):
    def add_bnd_box(self, x_min, y_min, x_max, y_max, name):
        bnd_box = {"xmin": x_min, "ymin": y_min, "xmax": x_max, "ymax": y_max}
        bnd_box["name"] = name
        # bnd_box["difficult"] = difficult
        self.box_list.append(bnd_box)

    def append_objects(self, top):
        for i, each_object in enumerate(self.box_list):
            object_item = ET.SubElement(top, "object")
            object_item.set("id", str(i))
            name = ET.SubElement(object_item, "name")
            name.text = each_object["name"]

            bnd_box = ET.SubElement(object_item, "bndbox")
            x_min = ET.SubElement(bnd_box, "xmin")
            x_min.text = str(each_object["xmin"])
            y_min = ET.SubElement(bnd_box, "ymin")
            y_min.text = str(each_object["ymin"])
            x_max = ET.SubElement(bnd_box, "xmax")
            x_max.text = str(each_object["xmax"])
            y_max = ET.SubElement(bnd_box, "ymax")
            y_max.text = str(each_object["ymax"])

    def save(self, target_file=None):
        root = self.gen_xml()
        self.append_objects(root)

        xmlstr = self.prettify(root)

        if target_file is None:
            assert 0
            # out_file = codecs.open(self.filename + XML_EXT, "w", encoding=ENCODE_METHOD)
        else:
            # out_file = codecs.open(target_file, "w", encoding=ENCODE_METHOD)
            with open(target_file, "w") as f:
                f.write(xmlstr)


class BspReader:
    def __init__(self, file_path):
        # shapes type:
        # [labbel, [(x1,y1), (x2,y2), (x3,y3), (x4,y4)], color, color, difficult]
        self.shapes = []
        self.file_path = file_path
        self.verified = False
        try:
            self.parse_xml()
        except:
            pass

    def get_shapes(self):
        return self.shapes

    # def add_shape(self, label, bnd_box, difficult):
    def add_shape(self, label, bnd_box):
        x_min = int(float(bnd_box.find("xmin").text))
        y_min = int(float(bnd_box.find("ymin").text))
        x_max = int(float(bnd_box.find("xmax").text))
        y_max = int(float(bnd_box.find("ymax").text))
        points = [(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)]
        # self.shapes.append((label, points, None, None, difficult))
        self.shapes.append((label, points, None, None))

    def parse_xml(self):

        xml_tree = ET.parse(self.file_path).getroot()

        try:
            verified = xml_tree.attrib["verified"]
            if verified == "yes":
                self.verified = True
        except KeyError:
            self.verified = False

        for object_iter in xml_tree.findall("object"):
            bnd_box = object_iter.find("bndbox")
            label = object_iter.find("name").text
            # Add chris
            # difficult = False
            # if object_iter.find("difficult") is not None:
            #    difficult = bool(int(object_iter.find("difficult").text))
            # self.add_shape(label, bnd_box, difficult)
            self.add_shape(label, bnd_box)
        return True
