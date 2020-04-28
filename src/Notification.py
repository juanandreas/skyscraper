import tkinter as tk
import webbrowser
from tkinter import ttk, Label

LARGE_FONT= ("Verdana", 12)

class Notification(object):

    def __init__(self):
        self.popup = tk.Tk()
        self.popup.wm_title("SKYSCRAPER NOTIFICATION")

    def callback(self, url):
        browser= webbrowser.get('chrome')
        browser.open_new(url)
        self.popup.destroy

    def window_notify(self, message_obj):
        '''
        message_obj = {
            "news_id": <news_source>,
            "news_url": <news_url>
        }
        '''
        news_id_label = ttk.Label(self.popup, text=message_obj["news_id"], font=LARGE_FONT)
        news_id_label.pack(side="top", fill="x", pady=100, padx=100)
        news_url_label = ttk.Label(self.popup, text=message_obj["news_url"], font=LARGE_FONT)
        news_url_label.pack(side="top", fill="x", pady=10, padx=100)
        url_button = ttk.Button(self.popup, text="Visit {0}".format(message_obj["news_id"]), command= lambda: self.callback(message_obj["news_url"]))
        url_button.pack()
        ok_button = ttk.Button(self.popup, text="Okay", command = self.popup.destroy)
        ok_button.pack()
        self.popup.call('wm', 'attributes', '.', '-topmost', '1')
        self.popup.mainloop()

n1 = Notification()
msg = {
    "news_id": "yt1",
    "news_url": "https://youtube.com"
}
n1.window_notify(msg)

n2 = Notification()
msg = {
    "news_id": "yt2",
    "news_url": "https://youtube.com"
}
n2.window_notify(msg)

n3 = Notification()
msg = {
    "news_id": "yt3",
    "news_url": "https://youtube.com"
}
n3.window_notify(msg)
