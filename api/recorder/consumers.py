from datetime import datetime
import json 
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer

class wsconsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("Websocket connected")

        # Prepare file to write binary audio
        self.audio_filename = "recorded_audio.webm"
        self.audio_file = open(self.audio_filename, "ab")

    def disconnect(self, close_code):
        print("WebSocket disconnected")
        if hasattr(self, 'audio_file') and not self.audio_file.closed:
            self.audio_file.close()
    
    def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            print(f"Received {len(bytes_data)} bytes")
            self.audio_file.write(bytes_data)  # Write audio chunk
        elif text_data:
            print(f"Text received: {text_data}")
                

