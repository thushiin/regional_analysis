import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
import base64
from common_charts import plot_charts
from theme import set_theme



def load_data():
    df = pd.read_csv("data/REGIONS.csv")
    return df[df["REGION"] == "Muscat"]

def run():
    set_theme()
    st.markdown("<h1 style='text-align: center;'>📍 MUSCAT DASHBOARD</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
    df = load_data()


    col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
    # Filter
    months = df["Month"].unique().tolist()
    selected_month = col1.selectbox("📅 Filter by Month", ["All Months"] + months,label_visibility="collapsed")

    if selected_month != "All Months":
        df = df[df["Month"] == selected_month]
        

    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(
            f"""
            <div style="
                background-color: #1B4332; 
                padding: 10px 15px; 
                border-radius: 12px; 
                box-shadow: 1px 10px 6px rgba(0.3,0.3,0.3,0.3); 
                text-align:center; 
                max-width: 250px; 
                margin: auto;">
                <h5 style="margin-bottom:0px; font-family: 'Helvetica', serif; white-space: nowrap; color:white; font-size: 14px"">💰 Total Direct Savings</h5>
                <p style="font-size: 20px; line-height: 1.1; font-family: 'Arial', serif; font-weight: 1000; margin: 0; color:white; text-align: center;">{df['DIRECT SAVINGS'].sum():,}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"""
            <div style="
                background-color: #1B4332; 
                padding: 10px 15px; 
                border-radius: 12px; 
                box-shadow: 1px 10px 6px rgba(0.3,0.3,0.3,0.3); 
                text-align: center; 
                max-width: 250px;
                margin: auto;">
                <h5 style="margin-bottom: 0px; line-height: 1.1; font-family: 'Helvetica', serif; white-space: nowrap; color:white; font-size: 14px">⚠️ Illegal Connections</h5>
                <p style="font-size: 20px; line-height: 1.1; font-family: 'Arial', serif; font-weight: 1000; margin: 0; color:white; text-align: center;">{int(df['ILLEGAL CONNECTION'].sum())}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col3:
        st.markdown(
            f"""
            <div style="
                background-color: #1B4332; 
                padding: 10px 15px; 
                border-radius: 12px; 
                box-shadow: 1px 10px 6px rgba(0.3,0.3,0.3,0.3); 
                text-align: center; 
                max-width: 270px; 
                margin: auto;">
                <h5 style="margin-bottom: 0px; font-family: 'Helvetica', serif; white-space: nowrap; color:white;  font-size: 14px"">📊 Total Meters Surveyed</h5>
                <p style="font-size: 20px; line-height: 1.1; font-family: 'Arial', serif; font-weight: 1000; margin: 0; color:white; text-align: center;">{df['METER SURVEYED'].sum():,}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            f"""
            <div style="
                background-color: #1B4332; 
                padding: 10px 15px; 
                border-radius: 12px; 
                box-shadow: 1px 10px 6px rgba(0.3,0.3,0.3,0.3); 
                text-align: center; 
                max-width: 250px; 
                margin: auto;">
                <h5 style="margin-bottom: 0px; font-family: 'Helvetica', serif; white-space: nowrap; color:white; font-size: 14px"">⚙️ Faulty Meters</h5>
                <p style="font-size: 20px; line-height: 1.1; font-family: 'Arial', serif; font-weight: 1000; margin: 0; color:white; text-align: center;">{df['FAULTY METER'].sum():,}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        
    st.markdown('<div style="margin-top: 10px;"></div>', unsafe_allow_html=True)
    
    left_col, right_col = st.columns([1, 6])  # Adjust width ratio as needed
    
    with left_col:
        
        st.markdown(
            f"""
            <div style="background-color: #1B4332; max-width: 170px; height: 40px; 
            border-radius: 20px; box-shadow: 1px 1px 6px rgba(0.3,0.3,0.3,0.3); 
            display: flex; align-items: center; justify-content: center; 
            text-align: center; margin-bottom: 3px; margin-left: 13px; padding-top: 10px; padding-left: 25px;">
                <h3 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-weight :1000; font-size: 12px">TOTAL TEAMS</h3>
                
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            f"""
            <div style="background-color: #1B4332; max-width: 170px; height: 100px; 
            border-radius: 12px; box-shadow: 1px 10px 6px rgba(0.3,0.3,0.3,0.3); 
            display: flex; align-items: center; justify-content: center; flex-direction: column; 
            text-align: center; margin-bottom: 10px; margin-left: 13px; padding-top: 15px; padding-left: 25px">
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Galfar: 19</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Global: 27</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Al Tayer: 0</h5>
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div style="background-color: #1B4332; max-width: 170px; height: 40px; 
            border-radius: 20px; box-shadow: 1px 1px 6px rgba(0.3,0.3,0.3,0.3); 
            display: flex; align-items: center; justify-content: center; 
            text-align: center; margin-bottom: 3px; margin-left: 13px; padding-top: 15px; padding-left: 25px;">
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-weight :1000; font-size: 10px">TOTAL ENGINEERS</h5>
                
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            f"""
            <div style="background-color: #1B4332; max-width: 170px; height: 100px; 
            border-radius: 12px; box-shadow: 1px 10px 6px rgba(0.3,0.3,0.3,0.3); 
            display: flex; align-items: center; justify-content: center; flex-direction: column; 
            text-align: center; margin-bottom: 10px; margin-left: 13px; padding-top: 15px; padding-left: 25px">
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Galfar: 7</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Global: 4</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Al Tayer: 0</h5>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="background-color: #1B4332; max-width: 170px; height: 40px; 
            border-radius: 20px; box-shadow: 1px 1px 6px rgba(0.3,0.3,0.3,0.3); 
            display: flex; align-items: center; justify-content: center; 
            text-align: center; margin-bottom: 3px; margin-left: 13px; padding-top: 15px; padding-left: 25px">
                <h5 style="margin-bottom:0px; font-family: 'Arial',serif; font-weight :1000; white-space: nowrap; color:white; font-size: 10px">PROJECT MANAGER</h5>
                
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            f"""
            <div style="background-color: #1B4332; max-width: 170px; height: 100px; 
            border-radius: 12px; box-shadow: 1px 10px 6px rgba(0.3,0.3,0.3,0.3); 
            display: flex; align-items: center; justify-content: center; flex-direction: column; 
            text-align: center; margin-bottom: 10px; margin-left: 13px; padding-top: 15px; padding-left: 25px">
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap;  color:white; font-size: 14px"> Galfar: 1</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Global: 1</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Al Tayer: 0</h5>
            </div>
            """,
            unsafe_allow_html=True
        )


        
    
    with right_col:

        # Charts
        plot_charts(df)

# Optional: Direct run (for testing)
if __name__ == "__main__":
    run()