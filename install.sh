rm -rf build
rm -rf dist
#python setup.py sdist bdist_wheel
python setup.py sdist
pip install dist/stockpy-0.0.1.tar.gz