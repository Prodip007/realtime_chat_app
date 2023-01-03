"""Receive messages over from RabbitMQ and send them over the websocket."""

import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.exchange_declare(
    exchange='fe662fd9de834fc', exchange_type='fanout'
)

# exclusive means the queue should be deleted once the connection is closed 
result = channel.queue_declare(queue="", exclusive=True)
# result = channel.queue_declare(queue="")
queue_name = ''  # random queue name generated by RabbitMQ 
# print('queue_name:', queue_name)
channel.queue_bind(exchange='fe662fd9de834fc', queue=queue_name)

# print('listening for messages...')
# x = channel.consume(queue_name)
# print('channel.consume:', [x])

# for item, item2 in channel.consume(queue_name):
#     print(item)

# while True:
#     print('inside while')
#     for method_frame, _, body in channel.consume(queue_name):
#         print('inside for loop')
#         try:
#             print(body)
#         except OSError as error:
#             print(error)
#         else:
#             channel.basic_ack(method_frame.delivery_tag)



for method_frame, properties, body in channel.consume(queue_name):

    # Display the message parts
    print(method_frame)
    print(properties)
    print(body)

    # Acknowledge the message
    channel.basic_ack(method_frame.delivery_tag)

    # Escape out of the loop after 10 messages
    if method_frame.delivery_tag == 10:
        break

# Cancel the consumer and return any pending messages
requeued_messages = channel.cancel()
print('Requeued %i messages' % requeued_messages)

# Close the channel and the connection
channel.close()
connection.close()