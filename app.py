import streamlit as st
import os
import base64

# 1. 配置
st.set_page_config(layout="wide")
ASSETS_DIR = "assets/genshin"

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 2. 动态获取资源列表
banners = [f for f in os.listdir(f"{ASSETS_DIR}/banners") if f.endswith(('.png', '.jpg'))]
current_banner = f"{ASSETS_DIR}/banners/{banners[0]}" # 默认显示第一张

# 3. 注入 CSS 
bg_base64 = get_base64(current_banner)
st.markdown(f"""
<style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{bg_base64}");
        background-size: cover;
    }}
    .pull-box {{ position: fixed; bottom: 50px; right: 50px; display: flex; gap: 20px; }}
</style>
""", unsafe_allow_html=True)

# 4. 模拟抽卡交互
st.markdown('<div class="pull-box">', unsafe_allow_html=True)
if st.button("祈愿 1 次"):
    st.balloons()
if st.button("祈愿 10 次"):
    st.snow()
st.markdown('</div>', unsafe_allow_html=True)
