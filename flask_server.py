from flask import Flask, request, jsonify
from Animalchannel import build_system_prompt, generate_story

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "online"})

@app.route("/submit", methods=["POST"])
def submit():
    try:
        answers = request.json
        prompt = build_system_prompt(answers)
        scenes = generate_story(prompt)
        print("=== GENERATED SCENES ===")
        for i, scene in enumerate(scenes, 1):
            print(f"{i}. {scene}")
        return jsonify({"status": "ok"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run()
