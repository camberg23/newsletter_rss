from openai import OpenAI
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain

generate_content = """
Your job is to help provide a human writer with key bullet points about how EACH personality type in the {MODEL} personality framework would/should characteristically do a given thing, based on your knowledge of each type.

Here is the specific content you should generate: {X}

Your output should include EACH of the types that exists in the {MODEL} personality framework, where each type is a header and there is as much information as is appropriate (in bullet form) about how each type would/should characteristically do the relevant thing described above.

It should be as rich information as possible/appropriate for each type.

Again, a human is going to take your outputs as an outline/reference for writing a polished blog piece on how each {MODEL} type does the thing, so you don't need to output polished text yourself, just make sure the core ideas and key raw content is there. It does not have to be pretty!

Formatting requirements: make sure you immediately output the specified content, no preface or conclusion, and make sure it is in markdown for easy formatting.

YOUR OUTPUTS:
"""

st.title('How do you X, by personality type')

# Dropdown for selecting the personality model with no option selected by default
model_type = st.selectbox(
    'Choose a Personality Model',
    ('Select a model', 'DISC', 'Enneagram', 'Myers-Briggs'),
    index=0,
    key='model_type'
)

# Text area for defining the task
task_description = st.text_area('Title/key content', placeholder='examples: How Each Personality Type Deals with Rejection | What Your Bedroom Looks Like, Based on Your Personality Type | Where Your Next Vacation Should Be, Based on Your Enneagram Type',
                                key='task_description',max_chars=200)

# Submit button
if st.button('Submit'):
    if model_type == 'Select a model':
        st.error('Please select a personality model.')
    elif not task_description.strip():
        st.error('Please define the task.')
    else:
        with st.spinner('Generating, standby...'):
            chat_model = ChatOpenAI(openai_api_key=st.secrets['API_KEY'], model_name='gpt-4-1106-preview', temperature=0.2)
            chat_chain = LLMChain(prompt=PromptTemplate.from_template(generate_content), llm=chat_model)
            generated_output = chat_chain.run(MODEL=model_type, X=task_description)
            
            # Display the LLM output using markdown
            st.write(generated_output)
            
            # Use Streamlit's download button to download the output
            st.download_button(
                label="Download Output",
                data=generated_output,
                file_name="personality_insights.txt",
                mime="text/plain"
            )
