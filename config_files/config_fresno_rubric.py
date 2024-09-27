APP_TITLE = "My First App"
APP_INTRO = """This is a template for an AI-powered Microapp that transforms complex AI prompts into intuitive, user-friendly and _shareable_ applications. The application works like a form that anyone can fill out to get consistent results. 
"""

APP_HOW_IT_WORKS = """
AI-Powered Microapps work by simplifying the creation of consistent and customized outputs from complex AI prompts. Here’s how they operate:

**1. Define the Inputs:** Begin by selecting the important user-defined variables within your AI prompt. These become the input fields in your microapp.

**2. Construct the Prompt(s):** Define the prompts with placeholders for the inputs that will come from the form. Additional internal prompts can be added, for example for scoring. Finally, prompts can be conditional so they are only sent if certain conditions are met. 

**3. User completes the form:** The microapp presents these fields as a form, and the prompt(s) is/are dynamically generated as the form is filled out. This form is designed for ease of use, allowing anyone to input the necessary details without needing to remember or interact with the AI’s underlying complexities.

**4. Deliver Consistent Results:** Once the form is completed, the microapp generates the AI’s response based on the assembled prompt. This process ensures consistent and reliable outputs, regardless of who uses the microapp. The results can then be used directly, shared, or further customized as needed.

**Benefits:**

- Ease of Use: AI-Powered Microapps make advanced AI accessible by converting complex prompts into simple forms.
- Customization: Each microapp is built to suit your specific requirements, ensuring personalized AI interactions.
- Shareability: Microapps can be easily shared across teams, organizations, or communities, providing everyone with consistent, high-quality AI outputs.
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = ""

PHASES = {
    "phase1": {
        "name": "course_details",
        "fields": {
            "course_name": {
                "type": "text_input",
                "label": "What is the name of your course?",
            },
            "course_about": {
                "type": "text_area",
                "label": "What is your course about? Enter as little or as much text as you want.",
            },
            "audience": {
                "type": "selectbox",
                "label": "Who is your intended audience?",
 			            "options": ["Middle School", "Highschool", "University"]
            }
        },
        "phase_instructions": "",
        "user_prompt": "I am building a course {course_name} for {audience} students. I will share details about the course below. Please generate a detailed outline for this course with four modules, learning objectives, a list of suggested content tagged to learning objectives, and ideas for online assessments. My course is about: {course_about}",
        "show_prompt": True,
    }
}


PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only
