import tkinter as tk
import rosbag


# Topicを一覧し選択するGUIを表示するclass
class TopicSelector:
    def __init__(self, file_path):
        self.file_path = file_path
        self.selected_topic = None

        topics = self.get_topics()
        max_topic_length = max(len(topic) for topic in topics)

        self.root = tk.Tk()
        self.root.title("Select Topic")

        self.topics_listbox = tk.Listbox(self.root, width=max_topic_length, height=20)
        self.topics_listbox.pack()

        analyze_button = tk.Button(self.root, text="Select", command=self.on_analyze_button_clicked)
        analyze_button.pack()

        for topic in topics:
            self.topics_listbox.insert(tk.END, topic)


    def get_topics(self):
        with rosbag.Bag(self.file_path) as bag:
            topics = list(bag.get_type_and_topic_info()[1].keys())
        return topics
    

    def on_analyze_button_clicked(self):
        self.selected_topic = self.topics_listbox.get(self.topics_listbox.curselection())
        self.root.quit()


    def run(self):
        self.root.mainloop()
        return self.selected_topic


def get_topic_name(bag_file_path):
    selector = TopicSelector(bag_file_path)
    selected_topic = selector.run()
    print(f"Selected Topic: {selected_topic}")
    return selected_topic
