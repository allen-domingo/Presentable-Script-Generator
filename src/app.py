import os
import re
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
       idea = request.form["idea"]
       category = request.form["category"]
       trait1 = request.form["trait1"]
       trait2 = request.form["trait2"]
       messages1=[
            {"role": "system", "content": f"You are a personable, entertaining {category} YouTube script writer with millions of subscribers. You specialize in creating fluid video essay outlines, section by section, based on an outline. Being {trait1} is priority #1,  details is #2, being {trait2} is #3.When you generate outlines, you return them in the format:[Section: Section Name] (include the brackets) \n - Bullet points . Your scripts flow in a natural, compounding, orderly fashion. Prioritize personality and content in place of filler and wordiness.Transitions between sections are natural; not abrupt, distinct, or repetitive."},
            {"role": "user", "content": generate_prompt(idea)}
            ],
       print(trait1,trait2)
       
           # prompt=generate_prompt(idea),
           
           
     #   response = openai.ChatCompletion.create(
     #        model="gpt-3.5-turbo",
     #       # prompt=generate_prompt(idea),
     #        max_tokens=1000,
     #        messages=[
     #        {"role": "system", "content": f"You are a personable, entertaining {category} YouTube script writer with millions of subscribers. You specialize in creating fluid video essay outlines, section by section, based on an outline. Being {trait1} is priority #1,  details is #2, being {trait2} is #3.When you generate outlines, you return them in the format:[Section Name] (include the brackets) \n - Bullet points . Your scripts flow in a natural, compounding, orderly fashion. Prioritize personality and content in place of filler and wordiness.Transitions between sections are natural; not abrupt, distinct, or repetitive."},
     #        {"role": "user", "content": generate_prompt(idea)}
     #        ],
     #        temperature=1.0,
     #        )
          #   messages=[
          #   {"role": "system", "content": f"You are a personable, entertaining {category} YouTube script writer with millions of subscribers. You specialize in creating fluid video essays, section by section, based on an outline. Being {trait1} is priority #1, being {trait2} is #2 Your scripts flow in a natural, compounding, orderly fashion. Prioritize personality and content in place of filler and wordiness.Transitions between sections are natural; not abrupt, distinct, or repetitive."},
          #   {"role": "user", "content": generate_prompt(idea)},
          #   {"role": "assistant","content": response.choices[0].message["content"]},
          #   {"role": "user","content": "Create a long essay based on the outline, going into great detail"}
          #   ],
          #   temperature=1.0,
     
       
     # Note: you need to be using OpenAI Python v0.27.0 for the code below to worlk
     #   print(generate_prompt(idea))
       response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
           # prompt=generate_prompt(idea),
            max_tokens=1000,
            messages = [
            {"role": "system", "content": f"You are a personable, entertaining {category} YouTube script writer with millions of subscribers. You specialize in creating fluid video essay outlines, section by section, based on an outline. Being {trait1} is priority #1,  details is #2, being {trait2} is #3.When you generate outlines, you return them into introduction, sections, and conclusion (include the brackets) \n - Bullet points . Your scripts flow in a natural, compounding, orderly fashion. Prioritize personality and content in place of filler and wordiness.Transitions between sections are natural; not abrupt, distinct, or repetitive."},
            {"role": "user", "content": generate_prompt(idea)}
            ],
            temperature=1.0,
            )
       with open('outline.txt','w') as f:
           f.write(response.choices[0].message["content"])
       print("request 1")
     #   messages1.append({"role": "assistant", "content": response.choices[0].message["content"]})
       with open('outline.txt') as f:
               lines = f.readlines()
       intro = [x for i,x in enumerate(lines) if x.find('Introduction') != -1]
       data = [x for i,x in enumerate(lines) if x.find('Section') != -1]
       conclu = [x for i,x in enumerate(lines) if x.find('Conclusion') != -1]
       index = []
       script = []
       for i in intro:
               intro = lines.index(i)
       for i in data:
               l = lines.index(i)
               index.append(l)
       for i in conclu:
               conclu = lines.index(i)


       for script_generate in range(len(lines)):
               if script_generate == intro:
                   user_input = "Write me an accessible, detailed 3 paragraph introduction, with each paragraph having a minimum of 3 sentences, centered around a bold, attention-grabbing hook, without specific dates, from a personable YouTuber based on 1) something relevant many people might not know about the topic and on 2) the following outline:" + ' '.join(lines[(intro+1):(index[0]-1)])
                   # user_input = "write introduction"
                   print(user_input)
               elif script_generate == "/n":
                   continue
               elif index.count(script_generate):
              
                   if script_generate == index[-1]:
                       endpoint = conclu
                   else:
                       endpoint = index[index.index(script_generate)+1]
                  
                   user_input = "Write me an intriguing, detailed 5 paragraph section, with each paragraph having a minimum of 3 sentences, from a personable YouTuber, flowing naturally from the previous sections, based on the following outline:" + ' '.join(lines[script_generate+1:endpoint-1])
                   print(user_input)
               elif script_generate == conclu:
                   user_input = "Write me an intriguing, detailed 5 paragraph section, with each paragraph having a minimum of 3 sentences, from a personable YouTuber, flowing naturally from the previous sections, based on the following outline:" + ' '.join(lines[conclu+1:len(lines)])
                   print(user_input)
                   # first_request = False
               else:
                   continue

     #   text = response.choices[0].message["content"]
     #   print(text)
     #   sep_list = re.findall("\[(.*?)\]",text)
       
     #   i=0
     #   while i < len(sep_list):
     #       print(sep_list[i])
     #       i +=1
     #       print(i)
               # messages1.append({"role": "user","content": user_input})
               response3 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
           # prompt=generate_prompt(idea),
           
            max_tokens=2000,
            
            messages=[
            {"role": "system", "content": f"You are a personable, entertaining {category} YouTube script writer with millions of subscribers. You specialize in creating fluid video essay outlines, section by section, based on an outline. Being {trait1} is priority #1,  details is #2, being {trait2} is #3.When you generate outlines, you return them in the format:[Section Name] (include the brackets) \n - Bullet points . Your scripts flow in a natural, compounding, orderly fashion. Prioritize personality and content in place of filler and wordiness.Transitions between sections are natural; not abrupt, distinct, or repetitive."},
            {"role": "user", "content": generate_prompt(idea)},
            {"role": "assistant", "content": response.choices[0].message["content"]},
            {"role": "user","content": user_input},
            ],
            temperature=1.0,
       )
               script.extend(response3.choices[0].message["content"])
               print(response3)
     #   messages1.append({"role": "assistant", "content": response})
       final = ""
       with open('script.txt','w') as f:
           for i in script:
             final = final + i
             f.write(i)
             

          #    
           
     #   response2 = openai.ChatCompletion.create(
     #        model="gpt-3.5-turbo",
     #       # prompt=generate_prompt(idea),
           
     #        max_tokens=2000,
            
     #        messages=[
     #        {"role": "system", "content": f"You are a personable, entertaining {category} YouTube script writer with millions of subscribers. You specialize in creating fluid video essays, section by section, based on an outline. Being {trait1} is priority #1, being {trait2} is #2 Your scripts flow in a natural, compounding, orderly fashion. Prioritize personality and content in place of filler and wordiness.Transitions between sections are natural; not abrupt, distinct, or repetitive."},
     #        {"role": "user", "content": generate_prompt(idea)},
     #        {"role": "assistant","content": response.choices[0].message["content"]},
     #        {"role": "user","content": "Create a long essay based on the outline, going into great detail"}
     #        ],
     #        temperature=1.0,
     #   )
       return redirect(url_for("index", result=final))
    #print("TESTTESTTESTTESTTESTTESTTESTTEST")
    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(idea1):
    return f"Create a youtube video essay outline based on {idea1}"
    
