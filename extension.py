def extension_extractor(file_name):
   
    file_extension=file_name.split('.')[-1].lower()
    return file_extension
    
def main():
    file_name=input("enter file name with extension: ")
    file_extension=extension_extractor(file_name)
    
    if len(file_extension)>0 : 
        match file_extension:
            case "gif" |"jpeg"|"jpg"|"png"|"pdf"|"txt"|"zip" : 
                print(f"image/{file_extension}")
            case _: print("application/octet-stream")
         
    else : print("application/octet-stream")

main()