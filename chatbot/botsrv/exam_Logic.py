from chatterbot.logic import LogicAdapter

class MyLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(MyLogicAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement):
        import random

        # Randomly select a confidence between 0 and 1
        confidence = random.uniform(0, 1)
        print('statement:' , statement)
        # For this example, we will just return the input as output
        selected_statement = statement
        selected_statement.confidence = confidence

        return selected_statement