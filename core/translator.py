# core/translator.py
import pysrt
from googletrans import Translator

# 在模块级别初始化翻译器，避免在循环中反复创建拖慢速度
translator = Translator()

def translate_srt_file(input_srt_path, output_srt_path, target_lang_code):
    """
    将指定的英文字幕文件翻译为目标语言，并保存到指定路径。
    """
    try:
        # 打开原始英文字幕文件
        subs = pysrt.open(input_srt_path)
        
        # 遍历每一行字幕进行翻译
        for i, sub in enumerate(subs):
            try:
                # src='en' 指定原语言为英文，dest 传入目标语言代码
                result = translator.translate(sub.text, src='en', dest=target_lang_code)
                subs[i].text = result.text
            except Exception as e:
                print(f"⚠️ 第 {i} 行翻译出错，将保留原文: {e}")
        
        # 将翻译好的结果保存（使用 utf-8 编码防止小语种乱码）
        subs.save(output_srt_path, encoding='utf-8')
        return True
        
    except Exception as e:
        print(f"❌ 读取或处理字幕文件时发生严重错误: {e}")
        return False