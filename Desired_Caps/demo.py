import yaml

from Common.contants import caps_dir
import os
# fs = open(os.path.join(caps_dir,"demo.yaml"))
# res = yaml.load(fs)
fs = open(os.path.join(caps_dir, "desired_caps.yaml"),encoding='UTF-8')
desired_caps = yaml.load(fs)
print(desired_caps)
