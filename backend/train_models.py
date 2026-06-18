import joblib

from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ================= HEART =================

heart = load_breast_cancer()

Xh = heart.data[:, :6]
yh = heart.target

Xh_train, Xh_test, yh_train, yh_test = train_test_split(
    Xh, yh, test_size=0.2, random_state=42
)

heart_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

heart_model.fit(Xh_train, yh_train)

joblib.dump(heart_model, "heart_model.pkl")

print("Heart model trained")


# ================= DIABETES =================

diabetes = load_diabetes()

Xd = diabetes.data
yd = (diabetes.target > 140).astype(int)

Xd_train, Xd_test, yd_train, yd_test = train_test_split(
    Xd, yd, test_size=0.2, random_state=42
)

diabetes_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

diabetes_model.fit(Xd_train, yd_train)

joblib.dump(diabetes_model, "diabetes_model.pkl")

print("Diabetes model trained")


# ================= CANCER =================

cancer = load_breast_cancer()

Xc = cancer.data[:, :10]
yc = cancer.target

Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    Xc, yc, test_size=0.2, random_state=42
)

cancer_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

cancer_model.fit(Xc_train, yc_train)

joblib.dump(cancer_model, "cancer_model.pkl")

print("Cancer model trained")

print("\nAll models trained successfully!")