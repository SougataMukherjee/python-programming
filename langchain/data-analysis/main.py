import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 Data Analysis with CSV File")

# File uploader
file = st.file_uploader("Upload your CSV file", type=["csv"])

@st.cache_data
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

if file:
    # Load CSV
    df = load_data(file)

    # Show preview
    st.subheader("🔎 Data Preview")
    st.dataframe(df.head())

    

    # City filter
    if "City" in df.columns:
        cities = df["City"].unique()
        selected_city = st.selectbox("Filter by City", cities)
        filtered_data = df[df["City"] == selected_city]

        st.subheader(f"🏙️ Data for {selected_city}")
        st.dataframe(filtered_data)

        # Sales Rate Graph
        if "Sales" in df.columns:
            st.subheader(f"📊 Sales Rate in {selected_city}")
            chart = (
                alt.Chart(filtered_data)
                .mark_bar()
                .encode(
                    x="Product:N",
                    y="Sales:Q",
                    tooltip=["Product", "Sales"]
                )
            )
            st.altair_chart(chart, use_container_width=True)

        #download report
        csv_report = filtered_data.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Report (CSV)",
            data=csv_report,
            file_name=f"{selected_city}_report.csv",
            mime="text/csv",
        )
    else:
        st.warning("⚠️ CSV file must contain a 'City' column.")
