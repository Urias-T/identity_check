import io
import json
import os
import shutil
from flask import Flask, request, jsonify, make_response

from utils import verify_id

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}


@app.route("/verify", methods=["POST"])
def verify():
    if "image1" not in request.files or "image2" not in request.files:
        return jsonify({"error": "Missing image files!"}), 400
    
    image1 = request.files["image1"]  # Live Image
    image2 = request.files["image2"]  # ID

    name = request.form["name"]

    image1_format = image1.mimetype.split("/")[1]
    image2_format = image2.mimetype.split("/")[1]

    if image1.filename == "" or image2.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if image1_format not in ALLOWED_EXTENSIONS or image2_format not in ALLOWED_EXTENSIONS:
        return jsonify({"error": "Invalid file format"}), 400
    
    try:

        os.mkdir("temp")


        image1.save(f"temp/live_image.{image1_format}")
        image2.save(f"temp/id_image.{image2_format}")


        result = verify_id(image1_format=image1_format, image2_format=image2_format, name=name)

        shutil.rmtree("temp")

        if result == "Verified":
            return jsonify ({"status": "Success",
                            "message": "Verified",
                            "details": {
                                "face_match": True,
                                "name_match": True
                            }
                            }), 200
        
        elif result == "face_mismatch":
            return jsonify({"status": "Failure",
                            "message": "Face Mismatch",
                            "details": {
                                "face_match": False,
                                "name_match": False
                            }
                            }), 401
        
        elif result == "name_mismatch":
            return jsonify({"status": "Failure",
                            "message": "Name Mismatch",
                            "details": {
                                "face_match": True,
                                "name_match": False
                            }
                            }), 401
        
    except Exception as e:
        if os.path.exists("temp"):
            shutil.rmtree("temp")

        return jsonify({"status": "Error",
                        "message": "An error occured",
                        "details": {
                            "error": e
                        }
                        }), 500
    

if (__name__) == "__main__":
    app.run(debug=True, host="0.0.0.0", port=(os.environ.get("PORT", 8080)))

