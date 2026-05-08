# core/translator.py
import pysrt
import time
from deep_translator import GoogleTranslator

def translate_srt_file(input_srt_path, output_srt_path, target_lang_code):
    """
    读取 SRT 文件，逐行翻译并保存。
    加入了防封锁休眠和自动重试机制。
    """
    try:
        subs = pysrt.open(input_srt_path)
    except Exception as e:
        print(f"     ❌ 读取字幕文件失败: {e}")
        return False

    # 初始化翻译器
    # 注意：deep-translator 的语言代码有些微不同，通常和 googletrans 是一致的 (如 'es', 'ja')
    translator = GoogleTranslator(source='auto', target=target_lang_code)
    
    total_lines = len(subs)
    print(f"     ⏳ 正在安全翻译字幕 (共 {total_lines} 行)，请耐心等待...")

    for i, sub in enumerate(subs):
        original_text = sub.text
        max_retries = 3 # 每句最多尝试 3 次
        
        for attempt in range(max_retries):
            try:
                # 核心翻译执行
                translated_text = translator.translate(original_text)
                sub.text = translated_text
                
                # 【防封锁核心】每翻译 10 句话，强制休息 1 秒，假装是人类操作
                if i > 0 and i % 10 == 0:
                    time.sleep(1)
                    
                break # 翻译成功，跳出重试循环
                
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"     ⚠️ 第 {i+1} 行翻译超时，正在进行第 {attempt+2} 次重试...")
                    time.sleep(2) # 遇到错误，休息 2 秒再试
                else:
                    print(f"     ❌ 第 {i+1} 行彻底翻译失败，保留原文。")
                    sub.text = original_text # 即使失败也保留原文，防止程序崩溃丢失进度

    # 保存翻译后的字幕
    try:
        subs.save(output_srt_path, encoding='utf-8')
        return True
    except Exception as e:
        print(f"     ❌ 保存翻译字幕失败: {e}")
        return False