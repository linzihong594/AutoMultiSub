# core/folder_manager.py
import os
import shutil
from .config import OUTPUT_DIR # 从同级的 config.py 中导入输出路径配置

def get_output_srt_path(project_name, episode_name, lang_cn_name):
    """
    根据剧名和语种，自动创建多级目录，并返回最终生成的字幕文件的完整路径。
    """
    # 1. 拼接主文件夹：results/《剧名》多国语言版字幕全集
    base_dir_name = f"《{project_name}》多国语言版字幕全集"
    base_dir_path = os.path.join(OUTPUT_DIR, base_dir_name)
    
    # 2. 拼接子文件夹：《剧名》XX语字幕版全集
    sub_dir_name = f"《{project_name}》{lang_cn_name}字幕版全集"
    sub_dir_path = os.path.join(base_dir_path, sub_dir_name)
    
    # 3. 自动创建文件夹树（如果已经存在则安全跳过）
    os.makedirs(sub_dir_path, exist_ok=True)
    
    # 4. 生成该集字幕文件的最终绝对路径
    output_srt_path = os.path.join(sub_dir_path, f"{episode_name}.srt")
    return output_srt_path

def copy_original_file(src_path, dest_path):
    """
    直接无损复制原文件（专门用于处理原生英文字幕）。
    """
    try:
        shutil.copy2(src_path, dest_path)
        return True
    except Exception as e:
        print(f"     ❌ 复制原始文件失败: {e}")
        return False