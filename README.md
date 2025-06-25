# 💳 Online Payments Fraud Detection Using Machine Learning

This project leverages machine learning techniques to detect fraudulent online transactions in real-time, ensuring secure and trustworthy digital payment systems.

---

## 🔗 Public Resources

- 📁 **Dataset:** [Kaggle - Online Payments Fraud Detection](https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset)
- 📦 **Trained Model (.pkl):** [Download from Google Drive](https://drive.google.com/file/d/1H8E4WCL9HfKQqOffDv2hpnWE14ayAHGR/view?usp=sharing)
- 🔗 **GitHub Repository:** [Aryzenshi/payments-fraud-detection](https://github.com/Aryzenshi/payments-fraud-detection)
- 🎥 **Video Demo:** [Video Demo](https://youtu.be/FaD7YC9v8G0)

---

## 📌 Project Summary

With the rise of digital payments, online fraud has become a major concern. This project uses real-world transaction data and state-of-the-art machine learning models to detect and prevent fraudulent activities. The final model is deployed using Flask and integrated into a simple, interactive web interface.

> 🔍 **Selected Model**: Extra Trees Classifier (ETC) with 99.97% accuracy

---

## 🧠 Tech Stack

- **ML Models**: Extra Trees, Random Forest, Decision Tree, SVC, XGBoost
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Libraries**: Scikit-learn, Pandas, NumPy, Seaborn, Matplotlib

---

## 🚀 How to Run the Web App Locally

### 📦 Step 1: Clone the Repository

```bash
git clone https://github.com/Aryzenshi/payments-fraud-detection.git
cd payments-fraud-detection
```

### 🧰 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### 📁 Step 3: Prepare Files

- Ensure the trained model file `payments.pkl` is present in the root directory.
- Place the dataset in a `data/` folder if needed for testing or retraining.

---

## ▶️ Flask App Tutorial

### How to Run the Flask App in VS Code

1. Open VS Code and navigate to the project folder containing `app.py`
2. Activate your virtual environment (if using one)
3. Open the Terminal (`Ctrl + ~`)
4. Run the following command:

```bash
python app.py
```

5. You should see:

```
Running on http://127.0.0.1:5000/
```

6. Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

7. Fill in the form, click Predict, and the model will return a prediction on a new page.

## 👥 Meet the Team

| 👤 Name            | 🧑‍💻 Role   | 🆔 ID     |
| ------------------ | --------- | --------- |
| ⭐ Aaryav Rastogi  | Team Lead | 23BCE0083 |
| 👩‍💻 Vansika Jain    | Member    | 23BCE0100 |
| 👨‍💻 Rakshit Garg    | Member    | 23BCE0790 |
| 👨‍💻 Divyansh Sharma | Member    | 23BCE0054 |

---

## 📄 License

This project is for academic and educational use.
© 2025 Aaryav Rastogi and Team. All rights reserved.
[MIT LICENSE](LICENSE)
