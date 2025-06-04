import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
import base64
from theme import set_theme





def load_combined_data():
    return pd.read_csv("data/REGIONS.csv")



def run():
    set_theme()
    st.markdown("<h1 style='text-align: center;'>🌏 REGIONAL ANALYSIS</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
    # Load Data
    df = load_combined_data()
    
    cluster_map = {
    "Cluster 1": ["Muscat", "North_sharqiyah", "South_sharqiyah"],
    "Cluster 2": ["North_bathinah", "Dhahirah", "Musandam"],
    "Cluster 3": ["Dakhliyah", "South_bathinah", "Al_wusta"],
    "All Clusters": ["Muscat", "North_sharqiyah", "South_sharqiyah",
                         "North_bathinah", "Dhahirah", "Musandam",
                         "Dakhliyah", "South_bathinah", "Al_wusta"]
    }


    # Better horizontal layout using 4 columns
    col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
    
    # Month selector
    months = ["All Months"] + df["Month"].unique().tolist()
    selected_month = col1.selectbox("📅", months, label_visibility="collapsed")
    
    # Cluster checkboxes inline
    cluster_labels = list(cluster_map.keys())[:-1]  # Exclude "All Clusters"
    col_check1, col_check2, col_check3 = col4.columns(3)
    checkbox_columns = [col_check1, col_check2, col_check3]
    
    selected_clusters = []
    for i, cluster in enumerate(cluster_labels):
        if checkbox_columns[i%3].checkbox(cluster, value=True):
            selected_clusters.append(cluster)

    
    # Combine selected regions
    selected_regions = []
    for cluster in selected_clusters:
        selected_regions.extend(cluster_map[cluster])
    
    # Fallback if none selected
    if not selected_clusters:
        selected_regions = cluster_map["All Clusters"]
    
    # Apply filters
    if selected_month != "All Months":
        df = df[df["Month"] == selected_month]
    df = df[df["REGION"].isin(selected_regions)]


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



    # Visualizations
    custom_colors = ["#74c69d", "#52b788", "#40916c", "#1b4332", "#95d5b2", "#d8f3dc"]
    custom_color=["#081C15", "#1B4332", "#2D6A4F", "#40916C", "#52B788", "#74C69D", "#95D5B2", "#B7E4C7"]
    fig1 = px.bar(df, x="REGION", y="DIRECT SAVINGS", color="Month", title="DIRECT SAVINGS", color_discrete_sequence=custom_color, height=300)
    fig1.update_layout(
        title=dict(
    text="DIRECT SAVINGS",
    x=0.5,           # Center the title horizontally
    xanchor='center' # Anchor the title at the center
    ),
    paper_bgcolor='white',
    plot_bgcolor='rgba(183,204,194,0)',
        font=dict(color="black", family='Segoe UI', size=14),
        hoverlabel=dict(
    font_size=13,
    font_family="Segoe UI",
    bgcolor="#32483D",
    font_color="white"), title_font=dict(color='black'), # Title font color
    legend=dict(font=dict(color='black'), bgcolor='rgba(0,0,0,0)'), xaxis=dict(
        tickfont=dict(color='black'),
        title_font=dict(color='black'),
        showgrid=False
    ),
    yaxis=dict(
        tickfont=dict(color='black'),
        title_font=dict(color='black'),
        showgrid=False
    )
    )

    

    fig2 = px.pie(df, names="REGION", values="ILLEGAL CONNECTION",title="ILLEGAL CONNECTION", color_discrete_sequence=custom_color, hole=0.4, height=300, width=500)
    
    fig2.update_layout(   title=dict(
        text="ILLEGAL CONNECTION",
        x=0.5,
        xanchor='center'
    ),margin=dict(l=0, r=0, t=60, b=30),
    paper_bgcolor='white',  # optional same background style
    plot_bgcolor='rgba(183,204,194,0)',     # optional
    font=dict(color="black"),title_font=dict(color='black'),hoverlabel=dict(
        font_size=13,
        font_family="Segoe UI",
        bgcolor="#32483D",
        font_color="white"),
    legend=dict( orientation="h",
        yanchor="bottom",
        y=-1.9,
        xanchor="center",
        x=0.5,font=dict(color='black'), bgcolor='rgba(0,0,0,0)'),
    )
    
    total_surveyed = df["METER SURVEYED"].sum()

    fig3 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=total_surveyed,
       
        gauge={'axis': {'range': [0, df["METER SURVEYED"].max()*6]},'bar': {'color': '#74c69d'},  # Change this color to match theme
        'bgcolor': "rgba(255,255,255,0.05)",
        'borderwidth': 2,
        'bordercolor': "#1b4332"}
    ))
    
    fig3.update_layout( title=dict(text="Total Meters Surveyed",x=0.5,xanchor='center'),
                       title_font=dict(color='black'),
    paper_bgcolor='white',
    font=dict(color="black"),margin=dict(l=120, r=120, t=40, b=0),height=300)
    
    total_meters = {
    "Mechanical": df["MECHANICAL METER"].sum(),
    "Smart": df["SMART METER"].sum()
    }
    
    fig4 = px.pie(names=list(total_meters.keys()),
                   values=list(total_meters.values()),title='ss',
                    hole=0.4, height=300, color_discrete_sequence=["#40916C", "#1B4332"])
    fig4.update_layout(title=dict(text="Overall Meter Type Composition",x=0.5,xanchor='center'),
                       title_font=dict(color='black'),
    paper_bgcolor='white', hoverlabel=dict(
    font_size=13,
    font_family="Segoe UI",
    bgcolor="#32483D",
    font_color="white"),
    font=dict(color="black"),legend=dict( orientation="h",
        yanchor="bottom",
        y=-0.5,
        xanchor="center",
        x=0.5,font=dict(color='black'), bgcolor='rgba(0,0,0,0)')
    )

    
    # Layout: Left for stat boxes, Right for charts
    left_col, right_col = st.columns([1, 6])  # Adjust width ratio as needed
    
    with left_col:
        
        st.markdown(
            f"""
            <div style="background-color: #1B4332; max-width: 170px; height: 40px; 
            border-radius: 20px; box-shadow: 1px 1px 6px rgba(0.3,0.3,0.3,0.3); 
            display: flex; align-items: center; justify-content: center; 
            text-align: center; margin-bottom: 3px; margin-left: 13px; padding-top: 2px; padding-left: 25px;">
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
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Galfar: 83</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Global: 35</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Al Tayer: 12</h5>
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
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Galfar: 12</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Global: 6</h5>
                <h5 style="margin-bottom:0px; font-family: 'Arial', serif; white-space: nowrap; color:white; font-size: 14px"> Al Tayer: 12</h5>
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
        row1_col1, row1_col2 = st.columns(2)
        row1_col1.plotly_chart(fig1, use_container_width=True)
        row1_col2.plotly_chart(fig2, use_container_width=True)
    
        row2_col1, row2_col2 = st.columns(2)
        row2_col1.plotly_chart(fig3, use_container_width=True)
        row2_col2.plotly_chart(fig4, use_container_width=True)

  


if __name__ == "__main__":
    run()
