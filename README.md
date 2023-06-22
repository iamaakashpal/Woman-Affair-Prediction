
**`Application Url`** **:** https://woman-affair-prediction.up.railway.app/

# Woman Affair Prediction
This repository contains the code and dataset for predicting the likelihood of a woman having an affair. The prediction is based on various factors such as Women Occupation, Husband Occupation, Rate Marriage, Women Age, Number of Years Marride, Number of Children, religious, and Education. The project aims to provide insights into the factors that contribute to extramarital affairs among women.

# Dataset
The dataset I chose is the affairs dataset that comes with Statsmodels. It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs. More information about the study is available in a 1978 paper from the Journal of Political Economy.

**`Description of Dataset :`**

The dataset contains 6366 observations of 9 variables:

**`rate_marriage`** **:** woman's rating of her marriage (1 = very poor, 5 = very good)

**`age`** **:** woman's age

**`yrs_married`** **:** number of years married

**`children`** **:** number of children

**`religious`** **:**  woman's rating of how religious she is (1 = not religious, 4 =strongly religious)

**`educ`** **:**  level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school,20 = advanced degree)

**`occupation`** **:**  woman's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)

**`occupation_husb`** **:**  husband's occupation (same coding as above)

**`affairs`** **:** time spent in extra-marital affairs

# Code
The code for the affair prediction model is implemented in Python and is available in the [**`Women_Affair_Prediction.ipynb`**](https://github.com/iamaakashpal/Woman-Affair-Prediction/blob/main/Women_Affair_Prediction.ipynb) Jupyter Notebook. The notebook provides step-by-step instructions for data preprocessing, model training, and evaluation.

The following dependencies are required to run the code in this repository:

```
Flask
gunicorn
Jinja2
Werkzeug
numpy
pandas
scipy
scikit-learn
matplotlib
```

# Usage
To use this code and dataset, follow these steps
    
#### 1. Clone the repository **:**
        
```
git clone https://github.com/iamaakashpal/Woman-Affair-Prediction.git
```
#### 2. Navigate to the project directory **:**

```
cd Woman-Affair-Prediction
```

####  3. Install the required dependencies **:**

```
pip install -r requirements.txt
```

#### 4. Open the affair_prediction.ipynb Jupyter Notebook **:**

```
jupyter notebook Women_Affair_Prediction.ipynb
```

#### 5. Run app.py file **:**

```
python app.py
```
# Results

The prediction model achieves an accuracy of approximately **`67%`** in classifying whether a woman is likely to have an affair. The evaluation metrics and additional insights can be found in the notebook.

**`Best Model`** **:** **`Logistic Regression`**

**`Training Score`** **:** **`68%`**

**`Test Score`** **:** **`67%`**

**`classification_report`** **:**

|           | **`precision`**| **`recall`**| **`f1-score`** |**`support`**|
| --------  | -------  |     - | --- |-|
| **`0.0`** |  **`0.69`** | **`0.87`** | **`0.77`** |**`971`**|
| **`1.0`** | **`0.65`** | **`0.39`** | **`0.49`** |**`628`**|
|           |       |               | |ㅤ |
|  **`accuracy`** |  |              |**`0.68`**   |**`1599`**|
| **`macro avg`** | **`0.67`** | **`0.63`**   | **`0.63`**  |**`1599`**|
| **`weighted avg`** | **`0.67`** | **`0.68`** |  **`0.66`** |**`1599`**|


# Output

![Output Screenshot](https://raw.githubusercontent.com/iamaakashpal/Woman-Affair-Prediction/main/img/1.png)

![Output Screenshot](https://raw.githubusercontent.com/iamaakashpal/Woman-Affair-Prediction/main/img/2.png)

![Output Screenshot](https://raw.githubusercontent.com/iamaakashpal/Woman-Affair-Prediction/main/img/3.png)

# Contributing

If you want to contribute to this project, you can:

- Create an issue to discuss potential improvements or report bugs.
- Fork the repository, make your changes, and submit a pull request.

# License
The code and dataset in this repository are available under the MIT License. Feel free to use, modify, and distribute them as per the terms of the license.
