import streamlit as st
import base64

# 1. 页面基础配置：必须设置为 wide 模式，让页面占满屏幕
st.set_page_config(
    page_title="全二游抽卡模拟器",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 核心：CSS 强行注入，去除所有 Streamlit 默认边距，并设置全局背景图
# 假设你在项目根目录建了一个 assets 文件夹，里面有一张 bg_genshin.jpg
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 这里你可以替换成你抓取到的卡池背景图路径
# bg_base64 = get_base64_of_bin_file("assets/bg_genshin.jpg")
# 为了演示，这里用一个纯色渐变替代背景图
custom_css = f"""
<style>
    /* 隐藏顶部导航条和右下角 watermark */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* 强行抹平所有的内边距和外边距，让背景铺满 */
    .block-container {{
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }}
    
    /* 设置全局背景，实际应用中将下面的 background 替换为 url(data:image/jpeg;base64,{bg_base64}) */
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    
    /* 自定义一个底部按钮区域的样式 */
    .button-container {{
        position: fixed;
        bottom: 50px;
        right: 50px;
        display: flex;
        gap: 20px;
    }}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. 布局结构：利用空行把按钮推到屏幕底部右侧（模仿游戏内布局）
# 使用多个 st.write() 或者 st.container() 占位
for _ in range(20):
    st.write("")

# 4. 交互组件：抽卡按钮
col1, col2, col3, col4 = st.columns([6, 1, 1, 1])

with col2:
    if st.button("祈愿 1 次"):
        st.toast("单抽触发！")
with col3:
    if st.button("祈愿 10 次"):
        st.toast("十连触发！")
