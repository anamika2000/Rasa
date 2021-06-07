# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet,EventType
from rasa_sdk.executor import CollectingDispatcher



class ContactForm(Action):

    def name(self) -> Text:
         return "user_details_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:
        required_slot = ["name","number","email"]

        for slot_name in required_slot:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("required_slot",slot_name)]

        return [SlotSet("required_slot",None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"
    def run(
        self,
        dispatcher,
        tracker : Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
    


        dispatcher.utter_message(template="utter_details_thanks",Name=tracker.get_slot('name'),Mobile_number=tracker.get_slot('number'),Email=tracker.get_slot('email'))
        return []
    

    
        
