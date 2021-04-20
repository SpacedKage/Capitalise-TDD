from capitalise_func import capitalise

def test_capitalise_one_word_lower():
    capitalised = capitalise("deborah")
    assert capitalised == "Deborah"

def test_capitalise_sentance_lower():
    capitalised = capitalise("the quick brown fox jumps over the lazy dog")
    assert capitalised == "The quick brown fox jumps over the lazy dog"

def _test_capitalised_empty_string():
    capitalised = capitalise("")
    assert capitalised == ""

def _test_capitalised_all_upper():
    capitalised = capitalise("HELLO WORLD")
    assert capitalised == "Hello world"