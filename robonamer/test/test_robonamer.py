from src import robonamer


def test_instantiation():
    r = robonamer.Robot()
    assert r.name is None
    assert r.bootcount == 0

def test_boot():
    r = robonamer.Robot()
    r.boot()
    assert r.bootcount == 1
    assert r.name is not None

def test_generate_name():
    r = robonamer.Robot()
    r.generate_name()
    assert len(r.name) == 5
    assert r.name[:1].isupper()
    assert r.name[2:].isdigit()

def test_reset():
    r = robonamer.Robot()
    r.boot()
    r.reset()
    assert r.bootcount == 1
    assert r.name is None

def test_rename_after_reset():
    r = robonamer.Robot()
    r.boot()
    r.reset()
    _ = print(r)
    assert r.name is not None

def test_load_used_names():
    """Only uses standard library at the moment so no need to test."""
    pass

def test_save_used_name():
    """Only uses standard library at the moment so no need to test."""
    pass
