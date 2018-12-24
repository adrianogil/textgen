# -*- coding: utf-8 -*-
from simplegrammar.grammar import SimpleGrammar

merry_xmas = SimpleGrammar() \
.set_text("#main_structure#")\
    .add_tag("main_structure", [
        "#congrats#\n\n#votes#\n\n#ending#"
    ])\
    .add_tag("congrats", [
        "Feliz Natal!", "Feliz festividades!", "Boas festas!",
    ])\
    .add_tag("votes", [
        "#feeling_based_votes#",
        "#spiritual_based_votes#"
    ])\
    .add_tag("feeling_based_votes", [
        "#health_votes# e #happy_feelings#!",
    ])\
    .add_tag("spiritual_based_votes", [
        "Benções infinitas para você e sua família!"
    ])\
    .add_tag("health_votes", [
        "Muita saúde", 
    ])\
    .add_tag("happy_feelings", [
        "felicidade",
        "contentamento",
        "boas energias",
        "intensa alegria"
        ])\
    .add_tag("ending", [
        "Abraços!",
        "Felicidades!",
        "Muita Paz!"
    ])

print(str(merry_xmas))
