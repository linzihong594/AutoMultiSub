# core/config.py

# 定义全局的输入和输出根目录
INPUT_DIR = "raw-data"
OUTPUT_DIR = "results"

# 配置目标语言代码及对应的中文名称（用于生成分类文件夹）
# 字典的 Key 是 googletrans 识别的语言代码，Value 是你要建的文件夹名称
LANGUAGE_MAP = {
    'pt': '葡语',
    'ja': '日语',
    'tr': '土耳其语',
    'es': '西班牙语',
    'id': '印尼语',
    'en': '英语' # 原文语种，用于触发直接复制的逻辑
}