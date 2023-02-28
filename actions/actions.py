from typing import Dict, Any, Text, List
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import operator
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
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


# class ValidateNameForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_calculation_forms"
    
#     operator_ = " "
#     num1 = 0
#     num2 = 0
    
#     def validate_operator(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `first_name` value."""
#         # If the name is super short, it might be wrong.
#         ValidateNameForm.operator_ = slot_value
#         return []
    
#     def validate_operand1(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `first_name` value."""
#         # If the name is super short, it might be wrong.
#         ValidateNameForm.num1 = float(slot_value)
#         return []
    
#     def validate_operand2(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `first_name` value."""
#         # If the name is super short, it might be wrong.
#         ValidateNameForm.num2 = float(slot_value)
#         return []
    
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # operation = tracker.get_slot("operator")
#         # operand1 = tracker.get_slot("operand_1")
#         # operand2 = tracker.get_slot("operand_2")
        
#          # operation = tracker.latest_message.get('entities', {}).get('operator', [])[0]['value']
#         # operand1 = tracker.latest_message.get('entities', {}).get('operand1', [])[1]['value']
#         # operand2 = tracker.latest_message.get('entities', {}).get('operand2', [])[2]['value']

#         dispatcher.utter_message(f"{ValidateNameForm.operator_, ValidateNameForm.num1, ValidateNameForm.num2}")

#         if ValidateNameForm.operator_ == "addition":
#             result = operator.add(ValidateNameForm.num1, ValidateNameForm.num2)
            
#         elif ValidateNameForm.operator_ == "subtraction":
#             result = operator.sub(ValidateNameForm.num1, ValidateNameForm.num2)
#         elif ValidateNameForm.operator_ == "multiplication":
#             result = operator.mul(ValidateNameForm.num1, ValidateNameForm.num2)
#         elif ValidateNameForm.operator_ == "division":
#             if ValidateNameForm.num2 == 0:
#                 dispatcher.utter_message(text="Sorry, cannot divide by zero.")
#                 return []
#             result = operator.truediv(ValidateNameForm.num1, ValidateNameForm.num2)
#         else:
#             dispatcher.utter_message(text="Sorry, I didn't understand the operation you want to perform.")
#             return []
#         #dispatcher.utter_message(f"result is {result}")

#         # dispatcher.utter_message(template="utter_slot_values", result=SlotSet("result", result))
#         return [SlotSet("result", result)]
    
    
# # my_instance = ValidateNameForm()
# # my_instance.validate_operator()
# # my_instance.validate_operand1()
# # my_instance.validate_operand2()
# # my_instance.run()
   




class MathOperations(Action):
    def name(self) -> Text:
        return "action_math_operation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    #def run(self, dispatcher, tracker, domain):
        operation = str(tracker.get_slot('operator'))
        #operation = tracker.latest_message.text
        operand1 = float(tracker.get_slot("operand1"))
        operand2 = float(tracker.get_slot("operand2"))
        #operation = next(tracker.get_latest_entity_values("operator"), None)
        
         # operation = tracker.latest_message.get('entities', {}).get('operator', [])[0]['value']
        # operand1 = tracker.latest_message.get('entities', {}).get('operand1', [])[1]['value']
        # operand2 = tracker.latest_message.get('entities', {}).get('operand2', [])[2]['value']

        #dispatcher.utter_message(f"{operation, operand1, operand2}")

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

"""_____________________________________________________________________________________________________________________________
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionMath(Action):

    def name(self) -> Text:
        return "action_math"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        num1 = next(tracker.get_latest_entity_values("number1"), None)
        num2 = next(tracker.get_latest_entity_values("number2"), None)
        operation = next(tracker.get_latest_entity_values("operation"), None)
        if operation == "add":
            result = num1 + num2
            message = f"The sum of {num1} and {num2} is {result}."
        elif operation == "subtract":
            result = num1 - num2
            message = f"The difference between {num1} and {num2} is {result}."
        elif operation == "multiply":
            result = num1 * num2
            message = f"The product of {num1} and {num2} is {result}."
        elif operation == "divide":
            if num2 == 0:
                message = "Cannot divide by zero."
            else:
                result = num1 / num2
                message = f"The quotient of {num1} and {num2} is {result}."
        else:
            message = "Sorry, I don't recognize that operation. Please try again."

        dispatcher.utter_message(text=message)

        return []
"""
