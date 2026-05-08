# core/subtitle_style.py

def get_style_string():
    # =====================================================================
    # 🎨 1. 请在这里直接填入你量出来的真实 720p 尺寸！
    # =====================================================================
    measured_fontsize = 45       # 你的字号
    measured_margin_v = 405      # 你的底部边距
    measured_outline = 3.5       # 你的描边粗细
    
    # 调整字间距：默认 0。如果是正数，字会散开；如果是负数（如 -1），字会紧凑
    measured_spacing = 1.0       

    # 更改字体：
    font_name = "King Gothic"   # 使用华康金刚黑（剪映“系统”字体，禁止商用！！！）

    # =====================================================================
    # 🤖 2. 自动坐标系转换 (你不需要管这里)
    # 将你的 720p 数值自动翻译为 FFmpeg 底层的 288p 微型坐标系
    # =====================================================================
    scale = 288 / 1280.0 
    
    ass_fontsize = max(1, int(measured_fontsize * scale))
    ass_margin_v = int(measured_margin_v * scale)
    ass_outline = max(0, round(measured_outline * scale, 1))
    ass_spacing = round(measured_spacing * scale, 1)

    # 颜色配置 (&H00BBGGRR)
    primary_color = "&H00FFFFFF" 
    outline_color = "&H00000000"
    alignment = 2 # 底部居中

    # =====================================================================
    # 3. 组装为 FFmpeg 认识的最终格式
    # =====================================================================
    styles = [
        f"Fontname={font_name}",
        f"Fontsize={ass_fontsize}",
        f"PrimaryColour={primary_color}",
        f"OutlineColour={outline_color}",
        f"Outline={ass_outline}",
        "Shadow=0",
        f"Alignment={alignment}",
        f"MarginV={ass_margin_v}",
        f"Spacing={ass_spacing}"
    ]
    
    return ",".join(styles)