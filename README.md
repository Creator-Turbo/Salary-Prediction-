# Salary Prediction

### Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Run](#run)
- [Deployment on Render](#deployment-on-render)
- [Directory Tree](#directory-tree)
- [To Do](#to-do)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [License](#license)
- [Credits](#credits)

---
## Demo
The Salary Prediction project estimates salaries based on various job-related features using machine learning techniques.<br>
**Link to Demo:** [comming-soon](#) 





![Salary Prediction](https://i.imgur.com/2GsXr6n.jpeg)

---

## Overview
This project helps job seekers, recruiters, and HR professionals understand salary expectations based on experience, job title, location, and other factors.

Key Features:

- Machine Learning-based salary estimation

- Predict salaries based on job-related factors

- Data visualization for insights

- Deployment-ready for real-world applications
---

## Motivation


Understanding salary trends is crucial for job seekers negotiating salaries and recruiters setting competitive pay scales. This model provides insights into salary expectations based on historical data.



---

## Technical Aspect

1️⃣ Data Collection & Preprocessing

- Processed job-related features (experience_level, job_title, company_location, etc.).
- Handled missing values, outliers, and applied one-hot encoding & feature scaling.

2️⃣ Feature Engineering

- Created new features, applied log transformation, and performed feature selection using mutual information & correlation analysis.

3️⃣ Model Selection & Training

- Implemented Linear Regression, Random Forest, XGBoost, and ANN for salary prediction.
- Used GridSearchCV & RandomizedSearchCV for hyperparameter tuning.

4️⃣ Model Evaluation

- Assessed models using MAE, MSE, and R² Score to select the best approach.

5️⃣ Deployment

-  Deployed via Flask/FastAPI with a Streamlit UI.
Hosted on Render / AWS / Hugging Face Spaces (TBD).

---

## Installation
The Code is written in Python 3.10. Install the required packages and libraries by running:

```bash
pip install -r requirements.txt
```

## Run
To run the Flask web app locally:

```bash
python app.py
```

## Deployment on Render

To deploy the Flask web app on Render:
- Push your code to GitHub.
- Log in to Render and create a new web service.
- Connect the GitHub repository.
- Configure environment variables (if any).
- Deploy and access your app live.

## Directory Tree 

```
salary-prediction/  
├── 📂 .github/  
├── 📂 data/  
├── 📂 logs/  
├── 📂 notebook/  
├── 📂 static/  
├── 📂 templates/  
├── 📂 venv/  
├── 📄 .gitignore  
├── 📄 app.py  
├── 📄 LICENSE  
├── 📄 README.md  
├── 📄 requirements.txt  
├── 📄 setup.py  
├── 📄 template.py  
           
```

## To Do

- Improve model performance using hyperparameter tuning.

- Implement a web-based interface for predictions.

- Deploy the model on a cloud platform.


## Bug / Feature Request
If you encounter any bugs or want to request a new feature, please open an issue on GitHub. Contributions are welcome!

## Technologies Used

- Python 3.10 🐍 – Core programming language

- Scikit-learn 📊 – Machine learning library

- Pandas & NumPy 📊 – Data processing and analysis

- Matplotlib & Seaborn 📊 – Data visualization

- Flask / Streamlit 🖥️ – Web framework for deployment

- Render / AWS ☁️ – Deployment (Planned)






![](https://forthebadge.com/images/badges/made-with-python.svg)


[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/260px-Scikit_learn_logo_small.svg.png" width=170>](https://scikit-learn.org/stable/)
[<img target="_blank" src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*RWkQ0Fziw792xa0S" width=170>](https://pandas.pydata.org/docs/)
[<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDzf1RMK1iHKjAswDiqbFB8f3by6mLO89eir-Q4LJioPuq9yOrhvpw2d3Ms1u8NLlzsMQ&usqp=CAU" width=280 height=160>](https://matplotlib.org/stable/index.html)
 [<img target="_blank" src="https://icon2.cleanpng.com/20180829/okc/kisspng-flask-python-web-framework-representational-state-flask-stickker-1713946755581.webp" width=170>](https://flask.palletsprojects.com/en/stable/) 
 [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/doc/) 
 [<img target="_blank" src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" width=200>](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html) 
[<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEc9A_S6BPxCDRp5WjMFEfXrpCu1ya2OO-Lw&s" width=170 height="170">](https://developer.mozilla.org/en-US/docs/Web/HTML) 
[<img target="_blank" src="https://cdn-icons-png.flaticon.com/512/919/919826.png" width=170>](https://developer.mozilla.org/en-US/docs/Web/CSS) 



---

## Team
This project was developed by:
[![Bablu kumar pandey](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](ressume_link) |
-|

**Bablu Kumar Pandey**

- [GitHub](https://github.com/Creator-Turbo)  
- [LinkedIn](https://www.linkedin.com/in/bablu-kumar-pandey-313764286/)
- **Personal Website**: [My Portfolio](https://creator-turbo.github.io/Creator-Turbo-Portfolio-website/)

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software under the terms of the MIT License. For more details, see the [LICENSE](LICENSE) file included in this repository.

## Credits

Special thanks to the contributors and open-source communities for their contributions to AI advancements!

🚀 Your support and innovation drive the future of AI-powered applications!