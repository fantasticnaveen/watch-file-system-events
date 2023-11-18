import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/rajen/Desktop/watch file system events/tracking file"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        name,extension = os.path.splitext(event.src_path)
        print("File '"+name+"' was created")
    def on_modified(self,event):
        name,extension = os.path.splitext(event.src_path)
        print("File '"+name+"' was modified")
    def on_moved(self,event):
        name,extension = os.path.splitext(event.src_path)
        print("File '"+name+"' was moved")
    def on_deleted(self,event):
        name,extension = os.path.splitext(event.src_path)
        print("File '"+name+"' was deleted")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()