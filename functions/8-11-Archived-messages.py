def send_messages(pending_messages, sent_messages):
    """
    send each message until none are left
    """
    while pending_messages:
        current_design = pending_messages.pop()
        print(f"Sending message: {current_design}")
        sent_messages.append(current_design)

def sent_messagess(sent_messages):
    """Show all the models that were printed."""
    print("\nThese messages have been sent:")
    for completed_model in sent_messages:
        print(completed_model)

pending_messages = ['message1', 'message2', 'message3']
sent_messages = []

send_messages(pending_messages[:], sent_messages)
sent_messagess(sent_messages)
print('----------------------')
print(pending_messages)
print(sent_messages)