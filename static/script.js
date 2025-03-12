        const symptom_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 117, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_ofurine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic_patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131, 'prognosis': 132}
        // JavaScript for toggling the navbar
        function toggleNavbar() {
            var navbar = document.querySelector('.navbar');
            navbar.classList.toggle('active');
        }

        // Add event listeners to each navbar link
        document.querySelectorAll('.navbar-links a').forEach(link => {
            link.addEventListener('click', () => {
                var navbar = document.querySelector('.navbar');
                navbar.classList.remove('active');
            });
        });

        const btns = document.querySelectorAll(".nav-btn");
        const slides = document.querySelectorAll(".img-slide");
        const contents = document.querySelectorAll(".content");

        let currentSlide = 0;
        let slideInterval;
        let isPaused = false; // Initialize isPaused

        // Set transition effect for all slides
        slides.forEach((slide) => {
            slide.style.transition = 'opacity 0.3s';
        });

        var sliderNav = function (manual) {
            // Remove active class from all buttons, slides, and contents
            btns.forEach(btn => btn.classList.remove("active"));
            slides.forEach(slide => slide.classList.remove("active"));
            contents.forEach(content => content.classList.remove("active"));

            if (manual !== undefined) {
                currentSlide = manual;
            }

            // Set active class for current slide
            btns[currentSlide].classList.add("active");
            slides[currentSlide].classList.add("active");
            contents[currentSlide].classList.add("active");

            // Set opacity for slides
            slides.forEach((slide, index) => {
                slide.style.opacity = index === currentSlide ? 1 : 0;
            });

            // Move to the next slide for the next interval
            currentSlide = (currentSlide + 1) % slides.length;
        }

        // Function to start the automatic slide change
        const startSlide = () => {
            slideInterval = setInterval(() => {
                if (!isPaused) {
                    sliderNav();
                }
            }, 5000); // Change slide every 5 seconds
        }

        // Add event listeners for pausing and resuming the slideshow on hover
        slides.forEach(slide => {
            slide.addEventListener("mouseover", () => isPaused = true);
            slide.addEventListener("mouseleave", () => isPaused = false);
        });

        // Event listeners for manual navigation
        btns.forEach((btn, i) => {
            btn.addEventListener("click", () => {
                clearInterval(slideInterval);
                sliderNav(i);
                startSlide();
            });
        });

        startSlide(); // Start the slideshow
        const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
        const symptomsInput = document.getElementById('symptoms');  // Get the input field

//        Speech Recognition

    document.addEventListener('DOMContentLoaded', function() {
    const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
    const symptomsInput = document.getElementById('symptoms');

    if ('webkitSpeechRecognition' in window) {
        let recognition = new webkitSpeechRecognition();
        recognition.continuous = false;  // Continuously captures speech until stopped
        recognition.interimResults = false;  // Shows results only after speech ends
        recognition.lang = 'en-US';

        recognition.onstart = function() {
            symptomsInput.placeholder = "Listening...";  // Notify user that mic is on
        };

        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;  // Capture the transcript from the recognition result
            symptomsInput.value = transcript;  // Display the recognized speech in the input box
            console.log('Recognized:', transcript);
        };

        recognition.onerror = function(event) {
            console.error('Speech Recognition Error:', event.error);
            symptomsInput.placeholder = "Error in speech recognition";  // Notify user of the error
        };

        recognition.onend = function() {
            if (symptomsInput.value === "") {
                symptomsInput.placeholder = "No speech detected or recognition ended";  // Reset placeholder if no input was recognized
            }
            console.log('Speech recognition service has stopped.');
        };

        startSpeechRecognitionButton.addEventListener('click', function() {
            symptomsInput.value = '';  // Clear previous input
            recognition.start();  // Start the recognition service
        });
    } else {
        console.log('Speech recognition not supported in this browser.');
    }
});

    document.getElementById("feedbackSelect").addEventListener("change", function() {
        var comments = document.getElementById("comments");
        var submitBtn = document.getElementById("submitBtn");
        var label = document.querySelector('label[for="comments"]');
        if (this.value !== "Please choose an option") {
            comments.style.display = "block";
            submitBtn.style.display = "block";
            label.style.display = "block";
        } else {
            comments.style.display = "none";
            submitBtn.style.display = "none";
            label.style.display = "none";
        }
    });

    document.getElementById("submitBtn").addEventListener("click", function() {
        var feedbackSelect = document.getElementById("feedbackSelect");
        if (feedbackSelect.value !== "Please choose an option") {
            document.querySelector(".success-message").textContent = "Thank you for sharing your thoughts!";
            }
    });



