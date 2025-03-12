from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
from datetime import datetime, time

# Initialize Flask application
app = Flask(__name__)


# Load dataset with health provider information
health_provider_info = pd.read_csv("datasets/Doctors_and_Diseases.csv")

# Load pre-trained SVM classifier from a serialized file
svc = pickle.load(open("models/svc.pkl", 'rb'))

#==================================================
# Symptoms Dictionary and DiseaseList Dictionary
#==================================================#

symptom_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 117, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_ofurine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic_patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131, 'prognosis': 132}
disease_list_dict = {0: '(vertigo) Paroymsal Positional Vertigo',1: 'AIDS',2: 'Acne',3: 'Alcoholic hepatitis',4: 'Allergy',5: 'Arthritis',6: 'Bronchial Asthma',7: 'Cervical spondylosis',8: 'Chicken pox',9: 'Chronic cholestasis',10: 'Common Cold', 11: 'Dengue',12: 'Diabetes',13: 'Dimorphic hemmorhoids(piles)', 14: 'Drug Reaction', 15: 'Fungal infection', 16: 'GERD',17: 'Gastroenteritis',18: 'Heart attack',19: 'Hepatitis B',20: 'Hepatitis C',21: 'Hepatitis D',22: 'Hepatitis E',23: 'Hypertension',24: 'Hyperthyroidism',25: 'Hypoglycemia',26: 'Hypothyroidism', 27: 'Impetigo', 28: 'Jaundice',29: 'Malaria',  30: 'Migraine',  31: 'Osteoarthristis',  32: 'Paralysis (brain hemorrhage)',  33: 'Peptic ulcer diseae',  34: 'Pneumonia', 35: 'Psoriasis',  36: 'Tuberculosis',  37: 'Typhoid', 38: 'Urinary tract infection',  39: 'Varicose veins',  40: 'hepatitis A'}


#======= model prediction function =======
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptom_dict))

    for item in patient_symptoms:
        input_vector[symptom_dict[item]]=1
    return disease_list_dict[svc.predict([input_vector])[0]]

#======= creating  Route  for Index Page =======
@app.route('/')
def index():
    symptoms_list = list(symptom_dict.keys())  # Get all symptoms as a list
    return render_template('index.html', symptoms_list=symptoms_list)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        symptoms = request.form.get('symptoms')
        specified_time = request.form.get('time')
        city_state = request.form.get('city_state', '').strip()  # Get combined city and state

        # Split and strip each symptom entered by the user
        user_symptoms = [sym.strip() for sym in symptoms.split(',')]

        # Check if all entered symptoms are known
        invalid_symptoms = [sym for sym in user_symptoms if sym not in symptom_dict]

        # If there are any invalid symptoms, return to the page with an error message
        if invalid_symptoms:
            error_message = f"Unrecognized symptoms provided: {', '.join(invalid_symptoms)}. Please correct your input."
            return render_template('index.html', error=error_message)

        # Proceed if all symptoms are valid
        predicted_disease = get_predicted_value(user_symptoms)  # Assuming this function is defined elsewhere

        available_doctors = []
        if specified_time:
            # Parse the specified time as a datetime.time object
            specified_time_obj = datetime.strptime(specified_time, "%H:%M").time()

            # Filter and process available doctors
            def is_time_within_slots(time_slots_str, check_time):
                slots = time_slots_str.split(',')
                for slot in slots:
                    start_time, end_time = [datetime.strptime(t.strip(), "%H:%M").time() for t in slot.split('-')]
                    if start_time <= check_time < end_time:
                        return True
                return False

            available_doctors = health_provider_info[
                (health_provider_info['Disease'] == predicted_disease) &
                (health_provider_info['Available Time Slots'].apply(
                    lambda x: is_time_within_slots(x, specified_time_obj)))
            ]
        else:
            # Get all doctors for the predicted disease
            available_doctors = health_provider_info[
                health_provider_info['Disease'] == predicted_disease
            ]

        if city_state:
            parts = city_state.split(',')
            specified_city = parts[0].strip() if len(parts) > 0 else ''
            specified_state = parts[1].strip() if len(parts) > 1 else ''

            # Filter by city and state if provided
            if specified_city:
                available_doctors = available_doctors[
                    available_doctors['City'].str.lower() == specified_city.lower()]
            if specified_state:
                available_doctors = available_doctors[
                    available_doctors['State'].str.lower() == specified_state.lower()]

        # sort doctors with respect to available ratings
        available_doctors = available_doctors.sort_values(by='User Rating', ascending=False)
        available_doctors = available_doctors[['Doctor Name', 'City', 'State', 'Available Time Slots', 'User Rating','Hospital']].to_dict(orient='records')


        # ... [rest of the code remains unchanged] ...
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return render_template('partials/prediction_results.html', predicted_disease=predicted_disease,
                                   health_providers=available_doctors)
        else:
            return render_template('index.html', predicted_disease=predicted_disease,
                                   health_providers=available_doctors)

        return render_template('index.html')



# ===============main python============ #
if __name__ == "__main__":
    app.run(debug=True)

