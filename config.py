APP_TITLE = "Guided Critical Analysis"
APP_INTRO = """In this guided case study, we'll both read the same case study. Then, you'll be guided through an analysis of the paper. Let's begin by reading the paper!

This is a **DEMO**, so sample answers are pre-filled and the article is one that is highly familiar to people.
"""

APP_HOW_IT_WORKS = """
 This is an **AI-Tutored Rubric exercise** that acts as a tutor guiding a student through a shared asset, like an article. It uses the OpenAI Assistants API with GPT-4. The **questions and rubric** are defined by a **faculty**. The **feedback and the score** are generarated by the **AI**. 

It can:

1. provide feedback on a student's answers to questions about an asset
2. roughly "score" a student to determine if they can move on to the next section.  

Scoring is based on a faculty-defined rubric on the backend. These rubrics can be simple (i.e. "full points if the student gives a thoughtful answer") or specific with different criteria and point thresholds. The faculty also defines a minimum pass threshold for each question. The threshold could be as low as zero points to pass any answer, or it could be higher. 

Using AI to provide feedback and score like this is a very experimental process. Some things to note: 

 - AIs make mistakes. Users are encourage to skip a question if the AI is not understanding them or giving good feedback. 
 - The AI might say things that it can't do, like "Ask me anything about the article". I presume further refinement can reduce these kinds of responses. 
 - Scoring is highly experimental. At this point, it should mainly be used to gauge if a user gave an approximately close answer to what the rubric suggests. It is not recommended to show the user the numeric score. 
 - Initial testing indicates that the AI is a very easy grader. This is probably good in this experiment, and it may be refined with different prompting. 
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
    "url":"http://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf",
    "button_text":"Read PDF"
}

PHASES = {
    "phase1": {
        "name": "Introduction",
        "fields": {
            "name": {
                "type": "text_input",
                "label": "What is your name?",
                "value": "Jane Doe"
            },
            "background": {
                "type": "text_area",
                "label": "What do you already know about online education and video engagement?",
                "value": "I have taken a few online courses and noticed that some video lectures are more engaging than others. I think factors like video length and the instructor's speaking style might affect engagement, but I'm not sure about the specifics or if there's research on this topic."
            }
        },
        "phase_instructions": "The user will provide you with their name and background of the study. Greet the user formally and acknowledge the user's background and explain how it relates to the paper we'll be analyzing.",
        "user_prompt": "My name is {name} and here is the {background} of the study",
        "ai_response": False,
        "custom_response": "Welcome {name} and Thanks for providing your background in the study as {background}.",
        "scored_phase": False,
        "allow_revisions": False,
        "allow_skip": True
    },
    "phase2": {
        "name": "Article Overview",
        "fields": {
            "topic": {
                "type": "text_area",
                "label": "What is the main topic of this research paper?",
                "value": "This research paper focuses on the impact of video production decisions on student engagement in online educational videos. It examines how various aspects of video creation affect how students interact with and learn from these videos in online courses."
            },
            "research_question": {
                "type": "text_area",
                "label": "What is the main research question or objective of this study?",
                "value": "The main objective of this study is to identify which factors in video production have the most significant impact on student engagement in online educational videos. Specifically, the researchers aim to understand how elements like video length, speaking rate, production style, and instructor visibility affect how long students watch videos and how they perform on subsequent problem-solving tasks."
            }
        },
        "phase_instructions": "Evaluate the user's understanding of the main topic of the research paper and study's primary goal. Guide them to refine their answer if it's not precise.",
        "user_prompt": "Here is the main topic of the research paper: {topic} and the study's primary goal is: {research_question}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """
            1. Accuracy
                2 points - Correctly identifies the main topic (video engagement in online education)            
                1 point - Partially identifies the topic (mentions either videos or engagement, but not both)
                0 points - Misidentifies the topic or provides an irrelevant answer
            2. Completeness
                2 points - Mentions both the focus on production decisions and their impact on student engagement
                1 point - Mentions either production decisions or student engagement, but not both
                0 points - Does not mention either key aspect of the study
        """,
        "allow_revisions": True,
        "allow_skip": True
    },
    "phase3": {
        "name": "Methodology Analysis",
        "fields": {
            "data_collection": {
                "type": "text_area",
                "label": "How did the researchers collect data for this study?",
                "value": "The researchers collected data from the edX platform, a massive open online course (MOOC) provider. They gathered information from approximately 6.9 million video watching sessions across four courses. The data included details on how long students watched each video and how they performed on problem sets following the videos. This large-scale approach allowed the researchers to analyze a vast amount of real-world data on student engagement with online educational videos."
            },
            "analysis_method": {
                "type": "text_area",
                "label": "What methods did the researchers use to analyze the data?",
                "value": "The researchers used a combination of quantitative and qualitative methods to analyze the data. They performed statistical analyses to correlate various video attributes (such as length, speaking rate, production style, and instructor visibility) with engagement metrics (video watching time and performance on subsequent problems). They also conducted qualitative analyses of video styles and content to categorize videos and understand nuances that might not be captured by quantitative data alone. The researchers used these methods to identify patterns and trends in how different video characteristics influenced student engagement and learning outcomes."
            }
        },
        "phase_instructions": "Assess the user's understanding of the data collection process and analysis methods. Prompt them to think about the scale and sources of data if they miss key points and Encourage them to consider both quantitative and qualitative aspects in analysis methods.",
        "user_prompt": "The data was collected as follows: {data_collection}. The analysis methods used were: {analysis_method}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """
            1. Data Source and Methods
                2 points - Correctly identifies edX as the source of data and analysis methods as Qualitative and Quantitative. 
                1 point - Mentions online courses but not specifically edX and talks about analysis methods in general.
                0 points - Does not mention or incorrectly identifies the data source and does not mention analysis methods
            2. Scale
                1 point - Mentions the large scale of the study (millions of sessions)
                0 points - Does not mention the scale of data collection
        """,
        "allow_revisions": True,
        "allow_skip": True
    },
    "phase4": {
        "name": "Results and Implications",
        "fields": {
            "key_findings": {
                "type": "text_area",
                "label": "What are the most significant findings of this study?",
                "value": "The study revealed several significant findings:\n1. Shorter videos are more engaging. Videos under 6 minutes long had the highest engagement.\n2. Videos that intersperse an instructor's talking head with slides are more engaging than slides alone.\n3. Videos with a more personal feel could be more engaging than high-fidelity studio recordings.\n4. Videos where instructors speak fairly quickly and with high enthusiasm are more engaging.\n5. Khan-style tablet drawings are more engaging than PowerPoint slides or code screencasts.\n6. Even high quality pre-recorded classroom lectures are not as engaging when repurposed for an online course."
            },
            "implications": {
                "type": "text_area",
                "label": "How might these findings impact the creation of online educational videos in the future?",
                "value": "These findings could significantly impact the creation of online educational videos:\n\n1. For educators: Instructors might focus on creating shorter, more focused videos instead of long lectures. They may also adjust their speaking style to be more enthusiastic and slightly faster-paced.\n\n2. For video producers: There might be a shift towards more personal, less polished production styles that emphasize the instructor's presence. This could include more use of tablet drawing techniques and interspersing talking head shots with informational slides.\n\n3. For platform designers: Learning management systems and video hosting platforms might incorporate features that encourage shorter video segments and provide analytics on student engagement based on video characteristics.\n\n4. For students: Learners might benefit from more engaging content, potentially leading to improved learning outcomes and course completion rates.\n\n5. For institutions: Universities and other education providers might need to invest in training for educators on effective online video production techniques, rather than simply repurposing existing lecture recordings.\n\nOverall, these findings could lead to a more standardized approach to creating engaging online educational content, potentially revolutionizing the way online courses are designed and delivered."
            }
        },
        "phase_instructions": "Evaluate the user's grasp of the key findings and implications. If they miss important findings and implications, provide them with hints.",
        "user_prompt": "The key findings of the study are: {key_findings}. The implications for the future of online educational videos are: {implications}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 3,
        "rubric": """
            1. Comprehensiveness
                3 points - Mentions at least three key findings (e.g., impact of video length, speaking rate, production style)
                2 points - Mentions two key findings
                1 point - Mentions one key finding
                0 points - Does not mention any relevant findings
            2. Accuracy
                2 points - All mentioned findings are accurate
                1 point - Some mentioned findings are accurate, some are not
                0 points - No accurate findings mentioned
        """,
        "allow_revisions": True,
        "allow_skip": True
    }
}

selected_llm = "gpt-3.5-turbo"


LLM_CONFIGURATIONS = {
    "gpt-3.5-turbo": {
        "model": "gpt-3.5-turbo-0125",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":0.50,
        "price_output_token_1M":1.50
    },
    "gpt-4-turbo": {
        "model": "gpt-4-turbo",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":10,
        "price_output_token_1M":30
    },
    "gpt-4o": {
        "model": "gpt-4o",
        "frequency_penalty": 0,
        "max_tokens": 250,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":5,
        "price_output_token_1M":15
    },
    "gemini-1.0-pro": {
        "model": "gemini-1.0-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.5,
        "price_output_token_1M":1.5
    },
    "gemini-1.5-flash": {
        "model": "gemini-1.5-flash",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.35,
        "price_output_token_1M":1.05
    },
    "gemini-1.5-pro": {
        "model": "gemini-1.5-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":3.5,
        "price_output_token_1M":10.50
    },
    "claude-opus": {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 15,
        "price_output_token_1M": 75
    },
    "claude-sonnet": {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-haiku": {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 0.25,
        "price_output_token_1M": 1.25
    }
}

SCORING_DEBUG_MODE = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False