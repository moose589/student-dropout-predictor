# AI-Driven Prediction for Students Drop-Out Risk in Nigeria Universities

An Educational Data Mining (EDM) predictive framework designed to identify at-risk undergraduate trajectories within the Nigerian tertiary education ecosystem using Deep Neural Networks (DNN).

## 🚀 System Architecture Overview
This system integrates multi-departmental administrative records (Registry, Bursary, and Student Affairs) to flag at-risk student trajectories before terminal academic failure occurs.

* **Backend Engine:** Multi-layered Deep Neural Network (DNN) optimizing a Sigmoid activation function.
* **Empirical Validation Accuracy:** 92.7% overall accuracy with an 88.6% Sensitivity (Recall) score.
* **Dynamic Engineered Features:** Academic Velocity Index (AVI) and Financial Stress Coefficient (FSC).

## 📂 Repository Structure
* `app.py`: Streamlit-driven user dashboard tracking interactive single-student and batch cohort inference.
* `requirements.txt`: Environment package dependencies optimized for serverless cloud deployment.

## 🛠️ Local Installation & Deployment
To run this application locally on your computer or mobile environment:

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/student-dropout-predictor.git](https://github.com/YOUR_USERNAME/student-dropout-predictor.git)
pip install -r requirements.txt
streamlit run app.py
## 4. Connecting GitHub to Streamlit Cloud on Mobile

Your project specifies that your repository is linked via automated webhooks to Streamlit Community Cloud for automated container building without system downtime[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span).

1. Open a new tab in your mobile browser and go to **[share.streamlit.io](https://share.streamlit.io)**.
2. Click **Connect with GitHub** and authorize your account.
3. Click the **Create app** (or **Deploy an app**) button.
4. In the setup fields, type your repository name: `YOUR_USERNAME/student-dropout-predictor`.
5. Set the Main file path to: `app.py`.
6. Click **Deploy!**

Streamlit will open a live terminal window showing it loading your `requirements.txt` packages. Within 1–2 minutes, it will give you a permanent public `[https://...streamlit.app](https://...streamlit.app)` URL. You can open this link on your phone, tablet, or presentation laptop during your graduation project defense to demonstrate your app live.

Now that your mobile-friendly architecture and GitHub configurations are

