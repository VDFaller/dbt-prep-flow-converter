from dbt_prep_flow_converter.foo import foo


def test_foo():
    assert foo("foo") == "foo"
