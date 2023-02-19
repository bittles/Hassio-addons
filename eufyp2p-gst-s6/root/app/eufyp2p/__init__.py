#!/usr/bin/env python3
from .websocket import EufySecurityWebSocket
import aiohttp
import asyncio
import json
import socket
import threading
import time
import sys
import subprocess
import os
from queue import Queue

HOST_NAME = '0.0.0.0'

RTSP_PORT_NUMBER = 8541

RECV_CHUNK_SIZE = 4096

video_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
audio_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
backchannel_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Default camera name in go2rtc
audioVideoStream = 'camera1'
# Take snapshot every interval in seconds
## set default to every 5 minutes
SSINTERVAL = 600

ffmpegbin = "/usr/bin/ffmpeg"

EVENT_CONFIGURATION: dict = {
    "livestream video data": {
        "name": "video_data",
        "value": "buffer",
        "type": "event",
    },
    "livestream audio data": {
        "name": "audio_data",
        "value": "buffer",
        "type": "event",
    },
}

START_P2P_LIVESTREAM_MESSAGE = {
    "messageId": "start_livesteam",
    "command": "device.start_livestream",
    "serialNumber": None,
}

STOP_P2P_LIVESTREAM_MESSAGE = {
    "messageId": "stop_livesteam",
    "command": "device.stop_livestream",
    "serialNumber": None,
}

STOP_TALKBACK = {
    "messageId": "stop_talkback",
    "command": "device.stop_talkback",
    "serialNumber": None,
}

SET_API_SCHEMA = {
    "messageId": "set_api_schema",
    "command": "set_api_schema",
    "schemaVersion": 13,
}

STOP_P2P_LIVESTREAM_MESSAGE = {
    "messageId": "stop_livesteam",
    "command": "device.stop_livestream",
    "serialNumber": None,
}

P2P_LIVESTREAMING_STATUS = "p2pLiveStreamingStatus"

START_LISTENING_MESSAGE = {"messageId": "start_listening", "command": "start_listening"}

DRIVER_CONNECT_MESSAGE = {"messageId": "driver_connect", "command": "driver.connect"}

run_event = threading.Event()
run_event.set()

class ClientAcceptThread(threading.Thread):
    def __init__(self,socket,run_event,name,ws,serialno):
        threading.Thread.__init__(self)
        self.socket = socket
        self.queues = []
        self.run_event = run_event
        self.name = name
        self.ws = ws
        self.serialno = serialno
        self.my_threads = []

    def update_threads(self):
        my_threads_before = len(self.my_threads)
        for thread in self.my_threads:
            if not thread.is_alive():
                self.queues.remove(thread.queue)
        self.my_threads = [t for t in self.my_threads if t.is_alive()]
        if self.ws and my_threads_before > 0 and len(self.my_threads) == 0:
            if self.name == "BackChannel":
                print("All clients died. Stopping Stream for ", self.name)
            else:
                print("All clients died. Stopping Stream for ", self.name)

                msg = STOP_P2P_LIVESTREAM_MESSAGE.copy()
                msg["serialNumber"] = self.serialno
                asyncio.run(self.ws.send_message(json.dumps(msg)))

    def run(self):
        while self.run_event.is_set():
            self.update_threads()
            sys.stdout.flush()
            try:
                client_sock, client_addr = self.socket.accept()
                print ("New connection added: ", client_addr, " for ", self.name)
                sys.stdout.flush()

                if self.name == "BackChannel":
                    client_sock.setblocking(True)
                    print("Starting BackChannel")
                    thread = ClientRecvThread(client_sock, run_event, self.name, self.ws, self.serialno)
                    thread.start()
                else:
                    client_sock.setblocking(False)
                    thread = ClientSendThread(client_sock, run_event, self.name, self.ws, self.serialno)
                    self.queues.append(thread.queue)
                    if self.ws:
                        msg = START_P2P_LIVESTREAM_MESSAGE.copy()
                        msg["serialNumber"] = self.serialno
                        asyncio.run(self.ws.send_message(json.dumps(msg)))
                    self.my_threads.append(thread)
                    thread.start()
            except socket.timeout:
                pass

class ClientSendThread(threading.Thread):
    def __init__(self,client_sock,run_event,name,ws,serialno):
        threading.Thread.__init__(self)
        self.client_sock = client_sock
        self.queue = Queue(100)
        self.run_event = run_event
        self.name = name
        self.ws = ws
        self.serialno = serialno

    def run(self):
        try:
            while self.run_event.is_set():
                if self.queue.empty():
                    # Send something to know if socket is dead
                    self.client_sock.sendall(bytearray(0))
                    time.sleep(0.1)
                self.client_sock.sendall(
                    bytearray(self.queue.get(True)["data"])
                )
        except socket.error as e:
            print("Connection lost", self.name, e)
            pass
        except socket.timeout:
            print("Timeout on socket for ", self.name)
            pass
        self.client_sock.close()

class ClientRecvThread(threading.Thread):
    def __init__(self,client_sock,run_event,name,ws,serialno):
        threading.Thread.__init__(self)
        self.client_sock = client_sock
        self.run_event = run_event
        self.name = name
        self.ws = ws
        self.serialno = serialno

    def run(self):
        try:
            while self.run_event.is_set():
                try:
                    data = self.client_sock.recv(RECV_CHUNK_SIZE)
                    print("got ", len(data))
                except BlockingIOError:
                    # Resource temporarily unavailable (errno EWOULDBLOCK)
                    pass
        except socket.error as e:
            print("Connection lost", self.name, e)
            pass
        except socket.timeout:
            print("Timeout on socket for ", self.name)
            pass
        self.client_sock.close()
        msg = []
        msg["serialNumber"] = self.serialno
        asyncio.run(self.ws.send_message(json.dumps(msg)))

class Connector:
    def __init__(
        self,
        run_event,
    ):
        video_sock.bind(("127.0.0.1", 63336))
        video_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        video_sock.settimeout(1) # timeout for listening
        video_sock.listen()
        audio_sock.bind(("127.0.0.1", 63337))
        audio_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        audio_sock.settimeout(1) # timeout for listening
        audio_sock.listen()
        backchannel_sock.bind(("127.0.0.1", 63338))
        backchannel_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        backchannel_sock.settimeout(1) # timeout for listening
        backchannel_sock.listen()
        self.ws = None
        self.run_event = run_event
        self.serialno = ""

    def setWs(self, ws : EufySecurityWebSocket):
        self.ws = ws

    async def on_open(self):
        print(f" on_open - executed")

    async def on_close(self):
        print(f" on_close - executed")

    async def on_error(self, message):
        print(f" on_error - executed - {message}")

    async def on_message(self, message):
        #print(f"- on_message {message}")
        payload = message.json()
        message_type: str = payload["type"]
        if message_type == "result":
            message_id = payload["messageId"]
            print(f"on_message - {payload}")
            if message_id == START_LISTENING_MESSAGE["messageId"]:
                message_result = payload[message_type]
                states = message_result["state"]
                for state in states["devices"]:
                    self.serialno = state["serialNumber"]
                self.video_thread = ClientAcceptThread(video_sock, run_event, "Video", self.ws, self.serialno)
                self.audio_thread = ClientAcceptThread(audio_sock, run_event, "Audio", self.ws, self.serialno)
                self.backchannel_thread = ClientAcceptThread(backchannel_sock, run_event, "BackChannel", self.ws, self.serialno)
                self.audio_thread.start()
                self.video_thread.start()
                self.backchannel_thread.start()

        if message_type == "event":
            message = payload[message_type]
            event_type = message["event"]
            if message["event"] == "livestream audio data":
                event_value = message[EVENT_CONFIGURATION[event_type]["value"]]
                event_data_type = EVENT_CONFIGURATION[event_type]["type"]
                if event_data_type == "event":
                    for queue in self.audio_thread.queues:
                        if queue.full():
                            # print("Video queue full.")
                            queue.get(False)
                        queue.put(event_value)
            if message["event"] == "livestream video data":
                event_value = message[EVENT_CONFIGURATION[event_type]["value"]]
                event_data_type = EVENT_CONFIGURATION[event_type]["type"]
                if event_data_type == "event":
                    for queue in self.video_thread.queues:
                        if queue.full():
                            # print("Video queue full.")
                            queue.get(False)
                        queue.put(event_value)
            if message["event"] == "livestream error":
                print("Livestream Error!")
                if self.ws and len(self.video_thread.queues) > 0:
                    msg = START_P2P_LIVESTREAM_MESSAGE.copy()
                    msg["serialNumber"] = self.serialno
                    asyncio.run(self.ws.send_message(json.dumps(msg)))

def buildFfmpegCommand(cam_name):
    ffmpegcommand = [
        ffmpegbin,
        "-y",
#        "-analyzeduration", "1200000",
        "-rtsp_transport", "tcp",
        "-f", "h264", 
        "-i", "rtsp://127.0.0.1:" + str(RTSP_PORT_NUMBER) + "/" + cam_name,
        "-hls_init_time", "0",
#        "-hls_time", "2",
#        "-hls_segment_type", "mpegts",
#        "-fflags", "genpts+nobuffer+flush_packets",
        "-frames:v", "1",
        "/config/www/eufyp2p/" + cam_name + ".jpg"
        ]
    return ffmpegcommand

def buildGstCmd(cam_name):
    gstcommand = [
        "gst-launch-1.0",
        "-v",
#        "rtspsrc",
#        "protocols=tcp",
#        "location=rtsp://127.0.0.1:" + str(RTSP_PORT_NUMBER) + "/" + cam_name + "?mp4",
#        "latency=0",
        "souphttpsrc",
        "location=http://192.168.21.40:1997/api/frame.mp4?src=" + cam_name,
        "!",
        "decodebin",
        "!",
        "jpegenc",
        "snapshot=true",
        "!",
        "filesink",
        "location=/config/www/eufyp2p/" + cam_name + ".jpg"
        ]
    return gstcommand

# build as non-async function and call in main
# maybe... build as async with subprocess.returncode used with await, build loop outside of function call
#async def snapshotCmd(cam_name, snapshot_interval):
#    ffmpegcmd = buildFfmpegCommand(cam_name)
#    print(ffmpegcmd)
#    await asyncio.sleep(60)
#    while True:
#        print("Snapshot starting")
#        subprocess.Popen(ffmpegcmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#        print("Snapshot created")
#        await asyncio.sleep(snapshot_interval)
        #else:
            #print("Error during snapshot, retrying in 10 seconds")
            #await asyncio.sleep(10)


async def main(run_event):

    SSINTERVAL = 600 # set as default, get envs not working returned none
    audioVideoStream = 'camera1' # set default, placeholder till sed for go2rtc made
    videoStream = 'camera1_video'
    audioStream = 'camera1_audio'
    c = Connector(run_event)

    ws: EufySecurityWebSocket = EufySecurityWebSocket(
        "127.0.0.1",
        3000,
        aiohttp.ClientSession(),
        c.on_open,
        c.on_message,
        c.on_close,
        c.on_error,
    )
    c.setWs(ws)
    await ws.connect()

    await ws.send_message(json.dumps(START_LISTENING_MESSAGE))
    await ws.send_message(json.dumps(SET_API_SCHEMA))
    await ws.send_message(json.dumps(DRIVER_CONNECT_MESSAGE))

    print("Main stream name is: ")
    print(audioVideoStream)
    print("Video only stream name is: ")
    print(videoStream)
    print("Snapshot interval is: ")
    print(SSINTERVAL)
    snapcmd = buildGstCmd(videoStream)
    print("Snapshot command is:")
    print(" ".join(snapcmd))
    await asyncio.sleep(20)
    while True: #need use ifs with returncode
        print("Snapshot snapping")
        subprocess.Popen(snapcmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        await asyncio.sleep(SSINTERVAL)
    await asyncio.sleep(1000000000000000000000005)

try:
    asyncio.run(main(run_event))

except (KeyboardInterrupt, SystemExit):
    run_event.clear()
