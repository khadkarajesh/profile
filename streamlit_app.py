import pandas as pd
import streamlit as st

st.markdown("### Software Engineer, Data Scientist")
st.markdown("* [Linkedin](https://www.linkedin.com/in/rajeshkhadka/) \n"
            "* [Github](https://github.com/khadkarajesh) \n"
            "* [Medium](https://medium.com/@rajesh_khadka) \n")

st.markdown("#### Summary")
st.markdown(
    "Software Engineer jumped into Data Science. Spent several years on software development(Backend, Mobile). Mostly worked on startup. Besides coding, you can find me on free mentorship platform (Adplist, MentorColor etc) helping peoples, writing blogs on medium.\n"
    "We can collaborate on followings:")
st.markdown("* Data Extraction, Preprocessing, Feature Engineering")
st.markdown("* ETL, Data Ingestion Pipeline")
st.markdown("* Machine learning model development and Deployment")
st.markdown("* Research and Benchmark of machine learning algorithm")
st.markdown("* Mentorship on Data Science and Machine Learning")
st.markdown("* Consultation on building API services and Mobile Application")
st.markdown("* Recommendation system in ecommerce")
st.markdown("* Open source project collaboration")

st.markdown("#### Technologies")
st.markdown("* Machine Learning: Tensorflow, Scikit-learn, Lightfm, Surprise, Implicit")
st.markdown("* Ml & ETL: Airflow, Mlflow, Evidently")
st.markdown("* Cloud: AWS, AWS-Personalize, S3, SQS, EC2, Lambda")
st.markdown("* Cloud: Firebase, Cloud Function, Realtime Database, Remote Config, Firebase Analytics")
st.markdown("* Database: Postgresql, MySQL, Mongodb, Redis")
st.markdown("* Containerization & Orchestrator: Docker, Kubernetes")
st.markdown("* Framework: Flask, Android, Flutter, Node.js")
st.markdown("* Programming Language: Python, Java, Kotlin, Javascript")

st.markdown("#### Interest")
st.markdown("* Graph Neural Network \n"
            "* Machine Learning \n"
            "* Data Science \n"
            "* Deep Learning \n"
            "* Software Development \n"
            "* Computational Mathematics \n"
            "* Recommender System \n"
            "* Startup")

st.markdown("#### Projects")
projects_df = pd.read_json("projects.json")
for i, row in projects_df.iterrows():
    image_col, container_col = st.columns((1, 2))
    image_container = image_col.container()
    image_container.markdown("\n")
    image_container.image(row['image'])

    container = container_col.container()
    container.markdown(f"##### {row['name']}")
    container.markdown(row['description'])
    container.markdown("###### Technologies")
    container.markdown(row['technologies'])
    container.write(f"[Github]({row['github']}), [Website]({row['website']})")
    st.markdown("------")
