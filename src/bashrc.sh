if [ -z "$TEXTGEN_PYTHON_PATH" ]
then
    export TEXTGEN_PYTHON_PATH=$TEXTGEN_DIR/python/
    export PYTHONPATH=$TEXTGEN_PYTHON_PATH:$PYTHONPATH
fi


alias textgen-merryxmas-pt="python3 -m textgen.feliz_natal"
alias textgen-merryxmas-ko="python3 -m textgen.ko_xmas"
alias textgen-en-gen="python3 -m textgen.english.gen_english_phrase"
