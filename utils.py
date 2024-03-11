import easyocr
from deepface import DeepFace


def name_check(id_image_format: str, name: str) -> bool:
    """function to check if name provided matches that on the id

    Args:
        id_image_format (str): format of the id image
        name (str): name provided

    Returns:
        bool: boolean: Is the name on the id or not?
    """
    
    reader = easyocr.Reader(["en"])
    result = reader.readtext(f"temp/id_image.{id_image_format}")

    texts = []

    for item in result:
        text = item[1]
        texts.append(text)

    joined_text = " ".join(texts)
    lower_text = joined_text.lower()

    return name.lower() in lower_text


def compare_faces(live_image_format: str, id_image_format: str) -> str:
    """function to compare the face on the live image to that on the id image using
    VGG-Face model and cosine similarity.

    Args:
        live_image_format (str): format of the live image
        id_image_format (str): format of the id image

    Returns:
        str: string indicating match or mismatch
    """
    
    verification = DeepFace.verify(img1_path=f"temp/live_image.{live_image_format}",
                                    img2_path=f"temp/id_image.{id_image_format}")
    
    if verification["verified"]:
        return "face_match"

    return "face_mismatch"


def verify_id(live_image_format: str, id_image_format: str, name: str) -> str:
    """function for verifying that the face on an id matches that on a live image
    and that the name provided matches that on the id.

    Args:
        live_image_format (str): format of the live image
        id_image_format (str): format of the id image
        name (str): name provided

    Returns:
        str: string indicating successful verification or a mismatch
    """

    compare_result = compare_faces(live_image_format, id_image_format)

    if compare_result == "face_mismatch":
        return compare_result
    
    else:
        name_check_result = name_check(id_image_format=id_image_format, name=name)

        if name_check_result:
            return "Verified"
        
        else:
            return "name_mismatch"

