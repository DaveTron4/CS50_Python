name_file = input("File name: ")


def extensions_manager(file):
    name_file_mod = file.lower().replace(".", " ")
    image_extensions = ["gif", "jpg", "jpeg", "png"]
    app_extensions = ["pdf", "zip"]
    result = ""

    if "jpg" in name_file_mod:
        result = "image/jpeg"
        print(result)
        return

    for extension in image_extensions:
        if extension in name_file_mod:
            result = f"image/{extension}"
            print(result)
            return
    for extension in app_extensions:
        if extension in name_file_mod:
            result = f"application/{extension}"
            print(result)
            return
        elif "txt" in name_file_mod:
            result = f"text/plain"
            print(result)
            return

    result = "application/octet-stream"
    print(result)
    return

extensions_manager(name_file)