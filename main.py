import os
import shutil
import logging
from flask import Flask, request, jsonify, make_response

from utils import verify_id

app = Flask(__name__)

logging.basicConfig(level=logging.ERROR)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}


@app.route("/verify", methods=["POST"])
def verify():
    if "image1" not in request.files or "image2" not in request.files:
        return jsonify({"error": "Missing image files!"}), 400
    
    live_image = request.files["image1"]  # Live Image
    id_image = request.files["image2"]  # ID

    name = request.form["name"]

    live_image_format = live_image.mimetype.split("/")[1]
    id_image_format = id_image.mimetype.split("/")[1]

    if live_image.filename == "" or id_image.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if live_image_format not in ALLOWED_EXTENSIONS or id_image_format not in ALLOWED_EXTENSIONS:
        return jsonify({"error": "Invalid file format"}), 400
    
    try:

        os.mkdir("temp")


        live_image.save(f"temp/live_image.{live_image_format}")
        id_image.save(f"temp/id_image.{id_image_format}")


        result = verify_id(live_image_format=live_image_format, id_image_format=id_image_format, name=name)

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
                            "message": "Verification failed. Live image does not match ID image.",
                            "details": {
                                "face_match": False,
                                "name_match": False
                            }
                            }), 401
        
        elif result == "name_mismatch":
            return jsonify({"status": "Failure",
                            "message": "Verification failed. Provided name doesn't match that on ID.",
                            "details": {
                                "face_match": True,
                                "name_match": False
                            }
                            }), 401
        
    except Exception as e:
        logging.error(f"{str(e)} error occured.")

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

