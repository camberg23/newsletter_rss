# from openai import OpenAI
# import streamlit as st
# from langchain_community.chat_models import ChatOpenAI
# from langchain.prompts import PromptTemplate 
# from langchain.chains import LLMChain

# generate_content = """
# Your job is to help provide a human writer with key bullet points that capture personality types in the {MODEL} personality framework for all of the major characters from a given TV show/movie/book/etc based on your knowledge of each type.

# AGAIN, THE SELECTED FRAMEWORK IS: {MODEL}

# (IF AND ONLY IF the selected framework is Myers-Briggs and you plan to label or name any of the types, please use the following names only. Note you don't have to do this, but if you do use the names in addition to the types, use these names: INFP: The Healer, INTJ: The Mastermind, INFJ: The Counselor, INTP: The Architect, ENFP: The Champion, ENTJ: The Commander, ENTP: The Visionary, ENFJ: The Teacher, ISFJ: The Protector, ISFP: The Composer, ISTJ: The Inspector, ISTP: The Craftsperson, ESFJ: The Provider, ESFP: The Performer, ESTJ: The Supervisor, ESTP: The Dynamo)

# Here is the specific character universe for which you should generate the appropriate personality types: {X}

# Your job is to output ALL of the key characters related to the above universe and their type assignment as headers, and the rich justification for and evidence related to assigning that character to that type as bullets below that header.
# SPECIAL NOTE: if the SELECTED FRAMEWORK is Big Five, you cannot do typing in the same way as the other models. Therefore, still output the major characters and attempt to characterize them across all five traits (very low, low, medium, high, very high), using rich evidence for each one.

# It should be as rich information as possible/appropriate for each character, using specific details or actions from the story to justify your type/trait assignment. It is okay to have duplicate types (give the best and most honest type assignment possible), but be mindful at the same time not to output, eg, 10 characters of the same type (this wouldn't make for a great article!). Strike the balance, but prioritize accurately nailing the types.

# Again, a human is going to take your outputs as an outline/reference for writing a polished blog piece, so you don't need to output polished text yourself, just make sure the core ideas and key raw content is there. It does not have to be pretty!

# Formatting requirements: make sure you immediately output the specified content, no preface or conclusion, and make sure it is in Markdown for easy formatting.

# YOUR OUTPUTS:
# """

# st.title('Get character personalities from any movie/TV show')

# # Dropdown for selecting the personality model with no option selected by default
# model_type = st.selectbox(
#     'Choose a Personality Model',
#     ('Select a model', 'DISC', 'Enneagram', 'Myers-Briggs', 'Big Five'),
#     index=0,
#     key='model_type'
# )

# # Text area for defining the task
# task_description = st.text_area('Enter TV show/movie here, with any additional context', placeholder='Gilmore Girls, top 10 characters | all major Harry Potter characters | protagonists from major Disney movies | etc.',
#                                 key='task_description',max_chars=400)

# # Submit button
# if st.button('Submit'):
#     if model_type == 'Select a model':
#         st.error('Please select a personality model.')
#     elif not task_description.strip():
#         st.error('Please define the task.')
#     else:
#         with st.spinner('Generating, standby...'):
#             chat_model = ChatOpenAI(openai_api_key=st.secrets['API_KEY'], model_name='gpt-4-1106-preview', temperature=0.2)
#             chat_chain = LLMChain(prompt=PromptTemplate.from_template(generate_content), llm=chat_model)
#             generated_output = chat_chain.run(MODEL=model_type, X=task_description)
            
#             # Display the LLM output using markdown
#             st.write(generated_output)
            
#             # Use Streamlit's download button to download the output
#             st.download_button(
#                 label="Download Output",
#                 data=generated_output,
#                 file_name="personality_characters.txt",
#                 mime="text/plain"
#             )

import streamlit as st

# Hardcoded RSS feed string
rss_feed = '''
<title>The Best Nonprofit Careers For Your Personality Type</title>
<link>https://www.truity.com/blog/best-nonprofit-careers-your-personality-type</link>
<description><p>Craving a career that's about more than just a paycheck? Look no further than the nonprofit sector. Here, your passions and principles don't just fuel your work—they become it. And with opportunities ranging from arts and education to public health and social services, there's a gig that fits every personality like a glove. Here are six of the best nonprofit career paths to help with your career planning.</p> 
<img src="https://d31u95r9ywbjex.cloudfront.net/blog/sites/default/files/media/image/2023-10/36268022_m_normal_none.jpg" width="1068" height="712" alt="The Best Nonprofit Careers For Your Personality Type" loading="lazy" class="image-style-blog-full-width" /></description>
<comments>https://www.truity.com/blog/best-nonprofit-careers-your-personality-type#comments</comments>
<enclosure url="https://d31u95r9ywbjex.cloudfront.net/blog/sites/default/files/media/image/2023-10/36268022_m_normal_none.jpg" length="52601" type="image/jpeg"/>
<guid isPermaLink="true">https://www.truity.com/blog/node/1190</guid>
<pubDate>Thu, 31 Aug 2023 06:21:21 -0700</pubDate>
<source url="https://www.truity.com/blog/rss.xml">True You Journal</source>
<dc:creator>Truity</dc:creator>
'''

# Serve the RSS feed as XML
# st.set_option('deprecation.showfileUploaderEncoding', False)
st.markdown(f"```xml\n{rss_feed}\n```")
