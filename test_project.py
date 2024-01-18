import project

def test_function_level_1_r():
    assert project.function_level_1("n", "vinegar", "ãdresas") == "Right!"
    assert project.function_level_1("y", "bandage", "bandage") == "Right!"

def test_function_level_1_nr():
    assert project.function_level_1("y", "vinegar", "ãdresas") == "Not right!"
    assert project.function_level_1("n", "bandage", "bandage") == "Not right!"

def test_function_level_2_r():
    assert project.function_level_2("aguõna", "aguõna") == "Right!"


def test_function_level_2_nr():
    assert project.function_level_2("gooseberry", "ãdresas") == "Not right!"
    assert project.function_level_2("n", "ãdresas") == "Not right!"
    assert project.function_level_2("1", "ãdresas") == "Not right!"
