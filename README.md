# 🔥 FuckOrNot - 图片AI评分工具 (Gradio版本)

一个基于Google Gemini API的图片AI评分工具，提供直观的Web界面。支持多种评分模式和emoji增强显示，让AI告诉你这张图片值不值得上。

## 250623更新：
- 修改了prompt，小说模式下回答会更粗俗
- 经过测试，虽然2.5模型的回答效果会更好，但审查过滤较严格，失败时可尝试更换2.0模型，或者更换更简短的模型

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

### 主要功能区域

#### 🔑 API密钥管理
- **API密钥输入框**：输入你的Gemini API密钥
- **测试API按钮**：验证API密钥是否有效
- **保存API按钮**：将API密钥保存到本地配置文件
- **提示**：点击链接可直接跳转到API密钥获取页面

#### 🤖 模型选择
- **可选模型**：
  - `gemini-2.5-flash-preview-05-20`（默认，推荐）
  - `gemini-2.0-flash`
  - `gemini-1.5-flash`

#### 🎯 评分模式
- **简短模式**：1-2句简洁评价
- **详细模式**：3-5句详细分析
- **小说模式**：15+句详细描述

#### 📸 图片处理
- **图片上传区域**：支持拖拽或点击上传
- **支持格式**：JPG, JPEG, PNG, GIF, BMP, WEBP
- **图片预览**：上传后自动显示预览

#### 🚀 操作按钮
- **开始评分按钮**：提交图片进行AI评分，显示处理进度
- **重置按钮**：清空图片和结果，开始新的评分任务

#### 📊 结果显示
- **评分结果**：显示格式为 `📊: 😋 上 (10/10) 👍` 或 `📊: 🤮 不上 (3/10) 👎`
- **详细说明**：显示AI的详细评价内容


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
- 可以使用"测试API"按钮验证密钥有效性

### Q5: 图片上传失败
**检查项目：**
- 图片格式是否支持
- 图片文件是否损坏
- 图片大小是否过大（建议<10MB）

### Q6: 评分请求超时
**解决方案：**
- 检查网络连接
- 尝试更换网络环境
- 刷新网页重试

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