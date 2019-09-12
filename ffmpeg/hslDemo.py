import re
import uuid
import subprocess
import requests

QUALITY = 'ld'


# 地址
def get_vedio_ids_from_url(url):
    html = requests.get(url).text
    video_ids = re.findall(r'data-lens-id="(\d+)"', html)
    video_ids = re.findall(r'data-lens-id="(\d+)"', html)  # print(video_ids)
    if video_ids:
        return set([int(video_id) for video_id in video_ids])
    return []


def yield_video_m3u8_url_from_video_ids(video_ids):
    for video_id in video_ids:
        api_video_url = 'https://lens.zhihu.com/api/videos/{}'.format(int(video_id))  # 下载的是知乎视频
        # print(api_video_url)
        r = requests.get(api_video_url)
        playlist = r.json()['playlist']
        print(playlist)
        m3u8_url = playlist[QUALITY]['play_url']
        yield m3u8_url


def download(url):
    video_ids = get_vedio_ids_from_url(url)
    m3u8_list = list(yield_video_m3u8_url_from_video_ids(video_ids))
    filename = '{}.mp4'.format(uuid.uuid4())
    path = "E:\\a.mp4"
    for idx, m3u8_url in enumerate(m3u8_list):
        # here \" and \" is important！
        cmd_str = 'ffmpeg -i \"' + 'http://10.141.6.187:6713/mag/hls/7b0b464bc27f4bb1b227cc6ea213b46f/0/live.m3u8' + '\" ' + '-acodec copy -vcodec copy -absf aac_adtstoasc ' + path + filename.format(
            str(idx))
        print(cmd_str)
        subprocess.call(cmd_str, shell=True)


if __name__ == '__main__':  # 贴上你需要下载的 回答或者文章的链接
    url = "http://10.141.6.187:6713/mag/hls/7b0b464bc27f4bb1b227cc6ea213b46f/0/live.m3u8"
    download(url)
