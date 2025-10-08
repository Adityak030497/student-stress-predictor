🧠 Student Stress Level Predictor

A machine learning web application that predicts student stress levels (0–100) based on multiple lifestyle and academic factors. Built with Random Forest Regressor, integrated into a Streamlit frontend, and powered by Plotly visualizations for clear insights and interactive analysis.

🚩 Overview

Stress among students often stems from academic pressure, lifestyle imbalance, and emotional strain. This project uses machine learning to analyze patterns from various personal and academic features to estimate a student’s stress level and offer well-being recommendations.

⚙️ Tech Stack

Frontend: Streamlit, Plotly

Backend / Model: Python, Scikit-learn, Pandas, NumPy

Model Used: Random Forest Regressor

Version Control: Git, GitHub

Deployment: Streamlit Cloud

🧩 Features

✅ Predicts stress score (0–100) based on inputs like:

Sleep hours

Study time

Screen time

Academic pressure

Peer pressure

Attendance and social activities

✅ Provides personalized suggestions for better stress management.
✅ Includes an interactive Plotly gauge chart to visualize stress level.
✅ Deployed via Streamlit Cloud for easy access and sharing.

📈 Model Performance

Model: Random Forest Regressor

Evaluation Metric: R² Score

R² Score: 0.82

Demonstrates strong accuracy and reliability in predicting stress levels.

🧠 How It Works

The user inputs lifestyle and academic parameters in the Streamlit interface.

The input data is preprocessed and encoded to match model requirements.

The trained model (stress_model.pkl) predicts the stress score.

The result is visualized using a color-coded gauge chart.

The app displays personalized stress management tips.

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/Adityak030497/student-stress-predictor.git
cd student-stress-predictor

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py

🧾 Dataset

The dataset contains anonymized student information, with 13 key features including sleep hours, academic pressure, and physical activity.
Target variable: stress_level (0–100)

📸 Example Output
![Screenshot_8-10-2025_194941_student-stress-predictor-ascplodlljaij6xmsnnpb2 streamlit app](https://github.com/user-attachments/assets/9fdf4c84-fd90-4afd-a522-2d5f67c8ff86)

💡 Future Improvements

Integrate real-time data collection via surveys or forms.

Implement explainability (e.g., SHAP values) to show factor importance.

Add database storage and analytics dashboard.

👨‍💻 Author

Aditya Kumar
