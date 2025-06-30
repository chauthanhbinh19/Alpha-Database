import json
import os
import random
import math
#Generate Trading

def create_cards_trade():
    cards_dir="Card_Hero"
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_hero_trade values (" + str(id) + "," + str(1) + "," + str(200) + ");\n")

                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_hero_trade values (" + str(id) + "," + str(5) + "," + str(500) + ");\n")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name,extension=os.path.splitext(file_name)
                        
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_hero_trade values (" + str(id) + "," + str(9) + "," + str(1000) + ");\n")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_hero_trade values (" + str(id) + "," + str(13) + "," + str(2000) + ");\n")
                        id=id+1

def create_book_trade():
    cards_dir="Book"
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                
                    with open('test.txt', 'a') as file:
                        file.write("insert into book_trade values (" + str(id) + "," + str(14) + "," + str(2000) + ");\n")
                    id=id+1

def create_captain_trade():
    cards_dir="Card_Captain"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into card_captain_trade values (" + str(id) + "," + str(15) + "," + str(2000) + ");\n")
                    id=id+1

def create_colonel_trade():
    cards_dir="Card_Colonel"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into card_colonel_trade values (" + str(id) + "," + str(12) + "," + str(2000) + ");\n")
                    id=id+1

def create_general_trade():
    cards_dir="Card_General"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into card_general_trade values (" + str(id) + "," + str(16) + "," + str(2000) + ");\n")
                    id=id+1

def create_admiral_trade():
    cards_dir="Card_Admiral"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into card_admiral_trade values (" + str(id) + "," + str(17) + "," + str(2000) + ");\n")
                    id=id+1

def create_skills_trade():
    cards_dir="Skill"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into skill_trade values (" + str(id) + "," + str(45) + "," + str(2000) + ");\n")
                    id=id+1

def create_collaboration_equipments_trade():
    cards_dir="CollborationEquipment"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["MR","LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        
                        with open('test.txt', 'a') as file:
                            file.write("insert into collaboration_equipment_trade values (" + str(id) + "," + str(2) + "," + str(200) + ");\n")

                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        
                        with open('test.txt', 'a') as file:
                            file.write("insert into collaboration_equipment_trade values (" + str(id) + "," + str(6) + "," + str(500) + ");\n")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name,extension=os.path.splitext(file_name)
                        with open('test.txt', 'a') as file:
                            file.write("insert into collaboration_equipment_trade values (" + str(id) + "," + str(10) + "," + str(1000) + ");\n")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        with open('test.txt', 'a') as file:
                            file.write("insert into collaboration_equipment_trade values (" + str(id) + "," + str(14) + "," + str(2000) + ");\n")
                        id=id+1
            if "MR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        with open('test.txt', 'a') as file:
                            file.write("insert into collaboration_equipment_trade values (" + str(id) + "," + str(61) + "," + str(5000) + ");\n")
                        id=id+1

def create_pets_trade():
    cards_dir="Pet"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into pet_trade values (" + str(id) + "," + str(16) + "," + str(5000) + ");\n")

                    id=id+1

def create_symbols_trade():
    cards_dir="Symbol"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into symbol_trade values (" + str(id) + "," + str(18) + "," + str(2000) + ");\n")

                    id=id+1

def create_medals_trade():
    cards_dir="Medal"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
                
                with open('test.txt', 'a') as file:
                    file.write("insert into medal_trade values (" + str(id) + "," + str(19) + "," + str(2000) + ");\n")

                id=id+1

def create_achievements_trade():
    cards_dir="Achievement"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
                
                with open('test.txt', 'a') as file:
                    file.write("insert into achievement_trade values (" + str(id) + "," + str(20) + "," + str(2000) + ");\n")
                id=id+1

def create_titles_trade():
    cards_dir="Title"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")

                with open('test.txt', 'a') as file:
                    file.write("insert into title_trade values (" + str(id) + "," + str(25) + "," + str(2000) + ");\n")
                id=id+1

def create_borders_trade():
    cards_dir="Border"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                with open('test.txt', 'a') as file:
                    file.write("insert into border_trade values (" + str(id) + "," + str(41) + "," + str(2000) + ");\n")
                id=id+1

def create_avatars_trade():
    cards_dir="Avatar"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                with open('test.txt', 'a') as file:
                    file.write("insert into avatar_trade values (" + str(id) + "," + str(41) + "," + str(2000) + ");\n")
                id=id+1

def create_items_trade():
    cards_dir="Item"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    with open('test.txt', 'a') as file:
                        file.write("insert into item_trade values (" + str(id) + "," + str(43) + "," + str(10) + ");\n")
                    id=id+1

def create_equipments_trade():
    cards_dir="Equipment"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir = os.path.basename(root)
        current_name=""
        current_name = os.path.basename(os.path.dirname(root))
        for dir_name in dirs:
            current_dir = os.path.join(root, dir_name)
            for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith(".png"):
                        name, extension = os.path.splitext(file_name)
                        set1_folder_name = os.path.basename(os.path.dirname(current_dir))
                        name=name.replace("_"," ")
                        if "SR" in dir_name:
                            with open('test.txt', 'a') as file:
                                file.write("insert into equipment_trade values (" + str(id) + "," + str(3) + "," + str(200) + ");\n")
                            id += 1
                        elif "SSR" in dir_name:
                            with open('test.txt', 'a') as file:
                                file.write("insert into equipment_trade values (" + str(id) + "," + str(7) + "," + str(500) + ");\n")
                            id += 1
                        elif "UR" in dir_name:
                            with open('test.txt', 'a') as file:
                                file.write("insert into equipment_trade values (" + str(id) + "," + str(11) + "," + str(1000) + ");\n")
                            id += 1
                        elif "LG" in dir_name:
                            with open('test.txt', 'a') as file:
                                file.write("insert into equipment_trade values (" + str(id) + "," + str(15) + "," + str(2000) + ");\n")
                            id += 1
                        elif "MR" in dir_name:
                            with open('test.txt', 'a') as file:
                                file.write("insert into equipment_trade values (" + str(id) + "," + str(69) + "," + str(5000) + ");\n")
                            id += 1

def create_collaboration_trade():
    cards_dir="Collaboration"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                with open('test.txt', 'a') as file:
                    file.write("insert into collaboration_trade values (" + str(id) + "," + str(46) + "," + str(5000) + ");\n")
                id=id+1     

def create_monster_trade():
    cards_dir="Card_Monster"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into card_monster_trade values (" + str(id) + "," + str(47) + "," + str(2000) + ");\n")
                    id=id+1

def create_military_trade():
    cards_dir="Card_Military"
    id=1
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_military_trade values (" + str(id) + "," + str(4) + "," + str(50000) + ");\n")
                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_military_trade values (" + str(id) + "," + str(8) + "," + str(500000) + ");\n")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_military_trade values (" + str(id) + "," + str(12) + "," + str(5000000) + ");\n")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_military_trade values (" + str(id) + "," + str(16) + "," + str(50000000) + ");\n")
                        id=id+1

def create_spell_trade():
    cards_dir="Card_Spell"
    id=1
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_spell_trade values (" + str(id) + "," + str(48) + "," + str(50000) + ");\n")
                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_spell_trade values (" + str(id) + "," + str(48) + "," + str(500000) + ");\n")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_spell_trade values (" + str(id) + "," + str(48) + "," + str(5000000) + ");\n")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('test.txt', 'a') as file:
                            file.write("insert into card_spell_trade values (" + str(id) + "," + str(48) + "," + str(50000000) + ");\n")
                        id=id+1

def create_relics_trade():
    cards_dir="Relics"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into relic_trade values (" + str(id) + "," + str(18) + "," + str(2000) + ");\n")

                    id=id+1

def create_magic_formation_circle_trade():
    cards_dir="MagicFormationCircle"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into magic_formation_circle_trade values (" + str(id) + "," + str(18) + "," + str(2000) + ");\n")

                    id=id+1

def create_talisman_trade():
    cards_dir="Talisman"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into talisman_trade values (" + str(id) + "," + str(18) + "," + str(2000) + ");\n")

                    id=id+1
                
def create_puppet_trade():
    cards_dir="Puppet"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into puppet_trade values (" + str(id) + "," + str(18) + "," + str(2000) + ");\n")

                    id=id+1

def create_alchemy_trade():
    cards_dir="Alchemy"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into alchemy_trade values (" + str(id) + "," + str(18) + "," + str(2000) + ");\n")

                    id=id+1

def create_forge_trade():
    cards_dir="Forge"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into forge_trade values (" + str(id) + "," + str(18) + "," + str(2000) + ");\n")

                    id=id+1

def create_card_life_trade():
    cards_dir="Card_Life"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    with open('test.txt', 'a') as file:
                        file.write("insert into card_life_trade values (" + str(id) + "," + str(18) + "," + str(2000) + ");\n")

                    id=id+1


#Chest book error

create_cards_trade()
create_book_trade()
create_captain_trade()
create_colonel_trade()
create_general_trade()
create_admiral_trade()
create_skills_trade()
create_collaboration_equipments_trade()
create_pets_trade()
create_symbols_trade()
create_medals_trade()
create_achievements_trade()
create_titles_trade()
create_borders_trade()
create_avatars_trade()
create_items_trade()
create_equipments_trade()
create_collaboration_trade()
create_monster_trade()
create_military_trade()
create_spell_trade()
create_relics_trade()
create_magic_formation_circle_trade()
create_talisman_trade()
create_puppet_trade()
create_alchemy_trade()
create_forge_trade()
create_card_life_trade()