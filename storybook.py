import os
import streamlit as st 
from openai import OpenAI

# Set the OpenAI API key
my_secret = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=my_secret)


def story_gen(user_prompt):
    system_prompt="""You are a world renowend experience children storyteller. 
    you will be given a concept to generate a story suitable for ages 5-7 years old."""
    

    response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages = [
        {"role": "system","content": 
      system_prompt},
        {"role": "user","content":
      user_prompt}   
    ],
    temperature=1.3,
    max_tokens=200

  )
    return response.choices[0].message.content

def cover_gen(user_prompt):
  system_prompt=""" 
  You will be given a children's storyboard.Generate a prompt for cover arts that is suitable and show off the story themes. 
  the prompt will be sent to dall-e-2"""
  

  response = client.chat.completions.create(
  model='gpt-4o-mini',
  messages = [
    {"role": "system", 
     "content": system_prompt},
    {"role": "user", 
     "content": user_prompt},

],
  temperature=1.3,
  max_tokens=100

)
  return response.choices[0].message.content

#image generator

def image_gen(prompt):
  response= client.images.generate(
      model = "dall-e-2",
      prompt = prompt,
      size = "256x256",
      n = 1,
  )
  return response.data[0].url

#Storybook method
def storybook(user_prompt):
  story = story_gen(user_prompt)
  cover = cover_gen(story)
  image = image_gen(cover)

  st.write(image)
  st.write(story)

st.title("Storybook Generator for kids for fun")
st.divider()

user_prompt = st.text_area("Enter your story concept:")

if st.button("Generate Storybook"):
  with st.spinner("please wait"):
    story = story_gen(user_prompt)
    cover = cover_gen(story)
    image = image_gen(cover)
  
    st.image(image)
    st.write(story)