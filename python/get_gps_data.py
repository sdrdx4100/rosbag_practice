from topic_selector import get_topic_name
import sys
import rosbag
import csv
from pyproj import CRS, Transformer


# 緯度、経度、高度の値を受け取り、UTM座標系に変換して返す
def convert_to_xyz(latitude, longitude, altitude):
    
    # WGS 84（世界測地系）からUTMゾーンへの変換
    utm_crs = CRS.from_epsg(32654) # UTMゾーン54N
    transformer = Transformer.from_crs(CRS.from_epsg(4326), utm_crs)

    # 緯度、経度からUTM座標への変換
    x, y = transformer.transform(latitude, longitude)
    x, y, altitude # x, yは東方向と北方向の座標、altitudeは高度
    x, y, z = latitude, longitude, altitude # この行を適切な変換に置き換える
    return x, y, z


# CSVファイルに書き出す
def export_to_csv(bag_file,gps_topic):
    with rosbag.Bag(bag_file, 'r') as bag:
        with open('gps_data.csv', mode='w') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Frame', 'X', 'Y', 'Z'])
            
            # すべてのGPS_msgを読み込み、緯度、経度、高度を取得する
            frame_number = 0
            for topic, msg, _ in bag.read_messages(gps_topic):
                latitude = msg.latitude
                longitude = msg.longitude
                altitude = msg.altitude
                
                x, y, z = convert_to_xyz(latitude, longitude, altitude)
                csv_writer.writerow([frame_number, x, y, z])
                print(f"Frame {frame_number}: x={x}, y={y}, z={z}")

                frame_number += 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_rtk_data.py <path_to_rosbag_file>")
        sys.exit(1)

    # 実行引数からbagファイルのパスを取得
    bag_file_path = sys.argv[1]
    
    # topic名を指定して取得するmoduleの呼び出し
    topic_name  = get_topic_name(bag_file_path)
    export_to_csv(bag_file_path,topic_name)