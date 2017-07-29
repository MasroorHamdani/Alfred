def get_print_string_data():
    """
    Test data for print command to print a string operation
    :return:
    """
    return {
          "id": "9c0306cd-9de8-4d01-aa47-a896e5c3bed4",
          "timestamp": "2017-07-28T17:58:17.421Z",
          "lang": "en",
          "result": {
            "source": "agent",
            "resolvedQuery": "print reet",
            "action": "print_string",
            "actionIncomplete": False,
            "parameters": {
              "subject": "reet"
            },
            "contexts": [],
            "metadata": {
              "intentId": "132344c9-8f6a-4c78-8dc4-5ad39f8ab4f1",
              "webhookUsed": "false",
              "webhookForSlotFillingUsed": "false",
              "intentName": "print string"
            },
            "fulfillment": {
              "speech": "Printing string",
              "messages": [
                {
                  "type": 0,
                  "speech": "Printing string"
                }
              ]
            },
            "score": 1
          },
          "status": {
            "code": 200,
            "errorType": "success"
          },
          "sessionId": "09ee3a6b-895d-403d-9e04-69256f6f7b9f"
        }


def get_print_variable_data():
    """
    Test data for printing command to print variable given
    :return:
    """
    return {
          "id": "12ac40ff-e338-45ed-a53e-ddcbce77dc9f",
          "timestamp": "2017-07-28T18:12:36.933Z",
          "lang": "en",
          "result": {
            "source": "agent",
            "resolvedQuery": "print variable test",
            "action": "print_variable",
            "actionIncomplete": False,
            "parameters": {
              "variable": "test"
            },
            "contexts": [],
            "metadata": {
              "intentId": "8c38035d-b4e9-457a-a170-71556393cb3c",
              "webhookUsed": "false",
              "webhookForSlotFillingUsed": "false",
              "intentName": "print variable"
            },
            "fulfillment": {
              "speech": "Printing variable",
              "messages": [
                {
                  "type": 0,
                  "speech": "Printing variable"
                }
              ]
            },
            "score": 0.8655292893150024
          },
          "status": {
            "code": 200,
            "errorType": "success"
          },
          "sessionId": "09ee3a6b-895d-403d-9e04-69256f6f7b9f"
        }


def assign_var_to_var():
    """
    Test data for command to assign a variable to other variable
    :return:
    """
    return {
          "id": "659cb956-6e01-4fe4-93a3-d6d2dfa2adc2",
          "timestamp": "2017-07-28T19:04:32.838Z",
          "lang": "en",
          "result": {
            "source": "agent",
            "resolvedQuery": "assign variable a to b",
            "action": "assign_var_to_var",
            "actionIncomplete": False,
            "parameters": {
              "source_var": "a",
              "target_var": "b"
            },
            "contexts": [],
            "metadata": {
              "intentId": "83c72886-b40c-404d-a864-bb488eb54f51",
              "webhookUsed": "false",
              "webhookForSlotFillingUsed": "false",
              "intentName": "assign var to var"
            },
            "fulfillment": {
              "speech": "Assigning source var to target var",
              "messages": [
                {
                  "type": 0,
                  "speech": "Assigning source var to target var"
                }
              ]
            },
            "score": 1
          },
          "status": {
            "code": 200,
            "errorType": "success"
          },
          "sessionId": "09ee3a6b-895d-403d-9e04-69256f6f7b9f"
        }


def assign_val_to_var():
    """
    Test data for command to assign value to a variable
    :return:
    """
    return {
          "id": "9c9d7e65-2736-473c-8973-21ddde53a33b",
          "timestamp": "2017-07-28T19:11:16.57Z",
          "lang": "en",
          "result": {
            "source": "agent",
            "resolvedQuery": "assign 5 to a",
            "action": "assign_val_to_var",
            "actionIncomplete": False,
            "parameters": {
              "value": "5",
              "variable": "a"
            },
            "contexts": [],
            "metadata": {
              "intentId": "b6e5e196-7032-446c-b00d-648d47525157",
              "webhookUsed": "false",
              "webhookForSlotFillingUsed": "false",
              "intentName": "assign val to var"
            },
            "fulfillment": {
              "speech": "Assigning the value to variable.",
              "messages": [
                {
                  "type": 0,
                  "speech": "Assigning the value to variable."
                }
              ]
            },
            "score": 1
          },
          "status": {
            "code": 200,
            "errorType": "success"
          },
          "sessionId": "09ee3a6b-895d-403d-9e04-69256f6f7b9f"
        }


def if_cond_data():
    """
    Test data for command to generate if condition.
    :return:
    """
    return {
          "id": "ab92a67a-3231-4a05-8af2-a96e07f18481",
          "timestamp": "2017-07-28T19:30:29.716Z",
          "lang": "en",
          "result": {
            "source": "agent",
            "resolvedQuery": "if a is less than 2 then perform variable equal to 7",
            "action": "conditon_if",
            "actionIncomplete": False,
            "parameters": {
              "action": "variable equal to 7",
              "condition": "a is greater than to 2"
            },
            "contexts": [],
            "metadata": {
              "intentId": "d4898405-8136-4f59-b6b0-9258e910558c",
              "webhookUsed": "false",
              "webhookForSlotFillingUsed": "false",
              "intentName": "condition"
            },
            "fulfillment": {
              "speech": "checking condition",
              "messages": [
                {
                  "type": 0,
                  "speech": "checking condition"
                }
              ]
            },
            "score": 1
          },
          "status": {
            "code": 200,
            "errorType": "success"
          },
          "sessionId": "09ee3a6b-895d-403d-9e04-69256f6f7b9f"
        }


def loop_condition_data():
    """
    Test data for loop condition command
    :return:
    """
    return {
          "id": "71161330-3c3b-40df-9eb2-d52f31cafcbe",
          "timestamp": "2017-07-28T20:12:25.317Z",
          "lang": "en",
          "result": {
            "source": "agent",
            "resolvedQuery": "repeat this 3 times",
            "action": "loop",
            "actionIncomplete": False,
            "parameters": {
              "range": "3"
            },
            "contexts": [
              {
                "name": "loop-followup",
                "parameters": {
                  "range.original": "3",
                  "range": "3"
                },
                "lifespan": 2
              }
            ],
            "metadata": {
              "intentId": "27a2379c-c421-45f5-9fa0-d806059f53fc",
              "webhookUsed": "false",
              "webhookForSlotFillingUsed": "false",
              "intentName": "Loop"
            },
            "fulfillment": {
              "speech": "writing the loop for you",
              "messages": [
                {
                  "type": 0,
                  "speech": "writing the loop for you"
                }
              ]
            },
            "score": 1
          },
          "status": {
            "code": 200,
            "errorType": "success"
          },
          "sessionId": "09ee3a6b-895d-403d-9e04-69256f6f7b9f"
        }


def loop_execute_data():
    """
    Test data for command for operation to be done inside loop
    :return:
    """
    return {
          "id": "e298ad47-a2e0-4fa9-83f9-89531a60f7b2",
          "timestamp": "2017-07-28T20:13:56.414Z",
          "lang": "en",
          "result": {
            "source": "agent",
            "resolvedQuery": "print variable test",
            "action": "print_variable",
            "actionIncomplete": False,
            "parameters": {
              "string": "",
              "variable": "test"
            },
            "contexts": [],
            "metadata": {
              "intentId": "0aaf8047-4dd7-497c-8985-2a1e7b6a8e68",
              "webhookUsed": "false",
              "webhookForSlotFillingUsed": "false",
              "intentName": "Loop - custom"
            },
            "fulfillment": {
              "speech": "repeating this",
              "messages": [
                {
                  "type": 0,
                  "speech": "repeating this"
                }
              ]
            },
            "score": 0.7139699014193341
          },
          "status": {
            "code": 200,
            "errorType": "success"
          },
          "sessionId": "09ee3a6b-895d-403d-9e04-69256f6f7b9f"
        }


def loop_end_data():
    """
    Test data for loop ending command
    :return:
    """
    return{
          "id": "c375fbb2-3b3d-4bc0-9b40-314d95e4b476",
          "timestamp": "2017-07-28T21:52:47.976Z",
          "lang": "en",
          "result": {
            "source": "agent",
            "resolvedQuery": "end loop",
            "action": "end_loop",
            "actionIncomplete": False,
            "parameters": {},
            "contexts": [],
            "metadata": {
              "intentId": "1593664c-e2cc-49ba-9d9c-538d083f089c",
              "webhookUsed": "false",
              "webhookForSlotFillingUsed": "false",
              "intentName": "end for"
            },
            "fulfillment": {
              "speech": "Ending the loop",
              "messages": [
                {
                  "type": 0,
                  "speech": "Ending the loop"
                }
              ]
            },
            "score": 1
          },
          "status": {
            "code": 200,
            "errorType": "success"
          },
          "sessionId": "09ee3a6b-895d-403d-9e04-69256f6f7b9f"
        }