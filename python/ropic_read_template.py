from topic_selector import TopicSelector
import sys


# 処理記述
class example:
    def example():
        return 


# 実行引数からbagファイルのパスを取得
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python camera.py <path_to_rosbag_file>")
        sys.exit(1)

    bag_file_path = sys.argv[1]
    # topic_selector.pyのget_topic_name関数を呼び出す
    camera_topic_name = get_camera_topic_name(bag_file_path)