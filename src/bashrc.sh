if [ -z "$TEXTGEN_PYTHON_PATH" ]
then
    export TEXTGEN_PYTHON_PATH=$TEXTGEN_DIR/python/
    export PYTHONPATH=$TEXTGEN_PYTHON_PATH:$PYTHONPATH
fi


alias textgen-merryxmas-pt="python2 -m textgen.feliz_natal"