from json import dump

import pika

from notifications.channels import BaseNotificationChannel


class BroadCastWebSocketChannel(BaseNotificationChannel):
    """Fanout notification channel with RabbitMQ."""

    def _connect(self):
        """Connect to the RabbitMQ server."""

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )

        channel = connection.channel()

        return connection, channel