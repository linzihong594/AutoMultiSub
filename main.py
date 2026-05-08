import os
from core.config import LANGUAGE_MAP, INPUT_DIR
from core.folder_manager import get_output_srt_path, copy_original_file
from core.translator import translate_srt_file
from core.video_processor import create_video_with_sub  # 【新增】导入视频处理模块

def run_pipeline(project_name, episode_name):
    # 假设你在 raw-data 里放了同名的 .mp4 和 .srt
    input_srt_name = f"{episode_name}.srt"
    input_video_name = f"{episode_name}.mp4" # 【新增】寻找无字幕原视频
    
    input_srt_path = os.path.join(INPUT_DIR, input_srt_name)
    input_video_path = os.path.join(INPUT_DIR, input_video_name)
    
    print(f"\n🚀 开始全自动处理项目: 《{project_name}》 | 集数: {episode_name}")
    
    # 检查源文件是否存在
    if not os.path.exists(input_srt_path):
        print(f"❌ 找不到字幕原件: {input_srt_path}")
        return
    if not os.path.exists(input_video_path):
        print(f"❌ 找不到视频原件: {input_video_path}")
        return

    # 遍历所有配置好的目标语言
    for lang_code, lang_cn_name in LANGUAGE_MAP.items():
        print(f"\n  ├─ 正在生成 [{lang_cn_name}] 版本...")
        
        # 1. 获取该语言保存的路径
        output_srt_path = get_output_srt_path(project_name, episode_name, lang_cn_name)
        
        # 2. 生成对应语言的视频路径 (把 .srt 后缀换成 .mp4)
        output_video_path = output_srt_path.replace('.srt', '.mp4')
        
        # 3. 处理字幕
        if lang_code == 'en':
            copy_original_file(input_srt_path, output_srt_path)
            print("     ✅ 英语字幕已复制")
        else:
            if translate_srt_file(input_srt_path, output_srt_path, lang_code):
                 print("     ✅ 字幕翻译完成")
                 
        # 4. 【关键新增】调用 FFmpeg 把字幕塞进视频里！
        if create_video_with_sub(input_video_path, output_srt_path, output_video_path):
             print(f"     🎉 视频已生成 -> {output_video_path}")

    print("\n🏆 所有语言版本的视频+字幕全部分类归档完成！\n")

if __name__ == "__main__":
    # 项目配置信息
    PROJECT_NAME = "Bride for Rent, Queen for Real"
    
    # 这里只需要填集数名！
    # 确保你的 raw-data 文件夹里同时有 "EP01.srt" 和 "EP01.mp4"
    TARGET_EPISODE = "EP01" 
    
    run_pipeline(PROJECT_NAME, TARGET_EPISODE)