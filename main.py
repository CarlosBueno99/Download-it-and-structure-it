import csv
import os
import urllib.request



document_path = "IN\\variations.csv"
pictures_path = "./OUT/"

column_that_has_the_id = "REFERENCIA"
column_that_has_the_name = "PRODUTO"
columns_that_has_the_photos = ["IMAGEM","IMAGEM 1","IMAGEM 2","IMAGEM 3","IMAGEM 4","IMAGEM 5","IMAGEM 6","IMAGEM 7","IMAGEM 8","IMAGEM 9","IMAGEM 10","IMAGEM 11","IMAGEM 12","IMAGEM 13","IMAGEM 14","IMAGEM 15","IMAGEM 16"]


def download_images(image_url, file_name):
    req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})

        
    with open(file_name + ".jpg", "wb") as f:
        with urllib.request.urlopen(req) as r:
            
            f.write(r.read())
            


with open( document_path, encoding="utf-8",newline='') as csvin:
    reader = csv.DictReader(csvin,delimiter=";")
    

    for row in reader:
        
        
        name_of_the_file = row[column_that_has_the_name]
        name_of_the_folder = row[column_that_has_the_id]
        count = 0

        path = pictures_path + name_of_the_folder + "/"

        messsage1 = "Iniciando download de fotos do produto "+name_of_the_file+" com id "+name_of_the_folder 
        print(messsage1.center(int(os.get_terminal_size()[0])))
    
        os.makedirs(path)

        for photo in columns_that_has_the_photos:
            count = count+1
            if row[photo] == '':
                break
            else:
                
                download_images(row[photo],path+name_of_the_file + str(count))
        
        
print("Download Completo".center(int(os.get_terminal_size()[0])))



        