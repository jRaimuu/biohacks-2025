import streamlit as st
import random
#function
#dictionaries
mar_dict = {
    "Married":1,
    "Common Law":2,
    "Unmarried (and Not Living Common Law)":3,
    "Separated or Divorced (and Not Living Common Law)":4,
    "Widowed (and Not Living Common Law)":5,
    "Prefer Not To Say":99
}
pop_dict = {
    "Rural area (less than1 ,000)":1,
    "Small population centre (1,000 to 29,999)":2, 
    "Medium population centre (30,000 to 99,999)":3, 
    "Large urban population centre (100,000 or greater)":4
}
age_dict = {
    (15, 19):1,
    (20, 24):2,
    (25, 29):3,
    (30, 34):4,
    (35, 39):5,
    (40, 54):6,
    (55, 64):7,
    (65, 130):8
}
gen_dict = {
    "Man+":1,
    "Woman+":2, 
    "Or please specify,":[1,2]
}
lgbt_dict = {
    True:1,
    False:2
}
imm_dict = {
    "Yes":1,
    "No":2,
    "No Answer":9
}
vism_dict ={
    True:1,
    False:2
}
def convert_all(mar, pop, age, gen, lgbt, imm, vism):
    array = []
    print("\n\n\n\n")
    print(mar, pop, age, gen, lgbt, imm, vism)
    for i in age_dict.keys():
        if age in i:
            age = age_dict[i]
    if gen in gen_dict.keys():
        if gen == "Or please specify,":
            gen = gen_dict["Or please specify,"]
        else:
            gen = gen_dict[gen]
    if None not in [mar, pop, age, gen, lgbt, imm, vism]:
        print(f"mar {mar_dict[mar]} pop {pop_dict[pop]} age {age} gen {gen} lgbt {lgbt_dict[lgbt]} imm {imm_dict[imm]} vism {vism_dict[vism]}")
    return [mar_dict[mar], pop_dict[pop], age, gen, lgbt_dict[lgbt], imm_dict[imm], vism_dict[vism]]


#main
#title
st.title("MindMappers Psychological Disorder Prediction Tool")

#census section
st.header("Let's get to know you... :eyes:")
st.markdown("We'll ask you some questions that you might see on Canada's Mental Health and Access to Health Care Survey in 2032. We'll use our neural network to rank your probability of having each mental health issue. \
             No data is collected because I don't have a webserver to store it...")
st.subheader("Excerpt of Canada's Mental Health and Access to Health Care Survery (MHACS)")
#CENSUS 

#age
age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

#reads sex
st.markdown("""The following questions are about sex at birth and gender. 
Sex refers to sex assigned at birth. Gender refers to 
current gender which may be different from sex assigned 
at birth and may be different from what is indicated on 
legal documents. """)
sex = st.radio(
    "What sex were you at birth?",
    ["Man+", "Woman+", "Prefer Not to Say"],
    index=None
)

#reads gender
gender = st.radio(
    "What gender identity do you have?", gen_dict.keys(),
    index=None
)
#in case gender identity is non-binary
if gender == "Or please specify,":
    gender = st.text_input("If please specify,", "")

sex_ori = st.radio(
    "What is your sexual orientation?",
    ["Heterosexual", "Gay or Lesbian", "Bisexual", "Or please specify,"],
    index=None
)
lgbt = False
#checks if they are lgbt

if sex_ori in ["Gay or Lesbian", "Bisexual", "Or please specify,"] or gender != sex:
    lgbt = True
else:
    lgbt = False
st.write(f"LGBT: {lgbt}")

#visible minority
st.markdown("Are you a member of any of the following visible minorities? Enter all that apply. ")
minority = st.multiselect(
    "I am...",
    ["White", "South Asian", "Chinese", "Black", "Filipino", "Arab", "Latin American", 
    "Southeast Asian", "West Asian", "Korean", "Japanese",  "Other"], help = "Southeast Asian - "
)
visible_minority = True
if any(i in minority for i in ["White", "Arab", "West Asian"]):
    visible_minority = False
else:
    visible_minority = True
st.write(f"Visibile Minority: {visible_minority}")
population = st.radio(
    "What is the population of the location where your primary residence is?",
    pop_dict.keys(),
    index=None
)
marital = st.radio(
    "What is your current marital status?", mar_dict.keys(),
     index=None
)
immigration = st.radio(
    "(A \"landed immigrant\" (permanent resident) \
    is a person who has been granted the right to live in Canada by immigration authorities. \n \
    Are you a landed immigrant?", imm_dict.keys(),
    index=None
)
st.markdown("Once you have completed the survey, press this button to submit your information to the neural network.\
            Let's see what mental disorders you are at risk of!")
if None not in [gender, sex_ori, population, marital, immigration, lgbt, visible_minority]:
    submit = st.button("Submit!", on_click=print(convert_all(marital, population, age, gender, lgbt, immigration, visible_minority)), disabled = False)