from behave import *
from roots import get_roots


@given('I put roots {roots} into the function')
def step_impl(context, roots: str):
    roots = list(map(float, roots[1:-1].split(',')))
    context.result = get_roots(*roots)


@then('I get roots {result}')
def step_impl(context, result: str):
    result = list(map(float, result[1:-1].split(',')))
    assert sorted(context.result) == sorted(result)
