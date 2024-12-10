import gradio as gr
from example1 import chain

def chat(question,history):
    if question == "":
        return "please ask a question"
    else:
        return chain.invoke(question)
    
gr.ChatInterface(
    fn=chat,
    type="messages"
).launch(
    share =True,
)
#---------------------------------
# with gr.Blocks(title="Chat with GPT-4") as demo:
#     gr.Markdown("# Chat with GPT-4 DEMO")
#     with gr.Row():
#         gr.Markdown("")
#         with gr.Column(scale=6):
#             chatbox = gr.Chatbot(type="messages")
#             with gr.Row():
#                 textbox = gr.Textbox(scale=7,container=False,placeholder="Ask Something")
#                 submit_button= gr.Button(
#                     value="Submit",
#                     scale=3,
#                     variant="primary"
#                 )
#     gr.Markdown("")
    
# def chat(question,history):
#     history.append({"role":"user","content":question})
#     if question == '':
#         response = "PLease ask something" 
#         history.append({"role":"assistant","content":response})
#     else:
#         # response = chain.invoke({"question": question})
#             response = chain.stream({"question": question})

#             # response = chain.invoke(question)
#             history.append({"role": "assistant" , "content": ''})
        
#     for i in response:
#         history[-1]['content'] += i
#         yield "", history

    
#     textbox.submit(chat, inputs=[textbox, chatbox], outputs=[textbox,chatbox])
#     submit_button.click(chat, inputs=[textbox, chatbox], outputs=[textbox,chatbox])



# demo.launch(
#     share=True,
# )

#---------------------------------
import gradio as gr
from example1 import chain


with gr.Blocks(title="Chat with GPT-4") as demo:
    with gr.Column():
        chatbox = gr.Chatbot(type="messages")
        textbox = gr.Textbox()
        submit_button = gr.Button(value="Submit")

    def chat(question , history):
        history.append({"role": "user", "content": question})
        if question == '' :
            response =  "Please ask a question"
            history.append({"role": "assistant" , "content": response})
        else:
            # response = chain.invoke({"question": question})
            response = chain.stream({"question": question})

            # response = chain.invoke(question)
            history.append({"role": "assistant" , "content": ''})
        
        for i in response:
            history[-1]['content'] += i
            yield "", history

    
    textbox.submit(chat, inputs=[textbox, chatbox], outputs=[textbox,chatbox])
    submit_button.click(chat, inputs=[textbox, chatbox], outputs=[textbox,chatbox])



demo.launch(
    server_name="0.0.0.0",
    server_port=7860
)