# core/subtitle_style.py

def get_style_string():
    # =====================================================================
    # 🎨 1. 基础排版数值
    # =====================================================================
    measured_fontsize = 45       
    measured_margin_v = 405      
    measured_outline = 3.5       
    measured_spacing = 1.0       

    # 字体源（华康金刚黑）
    font_name = "DFP King Gothic GB" 

    # =====================================================================
    # 🌟 2. 阴影系统 (新增)
    # =====================================================================
    # measured_shadow: 阴影向右下的偏移量。设为 0 就是没阴影，设为 3-5 会有明显的投影
    measured_shadow = 0 
    
    # 阴影颜色 (BackColour)：格式为 &H[透明度][蓝][绿][红]
    # &H00000000 是纯黑不透明；&H80000000 是半透明纯黑 (剪映默认感觉)
    shadow_color = "&H80000000"

    # =====================================================================
    # 🤖 3. 自动坐标系转换 
    # =====================================================================
    scale = 288 / 1280.0
    
    ass_fontsize = max(1, int(measured_fontsize * scale))
    ass_margin_v = int(measured_margin_v * scale)
    ass_outline = max(0, round(measured_outline * scale, 1))
    ass_spacing = round(measured_spacing * scale, 1)
    
    # 阴影也需要等比缩小
    ass_shadow = round(measured_shadow * scale, 1)

    primary_color = "&H00FFFFFF" 
    outline_color = "&H00000000"
    alignment = 2

    # =====================================================================
    # 4. 组装最终格式
    # =====================================================================
    styles = [
        f"Fontname={font_name}",
        f"Fontsize={ass_fontsize}",
        f"PrimaryColour={primary_color}",
        f"OutlineColour={outline_color}",
        f"BackColour={shadow_color}",  # 【新增】指定阴影颜色
        f"Outline={ass_outline}",
        f"Shadow={ass_shadow}",        # 【修改】激活阴影偏移
        f"Alignment={alignment}",
        f"MarginV={ass_margin_v}",
        f"Spacing={ass_spacing}",
        "BorderStyle=1"                # 确保是正常的描边模式
    ]
    
    return ",".join(styles)