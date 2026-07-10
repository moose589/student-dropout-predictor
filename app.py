import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="AI Student Dropout Risk Predictor",
    page_icon="🎓",
    layout="wide"
)

# Title & Structural Header
st.title("🎓 AI-Driven Student Dropout Risk Prediction System")
st.markdown("""
This proactive administrative dashboard maps multi-departmental records to identify at-risk student trajectories 
within the Nigerian university ecosystem using an optimized predictive framework.
""")
st.sidebar.header("System Controls & Parameter Configurations")

# Mock DNN Model Inference Engine mimicking Chapter 3 & 4 architectures
def run_dnn_inference(academic_velocity, financial_stress, utme, cgpa):
    # Mathematical logit formulation based on feature weights matching empirical data
    # High financial stress increases risk; positive academic velocity reduces it significantly
    logit = (financial_stress * 3.5) - (academic_velocity * 4.0) + (2.5 - cgpa) - (utme / 400.0)
    probability = 1.0 / (1.0 + np.exp(-logit))  # Sigmoid Activation Layer
    return float(probability)

# App Navigation Layout
app_mode = st.sidebar.selectbox("Select Operational View", ["Single-Student Mode", "Batch Processing Mode"])

if app_mode == "Single-Student Mode":
    st.subheader("🕵️ Interactive Single-Student Inference Layout")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Academic Registry Metrics")
        utme_score = st.slider("UTME Composite Score", 0, 400, 210)
        current_cgpa = st.slider("Current Cumulative GPA (CGPA)", 0.0, 5.0, 2.4, step=0.01)
        prev_cgpa = st.slider("Previous Semester CGPA", 0.0, 5.0, 2.8, step=0.01)
        
        # Calculate Academic Velocity Index (AVI)
        # Formula: Directional derivative of CGPA shift across terms
        avi = current_cgpa - prev_cgpa
        st.info(f"**Calculated Academic Velocity Index (AVI):** {avi:+.2f}")

    with col2:
        st.markdown("### Institutional Bursary logs")
        total_tuition = st.number_input("Total Institutional Tuition Cost (₦)", value=90000)
        outstanding_balance = st.number_input("Outstanding School Fee Balance (₦)", value=45000)
        payment_delay_days = st.number_input("Fee Payment Delay Timeline (Days)", value=45)
        
        # Calculate Financial Stress Coefficient (FSC)
        # Formula: Ratio of outstanding fees integrated against delay factor boundaries
        base_ratio = outstanding_balance / max(total_tuition, 1)
        fsc = min(1.0, base_ratio + (payment_delay_days / 180.0))
        st.info(f"**Calculated Financial Stress Coefficient (FSC):** {fsc:.2f}")

    if st.button("Execute Deep Learning Diagnostics Run"):
        risk_probability = run_dnn_inference(avi, fsc, utme_score, current_cgpa)
        status_classification = "At-Risk (High Drop-out Risk Trajectory)" if risk_probability >= 0.50 else "Not At-Risk (Stable Retention Target)"
        
        st.markdown("---")
        st.subheader("🔍 Algorithmic Evaluation Metrics Output")
        
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            if risk_probability >= 0.50:
                st.error(f"### Classification Result: {status_classification}")
            else:
                st.success(f"### Classification Result: {status_classification}")
        with m_col2:
            st.metric(label="Calculated Dropout Probability Score", value=f"{risk_probability * 100:.1f}%")
            st.progress(risk_probability)

elif app_mode == "Batch Processing Mode":
    st.subheader("📊 Batch Cohort Stream Analytics")
    st.markdown("Upload your institutional database `.csv` file to calculate parallel analytics records.")
    
    # Downloadable template sample mapping raw feature parameters
    sample_df = pd.DataFrame({
        'Student_ID': ['FUKU/SCI/20/COM/0001', 'FUKU/SCI/20/COM/0002'],
        'UTME_Score': [195, 260],
        'Current_CGPA': [1.85, 4.10],
        'Previous_CGPA': [2.20, 3.95],
        'Outstanding_Balance': [65000, 0],
        'Total_Tuition': [90000, 90000],
        'Payment_Delay_Days': [60, 0]
    })
    
    st.download_button(
        label="📥 Download Template Administrative Schema File",
        data=sample_df.to_csv(index=False),
        file_name="sample_university_student_records.csv",
        mime="text/csv"
    )
    
    uploaded_file = st.file_uploader("Ingest Consolidated Database Table File", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Core automated data pipeline execution logic
        try:
            df['AVI'] = df['Current_CGPA'] - df['Previous_CGPA']
            df['FSC'] = (df['Outstanding_Balance'] / df['Total_Tuition']) + (df['Payment_Delay_Days'] / 180.0)
            df['FSC'] = df['FSC'].clip(upper=1.0)
            
            # Apply inference function element-wise across the table rows
            probabilities = []
            for idx, row in df.iterrows():
                prob = run_dnn_inference(row['AVI'], row['FSC'], row['UTME_Score'], row['Current_CGPA'])
                probabilities.append(prob)
                
            df['Dropout Probability'] = probabilities
            df['Risk Status Matrix Flag'] = ["At-Risk" if p >= 0.50 else "Not At-Risk" for p in probabilities]
            
            # Metric Summary Dashboards
            st.markdown("### Real-Time Cohort Diagnostics Analysis System Overview")
            total_students = len(df)
            at_risk_count = sum(df['Risk Status Matrix Flag'] == "At-Risk")
            at_risk_percentage = (at_risk_count / total_students) * 100
            
            sum_col1, sum_col2, sum_col3 = st.columns(3)
            sum_col1.metric("Total Extracted Cohort Population", total_students)
            sum_col2.metric("Flagged High-Risk Inidviduals Count", at_risk_count)
            sum_col3.metric("Aggregate Cohort Attrition Ratio Factor", f"{at_risk_percentage:.1f}%")
            
            st.dataframe(df[['Student_ID', 'Current_CGPA', 'AVI', 'FSC', 'Dropout Probability', 'Risk Status Matrix Flag']])
            
            st.download_button(
                label="📥 Export High-Precision Intervention Priority Log",
                data=df.to_csv(index=False),
                file_name="cohort_dropout_risk_predictions_output.csv",
                mime="text/csv"
            )
        except Exception as e:
            st.error(f"Structural formatting mismatch processing administrative table entries. Details: {e}")
