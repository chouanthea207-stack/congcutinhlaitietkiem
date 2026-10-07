import streamlit as st
import pandas as pd
import numpy as np

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Smart Savings Planner",
    page_icon="💰",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #666;
    font-size: 17px;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #f7f8fa;
    border: 1px solid #e5e7eb;
    margin-bottom: 15px;
}

.card-title {
    font-size: 15px;
    color: #666;
}

.card-value {
    font-size: 25px;
    font-weight: 700;
}

.target-box {
    padding: 25px;
    border-radius: 15px;
    background-color: #f7f8fa;
    border: 1px solid #ddd;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HÀM FORMAT TIỀN
# =========================================================

def format_money(value):
    return f"{value:,.0f} VNĐ"


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("💰 Smart Savings")

menu = st.sidebar.radio(
    "Chọn chức năng",
    [
        "🏠 Trang chủ",
        "🧮 Tính lãi tiết kiệm",
        "⚖️ So sánh lãi đơn & lãi kép",
        "🎯 Mục tiêu tiết kiệm",
        "📚 Kiến thức tài chính"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    """
    **Smart Savings Planner**

    Công cụ hỗ trợ mô phỏng tiền gửi,
    lãi suất và kế hoạch tiết kiệm.

    *Kết quả chỉ mang tính tham khảo.*
    """
)


# =========================================================
# TRANG CHỦ
# =========================================================

if menu == "🏠 Trang chủ":

    st.markdown(
        '<div class="main-title">💰 SMART SAVINGS PLANNER</div>',
        '<div style="text-align:center; color:#666; font-size:16px;">'
        'Đỗ Trương Bảo Châu'
        '</div.>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Công cụ mô phỏng và lập kế hoạch tiết kiệm cá nhân'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">🧮 TÍNH LÃI</div>
            <div class="card-value">Lãi đơn & Lãi kép</div>
            <p>Mô phỏng tiền lãi theo nhiều hình thức.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">📊 PHÂN TÍCH</div>
            <div class="card-value">Biểu đồ trực quan</div>
            <p>Theo dõi sự tăng trưởng của khoản tiền.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-title">🎯 MỤC TIÊU</div>
            <div class="card-value">Lập kế hoạch</div>
            <p>Tính số tiền cần tiết kiệm để đạt mục tiêu.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("✨ Các chức năng chính")

    features = pd.DataFrame({
        "Chức năng": [
            "Tính lãi đơn",
            "Tính lãi kép",
            "Lãnh lãi theo tháng",
            "Lãnh lãi theo quý",
            "Lãnh lãi cuối kỳ",
            "So sánh lãi đơn và lãi kép",
            "Mục tiêu tiết kiệm",
            "Gửi thêm hàng tháng",
            "Biểu đồ tăng trưởng"
        ],
        "Trạng thái": ["✅"] * 9
    })

    st.dataframe(
        features,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# TÍNH LÃI TIẾT KIỆM
# =========================================================

elif menu == "🧮 Tính lãi tiết kiệm":

    st.markdown(
        '<div class="main-title">🧮 TÍNH LÃI TIẾT KIỆM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Mô phỏng khoản tiền gửi theo lãi đơn hoặc lãi kép'
        '</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # INPUT
    # -----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        tien_gui = st.number_input(
            "💵 Số tiền gửi ban đầu (VNĐ)",
            min_value=0,
            value=10000000,
            step=500000
        )

        ky_han = st.number_input(
            "⏳ Kỳ hạn (tháng)",
            min_value=1,
            max_value=600,
            value=12
        )

        lai_suat = st.number_input(
            "📈 Lãi suất (%/năm)",
            min_value=0.0,
            max_value=100.0,
            value=6.0,
            step=0.1
        )

    with col2:

        loai_lai = st.selectbox(
            "🧮 Hình thức tính lãi",
            [
                "Lãi đơn",
                "Lãi kép"
            ]
        )

        hinh_thuc = st.selectbox(
            "💳 Hình thức nhận lãi",
            [
                "Lãnh lãi theo tháng",
                "Lãnh lãi theo quý",
                "Lãnh lãi cuối kỳ"
            ]
        )

        gui_them = st.number_input(
            "💸 Gửi thêm mỗi tháng (VNĐ)",
            min_value=0,
            value=0,
            step=500000
        )

    st.divider()

    tinh = st.button(
        "🧮 TÍNH TOÁN",
        use_container_width=True
    )

    if tinh:

        r = lai_suat / 100
        so_thang = int(ky_han)

        # -------------------------------------------------
        # TÍNH LÃI
        # -------------------------------------------------

        data = []

        tong_tien = float(tien_gui)

        # LÃI ĐƠN
        if loai_lai == "Lãi đơn":

            for month in range(1, so_thang + 1):

                tien_dau_ky = tong_tien

                # Gửi thêm đầu mỗi tháng
                tong_tien += gui_them

                lai_thang = tien_gui * r / 12

                tong_tien += lai_thang

                data.append({
                    "Tháng": month,
                    "Tiền đầu kỳ": tien_dau_ky,
                    "Gửi thêm": gui_them,
                    "Tiền lãi": lai_thang,
                    "Tổng tiền": tong_tien
                })

        # LÃI KÉP
        else:

            for month in range(1, so_thang + 1):

                tien_dau_ky = tong_tien

                tong_tien += gui_them

                lai_thang = tong_tien * r / 12

                tong_tien += lai_thang

                data.append({
                    "Tháng": month,
                    "Tiền đầu kỳ": tien_dau_ky,
                    "Gửi thêm": gui_them,
                    "Tiền lãi": lai_thang,
                    "Tổng tiền": tong_tien
                })

        df = pd.DataFrame(data)

        tong_tien_gui = tien_gui + gui_them * so_thang

        tong_lai = tong_tien - tong_tien_gui

        # -------------------------------------------------
        # LÃI ĐỊNH KỲ
        # -------------------------------------------------

        if hinh_thuc == "Lãnh lãi theo tháng":

            lai_dinh_ky = df.iloc[-1]["Tiền lãi"]

        elif hinh_thuc == "Lãnh lãi theo quý":

            lai_dinh_ky = (
                df.iloc[-1]["Tiền lãi"] * 3
            )

        else:

            lai_dinh_ky = tong_lai

        # -------------------------------------------------
        # DASHBOARD
        # -------------------------------------------------

        st.subheader("📊 Kết quả")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "💵 Tổng tiền gửi",
                format_money(tong_tien_gui)
            )

        with c2:
            st.metric(
                "📈 Tổng tiền lãi",
                format_money(tong_lai)
            )

        with c3:
            st.metric(
                "💰 Tổng nhận",
                format_money(tong_tien)
            )

        with c4:
            st.metric(
                "💳 Lãi định kỳ",
                format_money(lai_dinh_ky)
            )

        st.divider()

        # -------------------------------------------------
        # BIỂU ĐỒ
        # -------------------------------------------------

        st.subheader("📈 Biểu đồ tăng trưởng")

        chart_df = df[
            ["Tháng", "Tổng tiền"]
        ].set_index("Tháng")

        st.line_chart(chart_df)

        # -------------------------------------------------
        # BẢNG CHI TIẾT
        # -------------------------------------------------

        st.subheader("📋 Chi tiết từng tháng")

        display_df = df.copy()

        for col in [
            "Tiền đầu kỳ",
            "Gửi thêm",
            "Tiền lãi",
            "Tổng tiền"
        ]:
            display_df[col] = display_df[col].apply(
                format_money
            )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

        # -------------------------------------------------
        # CÔNG THỨC
        # -------------------------------------------------

        st.subheader("🧮 Công thức")

        if loai_lai == "Lãi đơn":

            st.info(
                """
                **Lãi đơn**

                Tiền lãi = Tiền gốc × Lãi suất × Thời gian

                Với tiền gửi theo tháng:

                Tiền lãi tháng = Tiền gốc × Lãi suất năm / 12
                """
            )

        else:

            st.info(
                """
                **Lãi kép**

                Tiền cuối kỳ = Tiền đầu kỳ × (1 + lãi suất kỳ)

                Tiền lãi được cộng vào vốn,
                sau đó tiếp tục sinh lãi ở kỳ tiếp theo.
                """
            )


# =========================================================
# SO SÁNH LÃI ĐƠN VÀ LÃI KÉP
# =========================================================

elif menu == "⚖️ So sánh lãi đơn & lãi kép":

    st.markdown(
        '<div class="main-title">⚖️ SO SÁNH LÃI ĐƠN & LÃI KÉP</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Xem sự khác biệt giữa hai phương pháp tính lãi'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        principal = st.number_input(
            "💵 Số tiền ban đầu",
            min_value=0,
            value=10000000,
            step=500000
        )

    with col2:

        rate = st.number_input(
            "📈 Lãi suất (%/năm)",
            min_value=0.0,
            value=6.0,
            step=0.1
        )

    with col3:

        months = st.number_input(
            "⏳ Kỳ hạn (tháng)",
            min_value=1,
            value=60,
            step=1
        )

    r = rate / 100

    simple_values = []
    compound_values = []

    for month in range(1, int(months) + 1):

        # Lãi đơn
        simple = principal * (
            1 + r * month / 12
        )

        # Lãi kép
        compound = principal * (
            1 + r / 12
        ) ** month

        simple_values.append(simple)
        compound_values.append(compound)

    compare_df = pd.DataFrame({
        "Tháng": range(1, int(months) + 1),
        "Lãi đơn": simple_values,
        "Lãi kép": compound_values
    })

    st.subheader("📈 Biểu đồ so sánh")

    chart_compare = compare_df.set_index("Tháng")

    st.line_chart(chart_compare)

    st.subheader("📊 Kết quả cuối kỳ")

    final_simple = simple_values[-1]
    final_compound = compound_values[-1]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Lãi đơn",
            format_money(final_simple)
        )

    with c2:
        st.metric(
            "Lãi kép",
            format_money(final_compound)
        )

    with c3:

        difference = final_compound - final_simple

        st.metric(
            "Chênh lệch",
            format_money(difference)
        )

    st.info(
        "💡 Với lãi kép, tiền lãi được cộng vào vốn "
        "và tiếp tục tạo ra tiền lãi ở các kỳ sau."
    )


# =========================================================
# MỤC TIÊU TIẾT KIỆM
# =========================================================

elif menu == "🎯 Mục tiêu tiết kiệm":

    st.markdown(
        '<div class="main-title">🎯 MỤC TIÊU TIẾT KIỆM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Tính số tiền cần tiết kiệm để đạt mục tiêu'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        muc_tieu = st.number_input(
            "🎯 Số tiền mục tiêu (VNĐ)",
            min_value=100000,
            value=100000000,
            step=1000000
        )

        tien_ban_dau = st.number_input(
            "💵 Số tiền đang có (VNĐ)",
            min_value=0,
            value=10000000,
            step=500000
        )

    with col2:

        lai_muc_tieu = st.number_input(
            "📈 Lãi suất (%/năm)",
            min_value=0.0,
            value=6.0,
            step=0.1
        )

        thoi_gian = st.number_input(
            "⏳ Thời gian (tháng)",
            min_value=1,
            value=24,
            step=1
        )

    if st.button(
        "🎯 TÍNH KẾ HOẠCH",
        use_container_width=True
    ):

        r = lai_muc_tieu / 100 / 12
        n = int(thoi_gian)

        # Giá trị tương lai của tiền ban đầu
        future_initial = tien_ban_dau * (
            1 + r
        ) ** n

        # Khoản tiền còn thiếu
        con_thieu = muc_tieu - future_initial

        if con_thieu <= 0:

            st.success(
                "🎉 Với số tiền hiện tại và mức lãi suất "
                "đã chọn, bạn có thể đạt mục tiêu trong "
                "khoảng thời gian này mà chưa cần gửi thêm."
            )

        elif r > 0:

            # Công thức niên kim
            monthly_saving = con_thieu * r / (
                (1 + r) ** n - 1
            )

            tong_gui_them = monthly_saving * n

            tong_lai = (
                muc_tieu
                - tien_ban_dau
                - tong_gui_them
            )

            st.subheader("📊 Kế hoạch đề xuất")

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "💸 Cần gửi mỗi tháng",
                    format_money(monthly_saving)
                )

            with c2:

                st.metric(
                    "💵 Tổng tiền gửi thêm",
                    format_money(tong_gui_them)
                )

            with c3:

                st.metric(
                    "📈 Tiền lãi dự kiến",
                    format_money(tong_lai)
                )

            st.divider()

            st.progress(
                min(
                    tien_ban_dau / muc_tieu,
                    1.0
                )
            )

            st.write(
                f"🎯 Mục tiêu: **{format_money(muc_tieu)}**"
            )

            st.write(
                f"💵 Số tiền hiện có: **{format_money(tien_ban_dau)}**"
            )

            st.write(
                f"💸 Mỗi tháng cần tiết kiệm khoảng "
                f"**{format_money(monthly_saving)}**"
            )

        else:

            monthly_saving = con_thieu / n

            st.metric(
                "💸 Cần gửi mỗi tháng",
                format_money(monthly_saving)
            )


# =========================================================
# KIẾN THỨC TÀI CHÍNH
# =========================================================

elif menu == "📚 Kiến thức tài chính":

    st.markdown(
        '<div class="main-title">📚 KIẾN THỨC TÀI CHÍNH</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Một số khái niệm cơ bản về tiền gửi và lãi suất'
        '</div>',
        unsafe_allow_html=True
    )

    with st.expander("💡 Lãi đơn là gì?"):

        st.write(
            """
            Lãi đơn là phương pháp tính lãi trong đó
            tiền lãi của mỗi kỳ được tính dựa trên
            số tiền gốc ban đầu.

            Tiền lãi không được cộng vào vốn để
            tiếp tục sinh lãi.
            """
        )

        st.latex(
            r"I = P \times r \times t"
        )

    with st.expander("💡 Lãi kép là gì?"):

        st.write(
            """
            Lãi kép là phương pháp trong đó tiền lãi
            của kỳ trước được cộng vào vốn.

            Sang kỳ tiếp theo, tiền lãi được tính
            trên cả vốn ban đầu và phần lãi đã tích lũy.
            """
        )

        st.latex(
            r"FV = PV(1+r)^n"
        )

    with st.expander("💡 Lãi đơn và lãi kép khác nhau như thế nào?"):

        st.write(
            """
            Điểm khác biệt quan trọng nhất là cách xử lý
            phần tiền lãi.

            • Lãi đơn: lãi không nhập vào vốn.

            • Lãi kép: lãi được nhập vào vốn và tiếp tục
            tạo ra lãi trong các kỳ tiếp theo.
            """
        )

    with st.expander("💡 Lãi suất %/năm nghĩa là gì?"):

        st.write(
            """
            Lãi suất 6%/năm có nghĩa là mức lãi suất
            danh nghĩa được tính trên cơ sở một năm.

            Khi mô phỏng theo tháng, lãi suất năm thường
            được quy đổi thành lãi suất tháng bằng cách
            chia cho 12.
            """
        )

    with st.expander("💡 Vì sao nên theo dõi kế hoạch tiết kiệm?"):

        st.write(
            """
            Việc đặt mục tiêu cụ thể giúp người tiết kiệm
            biết mình cần tích lũy bao nhiêu tiền mỗi tháng
            và trong bao lâu để đạt được mục tiêu tài chính.
            """
        )

    st.success(
        "📌 Lưu ý: Lãi suất và phương thức tính lãi thực tế "
        "có thể khác nhau tùy từng ngân hàng và sản phẩm tiền gửi."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "💰 Smart Savings Planner | Công cụ mô phỏng tài chính "
    "phục vụ mục đích học tập và tham khảo."
)
