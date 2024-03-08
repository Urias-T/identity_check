import easyocr
from deepface import DeepFace


def name_check(image2_format, name):
    
    reader = easyocr.Reader(["en"])
    result = reader.readtext(f"temp/id_image.{image2_format}")

    texts = []

    for item in result:
        text = item[1]
        texts.append(text)

    joined_text = " ".join(texts)
    lower_text = joined_text.lower()

    return name.lower() in lower_text


def compare_faces(image1_format, image2_format):
    
    verification = DeepFace.verify(img1_path=f"temp/live_image.{image1_format}",
                                    img2_path=f"temp/id_image.{image2_format}")
    
    if verification["verified"]:
        return "face_match"

    return "face_mismatch"


def verify_id(image1_format, image2_format, name):

    compare_result = compare_faces(image1_format, image2_format)

    if compare_result == "face_mismatch":
        return compare_result
    
    else:
        name_check_result = name_check(image2_format=image2_format, name=name)

        if name_check_result:
            return "Verified"
        
        else:
            return "name_mismatch"

