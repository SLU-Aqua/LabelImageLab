# import copy
# import os
from pathlib import Path
import sys
import yaml


class BspWriter:
    def __init__(
        self,
        filename,
        img_size,
    ):
        self.box_list = []
        self.annotation = {
            "image": filename,
            "state": {"verified": False, "warnings": 0},
            "size": {
                "depth": img_size[2],
                "height": img_size[0],
                "width": img_size[1],
            },
        }

    def set_validated(self, validated: bool):
        self.annotation["state"]["verified"] = validated

    def set_warnings(self, warnings: int):
        self.annotation["state"]["warnings"] = warnings

    def add_bnd_box(self, x_min, y_min, x_max, y_max, name):
        bnd_box = {"xmin": x_min, "ymin": y_min, "xmax": x_max, "ymax": y_max}
        bnd_box["name"] = name
        self.box_list.append(bnd_box)

    def save(self, file_path: Path):

        if file_path.exists():
            try:
                verified = self.annotation["state"]["verified"]
                warnings = self.annotation["state"]["warnings"]
                file = open(file_path, "r")
                self.annotation = yaml.load(file, Loader=yaml.FullLoader)

                self.set_validated(verified)
                self.set_warnings(warnings)

            except OSError as e:
                sys.exit(f"OSError: {e}")
            except yaml.YAMLError as e:
                sys.exit(f"YAMLError: {e}")

        self.annotation["objects"] = []

        # Set object.
        for i, each_object in enumerate(self.box_list):
            self.annotation["objects"].append(
                {
                    "name": each_object["name"],
                    "bndbox": {
                        "xmax": each_object["xmax"] - 1,
                        "xmin": each_object["xmin"] - 1,
                        "ymax": each_object["ymax"] - 1,
                        "ymin": each_object["ymin"] - 1,
                    },
                }
            )

        if len(self.annotation["objects"]) == 0:
            self.annotation.pop("objects")

        try:
            file = open(file_path, "w")
            yaml.dump(self.annotation, file, allow_unicode=True)
        except OSError as e:
            sys.exit(f"OSError: {e}")
        except yaml.YAMLError as e:
            sys.exit(f"YAMLError: {e}")


class BspReader:
    def __init__(self, file_path):
        self.shapes = []
        self.file_path = file_path
        try:
            file = open(file_path, "r")
            self.annotation = yaml.load(file, Loader=yaml.FullLoader)

            if "verified" not in self.annotation["state"]:
                self.annotation["state"]["verified"] = False
            if "warnings" not in self.annotation["state"]:
                self.annotation["state"]["warnings"] = False

            if "objects" in self.annotation:
                objects = self.annotation["objects"]
                for obj in objects:
                    name = str(obj["name"])
                    x_max = obj["bndbox"]["xmax"] + 1
                    x_min = obj["bndbox"]["xmin"] + 1
                    y_max = obj["bndbox"]["ymax"] + 1
                    y_min = obj["bndbox"]["ymin"] + 1
                    points = [
                        (x_min, y_min),
                        (x_max, y_min),
                        (x_max, y_max),
                        (x_min, y_max),
                    ]
                    self.shapes.append((name, points, None, None))

        except OSError as e:
            sys.exit(f"OSError: {e}")
        except yaml.YAMLError as e:
            sys.exit(f"YAMLError: {e}")
        except KeyError as e:
            sys.exit(f"KeyError: {e}, parsing dict {str(self.file_path)}")

    def validated(self):
        try:
            verified = self.annotation["state"]["verified"]
        except KeyError as e:
            sys.exit(f"KeyError: {e}, parsing dict {str(self.file_path)}")
        return verified

    def warnings(self):
        try:
            warnings = self.annotation["state"]["warnings"]
        except KeyError as e:
            sys.exit(f"KeyError: {e}, parsing dict {str(self.file_path)}")
        return warnings

    def get_shapes(self):
        return self.shapes
