#!/bin/sh

python3 -m build
pip3 install dist/m360-0.0.1-*.whl --force-reinstall
