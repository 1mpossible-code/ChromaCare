# To start

```shell
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
# To run app
flask --app app/main run
```

# About

This is an accessibility project that focuses on analyzing and reviewing user-inputted websites on how accessible they
are for those who are subject to color vision deficiency (CVD) ; also known as color-blindness. In this application,
Python is used to parse a website's front-end code for hex color id's registered in CSS, and then convert them into RGB
tuples.
From this point, the collected RGB values are evaluated in respect to what RGB values are easily
visualized/distinguishable for CVD persons. Through these comparisons a color-blind accessibility grade is given out of
10, and is displayed amongst all the colors listed on the website through ChromaCare's application.

# Hackathon

This is a project made during Hack NYU hackathon!