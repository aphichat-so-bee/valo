import streamlit as st
import plotly.express as px
from prx_analytics import PRXAnalytics

# กำหนดรูปแบบหน้าเว็บ Streamlit
st.set_page_config(
    page_title="PRX VALORANT Analytics",
    page_icon="🦖",
    layout="wide"
)

# ส่วนหัวของ Web Application
st.title("🦖 PRX W-Gaming Strategy Dashboard")
st.caption("ระบบวิเคราะห์และจำลองแผนการเล่น VALORANT เชิงลึกจากกรณีศึกษาแชมป์ Paper Rex")
st.markdown("---")

# โหลดข้อมูลผ่าน Analytics Engine
analytics = PRXAnalytics()
df = analytics.get_summary_dataframe()
w_score = analytics.calculate_w_gaming_index(df)

# แสดงตัวเลขสถิติสำคัญ (KPI Metrics)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="🏆 Win Rate ภาพรวม", value="69.5%", delta="+12.3%")
with col2:
    st.metric(label="⚡ W-Gaming Aggressiveness Index", value=f"{w_score}/100", delta="High Risk/Reward")
with col3:
    st.metric(label="💥 Avg First Kills / Match", value=f"{df['First_Kills'].mean():.1f}")
with col4:
    st.metric(label="🎯 Total Clutch Rounds", value=f"{df['Clutch_Rounds'].sum()}")

st.markdown("---")

# ส่วนแสดงผลกราฟิกและตาราง
left_col, right_col = st.columns([3, 2])

with left_col:
    st.subheader("📊 Win Rate & First Kills แยกตามแผนที่ (Map)")
    fig = px.bar(
        df, 
        x="Map", 
        y="Win_Rate", 
        color="Result",
        text="Agent_Comp",
        title="สถิติการแข่งขันแบ่งตามแผนที่",
        color_discrete_map={"Win": "#00d26a", "Loss": "#f8312f"}
    )
    fig.update_layout(template="plotly_dark", yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.subheader("🧠 บทวิเคราะห์แผนการเล่นจาก AI (Tactical Insight)")
    selected_map = st.selectbox("เลือกแผนที่เพื่อดูบทวิเคราะห์:", df['Map'].unique())
    
    map_info = df[df['Map'] == selected_map].iloc[0]
    st.info(f"**Agent Composition:** {map_info['Agent_Comp']}")
    
    if map_info['Result'] == 'Win':
        st.success(f"**กลยุทธ์สำคัญ:** เน้นการเทรดแฟลชอย่างรวดเร็วและการเปิดพื้นที่ด้วย First Kill ({map_info['First_Kills']} ครั้ง) ทำให้ฝ่ายตรงข้ามตั้งรับไม่ทัน")
    else:
        st.warning(f"**จุดที่ต้องปรับปรุง:** โดนแก้ทางสไตล์การบุกไว ฝ่ายตรงข้ามใช้ Utility ชะลอการเข้าทำได้ดี")

# แสดงตารางข้อมูลดิบด้านล่าง
with st.expander("📂 ดูข้อมูลแมตช์การแข่งขันทั้งหมด (Raw Match Data)"):
    st.dataframe(df, use_container_width=True)