import os
import sys

temp = sys.argv[1].split(",")
file = temp[0] + "\\" + sys.argv[2]


os.system(
    "isort "
    + file
    + " --profile black && black "
    + file
    + " && flake8 "
    + file
    + " --max-line-length 88 --extend-ignore E203"
)
