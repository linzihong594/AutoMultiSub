# AutoMultiSub (全自动多语言视频字幕压制工具)

AutoMultiSub 是一个基于 Python 和 FFmpeg 的工业级自动化工具。它能够将单语种（如英文）字幕文件自动翻译为多国语言，并根据精准的视觉样式（完美复刻剪映排版），将字幕无损烧录（Hardsub）进 9:16 竖屏短视频中。

## 🌟 核心功能

- **防封锁翻译引擎**：弃用传统易崩溃的翻译库，采用 `deep-translator`。内置自动重试与防封锁脉冲（休眠）机制，从容应对长篇字幕批量翻译。
- **工业级目录管理**：无需手动建文件夹。自动根据“项目名、集数、语种”生成整洁嵌套的成品分类目录树。
- **高精度硬字幕烧录**：利用 FFmpeg 底层滤镜将字幕直接烙印在视频像素上，任何平台播放均自带字幕。
- **剪映级排版复刻**：在 `subtitle_style.py` 中直接填入你测算的 720p/1080p 视觉尺寸，脚本会自动处理 FFmpeg 恶心的底层坐标系换算。
- **画质无损渲染**：默认采用 `CRF 18` 视觉无损高画质编码，完美适配 TikTok、YouTube Shorts、Reels 等高清竖屏平台。

## 📁 目录结构

```text
AutoMultiSub/
│
├── raw-data/                  # [输入] 存放原始文件 (如: EP01.mp4, EP01.srt)
├── results/                   # [输出] 自动生成的成品视频与字幕归档库
│
├── core/                      # [核心引擎]
│   ├── __init__.py
│   ├── config.py              # 语言映射表与全局路径配置
│   ├── folder_manager.py      # 自动化目录生成器
│   ├── translator.py          # 智能字幕翻译模块 (含重试保护)
│   ├── video_processor.py     # FFmpeg 视频压制中心
│   └── subtitle_style.py      # 🎨 字幕样式控制台（调字号/位置重点修改此文件）
│
├── main.py                    # [主程序] 自动化流水线入口
└── requirements.txt           # [依赖清单] Python 第三方库清单
```

## 🛠️ 环境准备

### 1. 部署 FFmpeg 核心
本项目依赖 **FFmpeg** 进行视频处理：
1. 下载并解压 Windows 版 FFmpeg。
2. 打开 `core/video_processor.py`，将 `FFMPEG_PATH` 变量修改为你电脑上的绝对路径，例如：
   `FFMPEG_PATH = r"D:\ffmpeg\bin\ffmpeg.exe"`

### 2. 安装 Python 依赖
请确保你的环境中已安装清单内的库（包含 `pysrt` 和 `deep-translator`）。
在终端运行以下命令：
```bash
pip install -r requirements.txt
```

## 🚀 使用指南

1. **放置素材**：
   将你的无字幕原视频（如 `EP01.mp4`）和对应的英文字幕（如 `EP01.srt`）放入 `raw-data/` 目录。
2. **个性化配置**：
   - 🌐 **改语种**：打开 `core/config.py`，在 `LANGUAGE_MAP` 中增删你需要生成的国家语言。
   - 🎨 **改样式**：打开 `core/subtitle_style.py`，直接输入你想要的字号、底部边距、描边粗细（支持微调字间距）。
3. **一键启动**：
   ```bash
   python main.py
   ```
4. **验收成果**：
   去喝杯咖啡☕。处理完成后，在 `results/` 目录下即可获得按语种分类好的、压制完毕的 MP4 终极视频！

## ⚠️ 注意事项与避坑指南

- **坐标系陷阱（已解决）**：FFmpeg 处理 SRT 字幕时使用的是 288p 的微型虚拟画布。你**不需要**自己算比例，只需在 `subtitle_style.py` 里直接填入你量出的 720p 真实像素值，代码会自动为你换算投射。
- **网络环境**：翻译模块底层依赖 Google 翻译服务。虽然代码自带防封锁重试机制，但仍需确保你的本地网络环境能够稳定访问国际网络。
- **中日文字体支持**：代码默认强制使用 `Microsoft YaHei` (微软雅黑) 渲染中日文字符，以防出现系统默认的生硬宋体或乱码。如果你想换成“优设标题黑”等网红字体，请先确保电脑已安装该字体，并在代码中修改英文名称。
