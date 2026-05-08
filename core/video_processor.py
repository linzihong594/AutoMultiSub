# core/video_processor.py
import subprocess
import os

# 导入我们刚刚写好的格式生成器
from .subtitle_style import get_style_string

# 写死 FFmpeg 的绝对路径（请确保这个路径在你的电脑上是正确的）
FFMPEG_PATH = r"D:\ffmpeg\bin\ffmpeg.exe"

def create_video_with_sub(original_video_path, srt_path, output_video_path):
    """
    使用 FFmpeg 将字幕烧录进视频画面中（硬字幕），应用外部自定义的格式。
    """
    print(f"     🎬 正在渲染带样式的硬字幕视频 (需要重新编码，请耐心等待): {os.path.basename(output_video_path)} ...")
    
    # 1. 路径安全处理
    # 将 Windows 路径转换为 FFmpeg 滤镜能看懂的安全格式（处理斜杠和盘符冒号）
    abs_srt_path = os.path.abspath(srt_path).replace('\\', '/')
    safe_srt_path = abs_srt_path.replace(':', '\\:')
    
    # 2. 获取字幕样式
    # 【注意这里】直接获取我们写死的绝对像素样式即可，不需要传高度了
    style_params = get_style_string()

    # 3. 构建 FFmpeg 命令
    command = [
        FFMPEG_PATH, '-y',
        '-i', original_video_path,
        
        # 核心指令：调用 subtitles 滤镜并应用拼装好的 force_style 参数
        '-vf', f"subtitles='{safe_srt_path}':force_style='{style_params}'", 
        
        # 视频重新编码：使用兼容性最好的 libx264
        '-c:v', 'libx264',
        
        # 保证画质不过度压缩（crf 18 属于视觉无损的高质量）
        '-crf', '18',
        
        # 音频无损复制（不重新编码音频，节省时间）
        '-c:a', 'copy',
        
        output_video_path
    ]
    
    try:
        # 执行命令，隐藏本来刷屏的 FFmpeg 日志，只在报错时显示信息
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError as e:
        print(f"     ❌ 视频合成失败: {e}")
        return False