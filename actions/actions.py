from typing import Dict, Any, Text, List
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import operator
from rasa_sdk.types import DomainDict
from rasa_sdk import Tracker

class ActionNumbers(Action):

    def name(self) -> Text:
        return "action_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # extract entities from user input
        num1 = next(tracker.get_latest_entity_values("number1"), None)
        num2 = next(tracker.get_latest_entity_values("number2"), None)
        operator_ = next(tracker.get_latest_entity_values("operation"), None)

        # check if both numbers were provided
        if num1 is not None and num2 is not None:
            if operator_ == 'add' or operator_ == 'plus' or operator_ == 'sum':
                # perform addition
                result = float(num1) + float(num2)
                dispatcher.utter_message(template="utter_addition_result", result=result,num1 = num1 ,num2 = num2 )
            
            if operator_ == 'minus' or operator_ == 'subtract' or operator_ == 'difference':
                # perform addition
                result = float(num1) - float(num2)
                dispatcher.utter_message(template="utter_subtraction_result", result=result,num1 = num1 ,num2 = num2)
            
            if operator_ == 'product' or operator_ == 'multiply' or operator_ == 'times':
                # perform addition
                result = float(num1) * float(num2)
                dispatcher.utter_message(template="utter_multiplication_result", result=result,num1 = num1 ,num2 = num2)
            
            if operator_ == 'divide' or operator_ == 'division' or operator_ == 'divided by':
                # perform addition
                if num2 == 0:
                    dispatcher.utter_message(text="I'm sorry, you have entered an invalid input.")
                else:
                    result = float(num1) / float(num2)
                    dispatcher.utter_message(template="utter_division_result", result=result,num1 = num1 ,num2 = num2)
        else:
            dispatcher.utter_message(text="I'm sorry, I didn't understand the numbers you provided.")

        return []



class MathOperations(Action):
    def name(self) -> Text:
        return "action_math_operation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        operation = str(tracker.get_slot('operator'))
        operand1 = float(tracker.get_slot("operand1"))
        operand2 = float(tracker.get_slot("operand2"))
       

        if operation == "addition":
            result = operator.add(operand1, operand2)
        elif operation == "subtraction":
            result = operator.sub(operand1, operand2)
        elif operation == "multiplication":
            result = operator.mul(operand1, operand2)
        elif operation == "division":
            if operand2 == 0:
                dispatcher.utter_message(text="Sorry, cannot divide by zero.")
                return []
            result = operator.truediv(operand1, operand2)
        else:
            dispatcher.utter_message(text="Sorry, I didn't understand the operation you want to perform.")
            return []

        dispatcher.utter_message(template="utter_result", result=result, operation = operation, operand1 = operand1, operand2 = operand2)
        return []

