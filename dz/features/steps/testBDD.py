from behave import given, when, then
import bot
import math


@given('I send bot message {start}')
def step_impl(context, start: str):
    bot.cmd_start(start)


@when('I send bot first message {firstNum}')
def step_imp2(context, firstNum: str):
    context.firstNum = bot.first_num(firstNum)


@when('I send bot second message {secondNum}')
def step_imp3(context, secondNum: str):
    context.secondNum = bot.second_num(secondNum)


@then('I send bot operation ^ and get answer {result}')
def step_imp4(context, result: str):
    float(context.firstNum) ** float(context.secondNum) == float(result)

@then('I send bot operation <> and get answer {result}')
def step_imp4(context, result: str):
    math.sqrt(float(context.firstNum)*float(context.firstNum) +  float(context.secondNum)*float(context.secondNum)) == float(result)
