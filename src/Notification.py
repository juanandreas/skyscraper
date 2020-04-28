import datetime
import time
import tkinter as tk
import webbrowser
from tkinter import ttk, Label

from pygame import mixer

LARGE_FONT= ("Verdana", 12)

class Notification(object):

    def __init__(self):
        # self.popup = tk.Tk()
        # self.popup.wm_title("SKYSCRAPER NOTIFICATION")
        pass

    def open_site(self, url):
        browser= webbrowser.get('chrome')
        browser.open_new(url)

    # def window_notify(self, message_obj):
    #     '''
    #     message_obj = {
    #         "news_id": <news_source>,
    #         "news_url": <news_url>
    #     }
    #     '''
    #     news_id_label = ttk.Label(self.popup, text=message_obj["news_id"], font=LARGE_FONT)
    #     news_id_label.pack(side="top", fill="x", pady=100, padx=100)
    #     news_url_label = ttk.Label(self.popup, text=message_obj["news_url"], font=LARGE_FONT)
    #     news_url_label.pack(side="top", fill="x", pady=10, padx=100)
    #     url_button = ttk.Button(self.popup, text="Visit {0}".format(message_obj["news_id"]), command= lambda: self.open_site(message_obj["news_url"]))
    #     url_button.pack()
    #     ok_button = ttk.Button(self.popup, text="Okay", command = self.popup.destroy)
    #     ok_button.pack()
    #     self.popup.call('wm', 'attributes', '.', '-topmost', '1')
    #     self.popup.mainloop()

    def play_sound(self):
        mixer.init()
        mixer.music.load('src/when.mp3')
        mixer.music.play()
        time.sleep(0.4)


    def stream_notification(self, message_obj):
        print("{0} News update detected: {1}".format(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:"),
            message_obj["news_url"]))
        self.play_sound()

n1 = Notification()
msg = {
    "news_id": "yt1",
    "news_url": "https://youtube.com"
}
n1.stream_notification(msg)

