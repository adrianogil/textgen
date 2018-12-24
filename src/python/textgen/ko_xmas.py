# -*- coding: utf-8 -*-
from simplegrammar.grammar import SimpleGrammar

merry_xmas = SimpleGrammar() \
.set_text("#main_structure#")\
    .add_tag("main_structure", [
        "메리크리스마스 "
    ])

print(str(merry_xmas))
