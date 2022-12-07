import cv2
def video2frames(video_path, output_dir = 'E:\Prog\SkullGirls\Resource\TrainData', vid = None, skipframe = 5):
    """
    输入：video_path(视频文件的路径)
    输出：output_dir(保存图片路径)
    """
    # VideoCapture视频读取类
    videoCapture = cv2.VideoCapture()
    videoCapture.open(video_path)
    # 帧率
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    # 总帧数
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("fps=", int(fps), "frames=", int(frames))

    for i in range(int(frames)):
        _, frame = videoCapture.read()
        if i % skipframe == 0:
            cv2.imwrite("{}\{}{}.jpg".format(output_dir, vid, i), frame)
            print("Extract frame {}.".format(i))
    return

if __name__ == "__main__":
    video2frames('Resource\Video\data1.mp4',vid = 'a')