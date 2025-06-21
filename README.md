# 🌐 Gradio界面的FuckOrNot使用指南

## 📋 目录
- [快速开始](#快速开始)
- [详细启动步骤](#详细启动步骤)
- [界面功能介绍](#界面功能介绍)
- [常见问题解决](#常见问题解决)
- [高级配置](#高级配置)

## 🚀 快速开始

### 方法1：使用批处理文件（Windows推荐）
```bash
# 双击运行
start_gradio.bat
```

### 方法2：使用Python脚本
```bash
# 安装依赖
pip install -r requirements.txt

# 启动应用
python run_gradio.py
```


## 📦 详细启动步骤

### 1. 检查Python版本
```bash
python --version
# 需要Python 3.8或更高版本
```

### 2. 安装依赖包
```bash
# 方法1：使用requirements.txt
pip install -r requirements.txt

# 方法2：手动安装
pip install gradio>=4.0.0 Pillow>=9.0.0 requests>=2.25.0

# 方法3：使用国内镜像（如果下载慢）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gradio Pillow requests
```

### 3. 获取API密钥
1. 访问 [Google AI Studio](https://aistudio.google.com/app/apikey)
2. 登录Google账号
3. 创建新的API密钥
4. 复制密钥备用

### 4. 启动应用
```bash
python run_gradio.py
```

## 🎨 界面功能介绍

### 配置区域（左侧）

#### 🔑 API密钥输入框
- **功能**：输入你的Gemini API密钥
- **类型**：密码框（输入内容会被隐藏）
- **提示**：点击链接可直接跳转到API密钥获取页面

#### 🤖 模型选择下拉菜单
- **可选模型**：
  - `gemini-2.5-flash-preview-05-20`（默认，推荐）
  - `gemini-2.0-flash`
  - `gemini-1.5-flash`

#### ⏱️ 超时时间滑块
- **范围**：10-120秒
- **默认**：30秒
- **建议**：网络较慢时可适当增加

#### 🎯 评分模式单选按钮
- **简短模式**：1-2句简洁评价
- **详细模式**：3-5句详细分析
- **小说模式**：10+句详细描述

#### 🚀 开始评分按钮
- **功能**：提交图片进行AI评分
- **状态**：点击后会显示处理进度

#### 🔄 重置按钮
- **功能**：清空图片和结果
- **用途**：开始新的评分任务


## 🔧 常见问题解决

### Q1: 启动时提示"ModuleNotFoundError: No module named 'gradio'"
**解决方案：**
```bash
pip install gradio
```

### Q2: 浏览器没有自动打开
**解决方案：**
- 手动访问：`http://localhost:7860`
- 或者：`http://127.0.0.1:7860`

### Q3: 端口7860被占用
**解决方案：**
1. 重启电脑
2. 或修改`gradio_app.py`中的端口号：
   ```python
   app.launch(server_port=7861)  # 改为其他端口
   ```

### Q4: API密钥无效
**检查项目：**
- 密钥是否正确复制（无多余空格）
- API密钥是否已启用Gemini服务
- 是否有足够的API配额

### Q5: 图片上传失败
**检查项目：**
- 图片格式是否支持
- 图片文件是否损坏
- 图片大小是否过大（建议<10MB）

### Q6: 评分请求超时
**解决方案：**
- 增加超时时间设置
- 检查网络连接
- 尝试更换网络环境

### Q7: 界面显示异常
**解决方案：**
- 刷新浏览器页面
- 清除浏览器缓存
- 尝试其他浏览器

## ⚙️ 高级配置

### 自定义启动参数
修改`gradio_app.py`中的`app.launch()`参数：

```python
app.launch(
    server_name="0.0.0.0",    # 允许外部访问
    server_port=7860,         # 端口号
    share=True,               # 创建公共链接
    inbrowser=True,           # 自动打开浏览器
    show_error=True,          # 显示错误信息
    auth=("username", "password")  # 添加登录验证
)
```

### 环境变量配置
可以通过环境变量设置默认API密钥：

```bash
# Windows
set GEMINI_API_KEY=your_api_key_here
python run_gradio.py

# Linux/Mac
export GEMINI_API_KEY=your_api_key_here
python run_gradio.py
```

### 自定义主题
修改`gradio_app.py`中的主题设置：

```python
with gr.Blocks(theme=gr.themes.Glass()) as app:  # 玻璃主题
# 或
with gr.Blocks(theme=gr.themes.Monochrome()) as app:  # 黑白主题
```


**享受使用这个项目！** 🎉