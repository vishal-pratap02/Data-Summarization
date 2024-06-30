from flask import Flask, render_template, url_for
from flask import request as req
import requests



app = Flask(__name__)



# max_l = 60               #56 - 82




@app.route("/")
def first_page():
    return render_template("index.html")



@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    if req.method == "POST":

        API_TOKEN = "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"

        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        data = req.form["data"]
        word_list=data.split()
        input_words=len(word_list)

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            # "parameters": {"max_length": max_l}
        })

        summary = output[0]['summary_text']

        output_word_list=summary.split()
        output_words=len(output_word_list)

        return render_template('index.html', result=summary, data=data, input_words=input_words, output_words=output_words)

    else:
        return render_template('index.html')




if  __name__ == "__main__":
     app.run(debug=True)

