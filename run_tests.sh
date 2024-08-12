SCRIPT_DIR=$(cd $(dirname "$0") && pwd)
export PYTHONPATH=$SCRIPT_DIR/scripts
python -m unittest discover -s $SCRIPT_DIR/tests -p "test_*.py"