#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
启动Gradio可视化界面的便捷脚本
"""

import sys
import os
from pathlib import Path

# 添加fuckornot目录到Python路径
project_root = Path(__file__).parent
fuckornot_dir = project_root / "fuckornot"
sys.path.insert(0, str(fuckornot_dir))

try:
    from gradio_app import main
    
    if __name__ == "__main__":
        print("🎉 欢迎使用图片AI评分工具 - Gradio版本")
        print("📋 功能特点:")
        print("   • 🔑 API密钥管理（保存/测试）")
        print("   • 🤖 多种AI模型选择")
        print("   • 🎯 三种评分模式")
        print("   • 📸 图片上传与预览")
        print("   • 📊 emoji增强的评分显示")
        print("   • 🔄 一键重置功能")
        print("")
        print("🚀 正在启动应用...")
        
        main()
        
except ImportError as e:
    print("❌ 导入错误:", e)
    print("")
    print("📦 请先安装依赖:")
    print("   pip install -r requirements.txt")
    print("")
    print("📁 确保文件结构正确:")
    print("   fuckornot/")
    print("   ├── gradio_app.py")
    print("   └── config.json")
except Exception as e:
    print("❌ 启动失败:", e)
    print("")
    print("🔍 可能的解决方案:")
    print("   1. 检查Python版本 (推荐3.8+)")
    print("   2. 重新安装依赖: pip install -r requirements.txt")
    print("   3. 检查网络连接")
    print("   4. 确保端口7860未被占用")