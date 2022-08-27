# -*- coding: utf-8 -*-
from simplegrammar.grammar import SimpleGrammar

def gen_english_phrase():
    english_phrase = SimpleGrammar()\
        .set_text("#main_structure#")\
        .add_tag("main_structure", [
            "#unreal_conditionals#",
            "#used_to_phrases#"
        ])\
        .add_tag("unreal_conditionals", [
            "If there was a fire in this hotel, it would be very difficult to escape.",
            "I wouldn't have a car if I didn't live in the suburbs.",
            "If it wasn't raining so hard, we could get to #seemingly_unreachable_place#.",
            "If I were you, I'd make #random_person_name# wear a helmet when he's riding a bike"
            ])\
        .add_tag("used_to_phrases", [
            "#my_animals# are not used to #thing_that_scare_animals#, they always get scared"
            ])\
        .add_tag("seemingly_unreachable_place", [
            "the end of this road",
            "the top of the mountain",
            ])\
        .add_tag("thing_that_scare_animals", [
            "listening to the ships",
            "listening to church bell ringing",
            ])\
        .add_tag("random_person_name", [
            "Jimmy",
            "Samantha"
            ])\
        .add_tag("my_animals", [
            "my cats",
            "my fishes",
            "my dogs"
            ])

        # My cats are not used to listening to the ships, they always get scared

    print(str(english_phrase))


if __name__ == '__main__':

    import sys

    number_phrases = 1
    if len(sys.argv) > 1:
        number_phrases = int(sys.argv[1])


    for _ in range(0, number_phrases):
        gen_english_phrase()
