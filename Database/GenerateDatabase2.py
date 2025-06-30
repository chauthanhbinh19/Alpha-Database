import json
import os
import random
import math
#Generate chest

def create_chest_equipment():
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
                        if "Amnitus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(1) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(2) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(3) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(334) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(374) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Angelis_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(4) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(5) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(6) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(335) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(375) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Bellion_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(7) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(8) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(9) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(336) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(376) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Benzamin_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(10) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(11) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(12) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(337) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(377) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Celestial_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(13) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(14) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(15) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(338) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(378) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Ceverus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(16) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(17) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(18) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(339) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(379) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Delius_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(19) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(20) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(21) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(340) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(380) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Domitius_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(22) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(23) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(24) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(341) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(381) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Etherium_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(25) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(26) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(27) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(342) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(382) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Everlyn_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(28) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(29) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(30) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(343) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(383) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "EvilFruit_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(31) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(32) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(33) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(344) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(384) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Extra_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(34) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(35) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(36) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(345) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(385) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Faltus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(37) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(38) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(39) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(346) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(386) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Fealan_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(40) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(41) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(42) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(347) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(387) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Gamma_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(43) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(44) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(45) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(348) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(388) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Gem_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(46) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(47) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(48) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(349) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(389) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Hagoro_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(49) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(50) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(51) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(350) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(390) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Hakalite_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(52) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(53) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(54) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(351) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(391) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Heatherus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(55) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(56) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(57) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(352) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(392) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Ignis_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(58) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(59) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(60) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(353) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(393) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Ivitus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(61) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(62) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(63) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(354) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(394) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Karis_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(64) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(65) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(66) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(355) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(395) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Karmus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(67) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(68) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(69) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(356) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(396) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Lotus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(70) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(71) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(72) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(357) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(397) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Luminius_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(73) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(74) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(75) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(358) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(398) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Macus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(76) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(77) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(78) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(359) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(399) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Morganis_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(79) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(80) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(81) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(360) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(400) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Nimigazin_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(82) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(83) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(84) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(361) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(401) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Omonitus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(85) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(86) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(87) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(362) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(402) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Pet_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(88) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(89) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(90) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(363) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(403) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Qiyantus_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(91) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(92) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(93) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(364) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(404) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Rainbow_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(94) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(95) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(96) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(365) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(405) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Redvenger_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(97) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(98) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(99) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(366) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(406) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Retanic_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(100) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(101) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(102) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(367) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(407) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Souls_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(103) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(104) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(105) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(368) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(408) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Support_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(106) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(107) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(108) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(369) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(409) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Syncroharon_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(109) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(110) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(111) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(370) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(410) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Uni_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(112) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(113) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(114) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(371) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(411) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Zodiac_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(115) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(116) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(117) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(372) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(412) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        elif "Zpower_Equipment" in current_name:
                            with open('chest.txt', 'a') as file:
                                file.write("insert into chest_equipment values (" + str(118) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(119) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(120) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(373) + "," + str(id) + "," + str(1) + ");\n")
                                file.write("insert into chest_equipment values (" + str(413) + "," + str(id) + "," + str(1) + ");\n")
                            id += 1
                        
def create_chest_card():
    cards_dir="Card_Hero"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                if "Adamas" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(283) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(284) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Avian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(285) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(286) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Barbarian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(287) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(288) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Cylloran" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(289) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(290) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Dreizen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(291) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(292) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Etrigon" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(293) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(294) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Firimir" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(295) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(296) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Gennesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(297) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(298) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Hecarus" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(299) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(300) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Illonima" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(301) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(302) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Jaguar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(303) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(304) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Kryptonian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(305) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(306) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Lamania" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(307) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(308) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Marverick" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(309) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(310) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Nemesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(311) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(312) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Onyx" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(313) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(314) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Palladian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(315) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(316) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Quasar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(317) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(318) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Riverven" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(319) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(320) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Starroian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(321) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(322) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Terac" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(323) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(324) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Urius" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(325) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(326) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Vril" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(327) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(328) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Wyvern" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(329) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(330) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Xanthera" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(331) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Yornath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(332) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Zerath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(333) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1             
            if "SSR" in dir_name:
                if "Adamas" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(283) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(284) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Avian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(285) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(286) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Barbarian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(287) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(288) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Cylloran" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(289) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(290) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Dreizen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(291) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(292) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Etrigon" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(293) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(294) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Firimir" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(295) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(296) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Gennesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(297) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(298) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Hecarus" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(299) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(300) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Illonima" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(301) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(302) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Jaguar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(303) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(304) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Kryptonian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(305) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(306) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Lamania" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(307) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(308) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Marverick" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(309) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(310) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Nemesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(311) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(312) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Onyx" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(313) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(314) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Palladian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(315) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(316) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Quasar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(317) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(318) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Riverven" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(319) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(320) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Starroian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(321) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(322) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Terac" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(323) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(324) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Urius" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(325) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(326) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Vril" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(327) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(328) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Wyvern" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(329) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(330) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Xanthera" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(331) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Yornath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(332) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Zerath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(333) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1             
            if "UR" in dir_name:
                if "Adamas" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(283) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(284) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Avian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(285) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(286) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Barbarian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(287) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(288) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Cylloran" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(289) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(290) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Dreizen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(291) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(292) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Etrigon" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(293) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(294) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Firimir" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(295) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(296) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Gennesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(297) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(298) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Hecarus" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(299) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(300) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Illonima" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(301) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(302) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Jaguar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(303) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(304) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Kryptonian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(305) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(306) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Lamania" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(307) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(308) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Marverick" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(309) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(310) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Nemesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(311) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(312) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Onyx" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(313) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(314) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Palladian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(315) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(316) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Quasar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(317) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(318) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Riverven" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(319) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(320) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Starroian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(321) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(322) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Terac" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(323) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(324) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Urius" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(325) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(326) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Vril" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(327) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(328) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Wyvern" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(329) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(330) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Xanthera" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(331) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Yornath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(332) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Zerath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(333) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1             
            if "LG" in dir_name:
                if "Adamas" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(283) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(284) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Avian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(285) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(286) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Barbarian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(287) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(288) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Cylloran" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(289) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(290) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Dreizen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(291) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(292) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Etrigon" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(293) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(294) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Firimir" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(295) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(296) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Gennesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(297) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(298) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Hecarus" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(299) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(300) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Illonima" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(301) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(302) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Jaguar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(303) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(304) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Kryptonian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(305) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(306) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Lamania" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(307) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(308) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Marverick" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(309) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(310) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Nemesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(311) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(312) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Onyx" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(313) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(314) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Palladian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(315) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(316) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Quasar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(317) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(318) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Riverven" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(319) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(320) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Starroian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(321) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(322) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Terac" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(323) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(324) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Urius" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(325) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(326) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Vril" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(327) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(328) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Wyvern" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(329) + "," + str(id) + "," + str(1) + ");\n")
                            file.write("insert into chest_card_hero values (" + str(330) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Xanthera" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(331) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Yornath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(332) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
                elif "Zerath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_hero values (" + str(333) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1             

def create_chest_book():
    cards_dir="Book"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "ArtKnight_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(121) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(122) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(123) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "ETC_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(124) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(125) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(126) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Gemini_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(127) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(128) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(129) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Genshin_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(130) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(131) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(132) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Iterious_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(133) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(134) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(135) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Manhatan_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(136) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(137) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(138) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Monster_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(139) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(140) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(141) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "NA_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(142) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(143) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(144) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "OP_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(145) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(146) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(147) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Othellonia_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(148) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(149) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(150) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "SAO_book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(151) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(152) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(153) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Tanhagan_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(154) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(155) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(156) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Tensei_shitara_Slime_Datta_Ken_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(157) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(158) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(159) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Touhou_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(160) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(161) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(162) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Xenoraphine_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_book values (" + str(163) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(164) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_book values (" + str(165) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1

def create_chest_captain():
    cards_dir="Card_Captain"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_card_captain values (" + str(166) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_captain values (" + str(167) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_captain values (" + str(168) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_captain values (" + str(169) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_colonel():
    cards_dir="Card_Colonel"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_card_colonel values (" + str(170) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_colonel values (" + str(171) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_colonel values (" + str(172) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_colonel values (" + str(173) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_general():
    cards_dir="Card_General"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_card_general values (" + str(174) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_general values (" + str(175) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_general values (" + str(176) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_general values (" + str(177) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_admiral():
    cards_dir="Card_Admiral"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_card_admiral values (" + str(178) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_admiral values (" + str(179) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_admiral values (" + str(180) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_admiral values (" + str(181) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_border():
    cards_dir="Border"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_border values (" + str(182) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_avatar():
    cards_dir="Avatar"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_avatar values (" + str(232) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_collaboration():
    cards_dir="Collaboration"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_collaboration values (" + str(183) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_currency():
    cards_dir="Currency"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_currency values (" + str(184) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_currency values (" + str(185) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_currency values (" + str(186) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_medal():
    cards_dir="Medal"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_medal values (" + str(187) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_medal values (" + str(188) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_medal values (" + str(189) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_monster():
    cards_dir="Card_Monster"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_card_monster values (" + str(190) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_monster values (" + str(191) + "," + str(id) + "," + str(1) + ");\n")
                    file.write("insert into chest_card_monster values (" + str(192) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_pet():
    cards_dir="Pet"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Legendary_Dragon" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_pet values (" + str(193) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(194) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(195) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Mysthic_Monster" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_pet values (" + str(196) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(197) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(198) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Naruto_Bijuu" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_pet values (" + str(199) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(200) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(201) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Naruto_Susanoo" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_pet values (" + str(202) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(203) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(204) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "One_Piece_Ship" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_pet values (" + str(205) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(206) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(207) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Prime_Monster" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_pet values (" + str(208) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(209) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(210) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Ultimate_Monster" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_pet values (" + str(211) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(212) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(213) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Xeras_Monster" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_pet values (" + str(214) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(215) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_pet values (" + str(216) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1

def create_chest_symbol():
    cards_dir="Symbol"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Legendary_Symbol" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_symbol values (" + str(217) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(218) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(219) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Miracle_Symbol" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_symbol values (" + str(220) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(221) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(222) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Mythic_Symbol" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_symbol values (" + str(223) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(224) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(225) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Prime_Symbol" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_symbol values (" + str(226) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(227) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(228) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "World_Symbol" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_symbol values (" + str(229) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(230) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_symbol values (" + str(231) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            
def create_chest_title():
    cards_dir="Title"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_title values (" + str(233) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1

def create_chest_collaboration_equipment():
    cards_dir="CollborationEquipment"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Berus_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(235) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(236) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(237) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Chibi_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(238) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(239) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(240) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "DragonBall_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(241) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(242) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(243) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Drasma_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(244) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(245) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(246) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "ETC_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(247) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(248) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(249) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Hirai_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(250) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(251) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(252) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Ikarus_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(253) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(254) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(255) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Kaisen_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(256) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(257) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(258) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Light_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(259) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(260) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(261) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Naruto_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(262) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(263) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(264) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Neko_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(265) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(266) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(267) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "OnePiece_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(268) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(269) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(270) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Rainbow_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(271) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(272) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(273) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Spirit_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(274) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(275) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(276) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Void_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(277) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(278) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(279) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Xeras_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_collaboration_equipment values (" + str(280) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(281) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_collaboration_equipment values (" + str(282) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1

def create_chest_military():
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
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_military values (" + str(401) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_military values (" + str(401) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_military values (" + str(401) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_military values (" + str(401) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1

def create_chest_spell():
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
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_spell values (" + str(383) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_spell values (" + str(383) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_spell values (" + str(383) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        with open('chest.txt', 'a') as file:
                            file.write("insert into chest_card_spell values (" + str(383) + "," + str(id) + "," + str(1) + ");\n")
                        id=id+1

def create_chest_relics():
    cards_dir="Relics"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Arm" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(217) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(218) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(219) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Blood" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(220) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(221) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(222) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Bone" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(223) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(224) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(225) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Brain" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(226) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(227) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(228) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Eyes" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(229) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(230) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(231) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Heart" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(217) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(218) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(219) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Leg" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(220) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(221) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(222) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Lung" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(223) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(224) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(225) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Nail" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(226) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(227) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(228) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Spirits" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(229) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(230) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(231) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Stomach" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(217) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(218) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(219) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Torso" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_relic values (" + str(220) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(221) + "," + str(id) + "," + str(1) + ");\n")
                        file.write("insert into chest_relic values (" + str(222) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1

def create_chest_magic_formation_circle():
    cards_dir="MagicFormationCircle"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Attack" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_magic_formation_circle values (" + str(217) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Defence" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_magic_formation_circle values (" + str(218) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Support" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_magic_formation_circle values (" + str(219) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1

def create_chest_talisman():
    cards_dir="Talisman"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Attack" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_talisman values (" + str(220) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Defence" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_talisman values (" + str(221) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Support" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_talisman values (" + str(222) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1

def create_chest_puppet():
    cards_dir="Puppet"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Attack" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_puppet values (" + str(223) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Defence" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_puppet values (" + str(224) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Support" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_puppet values (" + str(225) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1

def create_chest_alchemy():
    cards_dir="Alchemy"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Attack" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_alchemy values (" + str(226) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Defence" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_alchemy values (" + str(227) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Support" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_alchemy values (" + str(228) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1

def create_chest_forge():
    cards_dir="Forge"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Attack" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_forge values (" + str(229) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Defence" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_forge values (" + str(230) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1
            elif "Support" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    with open('chest.txt', 'a') as file:
                        file.write("insert into chest_forge values (" + str(231) + "," + str(id) + "," + str(1) + ");\n")
                    id=id+1

def create_chest_card_life():
    cards_dir="Forge"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                with open('chest.txt', 'a') as file:
                    file.write("insert into chest_card_life values (" + str(234) + "," + str(id) + "," + str(1) + ");\n")
                id=id+1


create_chest_equipment()
create_chest_card()
create_chest_captain()
create_chest_colonel()
create_chest_general()
create_chest_admiral()
create_chest_border()
create_chest_avatar()
create_chest_collaboration()
create_chest_currency()
create_chest_medal()
create_chest_monster()
create_chest_pet()
create_chest_symbol()
create_chest_title()
create_chest_collaboration_equipment()
create_chest_military()
create_chest_spell()
create_chest_relics()
create_chest_magic_formation_circle()
create_chest_talisman()
create_chest_puppet()
create_chest_alchemy()
create_chest_forge()
create_chest_card_life()
create_chest_book()