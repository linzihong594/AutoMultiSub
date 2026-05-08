# AutoMultiSub (全自动多语言视频字幕压制工具)

AutoMultiSub 是一个基于 Python 和 FFmpeg 的自动化工具，旨在将单语种（如英文）字幕文件自动翻译为多国语言，并根据预设的视觉样式（参考剪映标准）将字幕烧录（Hardsub）进 9:16 竖屏视频中。

## 🌟 核心功能

- **多语言自动翻译**：集成 Google Translate API，一键生成多国语言字幕。
- **工业级目录管理**：自动根据项目名、集数和语种生成规范的文件夹树。
- **高精度硬字幕烧录**：利用 FFmpeg 将字幕直接压制进视频画面。
- **剪映样式复刻**：通过 `subtitle_style.py` 完美适配剪映的字号、位置和描边参数。
- **画质无损**：默认采用 `CRF 18` 高质量编码，适配 720p/1080p 竖屏短视频。

## 📁 目录结构

```text
AutoMultiSub/
│
├── raw-data/                  # [输入] 存放原始文件 (EP01.mp4, EP01.srt)
├── results/                   # [输出] 自动生成的成品视频文件夹树
│
├── core/                      # [核心模块]
│   ├── __init__.py
│   ├── config.py              # 语言映射与路径配置
│   ├── folder_manager.py      # 自动化目录生成逻辑
│   ├── translator.py          # 字幕翻译引擎
│   ├── video_processor.py     # FFmpeg 视频合成逻辑
│   └── subtitle_style.py      # 字幕样式自定义配置（重点修改此文件）
│
├── main.py                    # [主程序] 逻辑调度入口
└── requirements.txt           # [依赖清单] Python 库清单
```

## 🛠️ 环境准备

### 1. FFmpeg 安装
本项目极度依赖 **FFmpeg** 处理器：
1. 下载并解压 FFmpeg。
2. 在 `core/video_processor.py` 中将 `FFMPEG_PATH` 修改为你电脑上的实际绝对路径：
   `FFMPEG_PATH = r"D:\ffmpeg\bin\ffmpeg.exe"`

### 2. Python 依赖
建议在虚拟环境中运行：
```bash
pip install -r requirements.txt
```

## 🚀 使用指南

1. **放置素材**：
   将你的无字幕原视频（如 `EP01.mp4`）和对应的英文字幕（如 `EP01.srt`）放入 `raw-data/` 目录。
2. **修改配置**：
   - 打开 `core/config.py` 修改 `LANGUAGE_MAP`（需要生成的语种）。
   - 打开 `core/subtitle_style.py` 调整字号、描边和底部边距。
3. **运行程序**：
   ```bash
   python main.py
   ```
4. **查看结果**：
   处理完成后，在 `results/` 目录下即可看到按语种分类好的、压制好硬字幕的 MP4 视频。

## ⚠️ 注意事项

- **坐标系陷阱**：FFmpeg 处理 SRT 字幕时使用的是 288p 虚拟画布，`subtitle_style.py` 已内置换算公式，请直接填入你量出的 720p 真实像素值。
- **网络环境**：翻译模块依赖 Google 服务，请确保你的网络环境可以正常访问。
- **字体支持**：默认使用 `Microsoft YaHei`，若需其他字体请确保系统中已安装该字体。
