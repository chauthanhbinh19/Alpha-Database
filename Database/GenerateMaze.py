import random

# Danh sách mẫu các giá trị VALUES cho câu lệnh INSERT
sample_values = [
    "('{name}', '{node_id}', 'Health', 'LG', {x}, {y}, 0, 5000000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Physical Attack', 'LG', {x}, {y}, 0, 0, 100000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Physical Defense', 'LG', {x}, {y}, 0, 0, 0, 75000000, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Magical Attack', 'LG', {x}, {y}, 0, 0, 0, 0, 100000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Magical Defense', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 75000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Chemical Attack', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 100000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Chemical Defense', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 75000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Atomic Attack', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 100000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Atomic Defense', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Mental Attack', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Mental Defense', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Speed', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Shield Strength', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Damage To Different Faction Rate', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Resistance To Different Faction Rate', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Damage To Same Faction Rate', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Resistance To Same Faction Rate', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Health', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Physical Attack', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Physical Defense', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Magical Attack', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Magical Defense', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Chemical Attack', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Chemical Defense', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Atomic Attack', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Atomic Defense', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0)",
    "('{name}', '{node_id}', 'Percent All Mental Attack', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0)",
    "('{name}', '{node_id}', 'Percent All Mental Defense', 'LG', {x}, {y}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25)",
    # Bạn có thể thêm nhiều dòng mẫu từ câu SQL ban đầu vào đây
]

attribute_names = [
    "Health", "Physical Attack", "Physical Defense", "Magical Attack", "Magical Defense",
    "Chemical Attack", "Chemical Defense", "Atomic Attack", "Atomic Defense",
    "Mental Attack", "Mental Defense", "Speed", "Shield Strength",
    "Damage To Different Faction Rate", "Resistance To Different Faction Rate",
    "Damage To Same Faction Rate", "Resistance To Same Faction Rate",
    "Percent All Health", "Percent All Physical Attack", "Percent All Physical Defense",
    "Percent All Magical Attack", "Percent All Magical Defense", "Percent All Chemical Attack",
    "Percent All Chemical Defense", "Percent All Atomic Attack", "Percent All Atomic Defense",
    "Percent All Mental Attack", "Percent All Mental Defense"
]

# Giá trị tương ứng nếu thuộc tính được chọn
attribute_values = {
    "Health": 5000000000,
    "Physical Attack": 100000000,
    "Physical Defense": 75000000,
    "Magical Attack": 100000000,
    "Magical Defense": 75000000,
    "Chemical Attack": 100000000,
    "Chemical Defense": 75000000,
    "Atomic Attack": 100000000,
    "Atomic Defense": 75000000,
    "Mental Attack": 100000000,
    "Mental Defense": 75000000,
    "Speed": 100000000,
    "Shield Strength": 100000000,
    "Damage To Different Faction Rate": 50,
    "Resistance To Different Faction Rate": 50,
    "Damage To Same Faction Rate": 50,
    "Resistance To Same Faction Rate": 50,
    "Percent All Health": 50,
    "Percent All Physical Attack": 30,
    "Percent All Physical Defense": 25,
    "Percent All Magical Attack": 30,
    "Percent All Magical Defense": 25,
    "Percent All Chemical Attack": 30,
    "Percent All Chemical Defense": 25,
    "Percent All Atomic Attack": 30,
    "Percent All Atomic Defense": 25,
    "Percent All Mental Attack": 30,
    "Percent All Mental Defense": 25
}

# Danh sách tất cả các cột (bắt đầu từ power)
columns = [
    "power", "health", "physical_attack", "physical_defense",
    "magical_attack", "magical_defense", "chemical_attack", "chemical_defense",
    "atomic_attack", "atomic_defense", "mental_attack", "mental_defense",
    "speed", "critical_damage_rate", "critical_rate", "critical_resistance_rate", "ignore_critical_rate",
    "penetration_rate", "penetration_resistance_rate",
    "evasion_rate", "damage_absorption_rate", "ignore_damage_absorption_rate", "absorbed_damage_rate",
    "vitality_regeneration_rate", "vitality_regeneration_resistance_rate",
    "accuracy_rate", "lifesteal_rate", "shield_strength", "tenacity",
    "resistance_rate", "combo_rate", "ignore_combo_rate", "combo_damage_rate", "combo_resistance_rate", "stun_rate", "ignore_stun_rate",
    "reflection_rate", "ignore_reflection_rate", "reflection_damage_rate", "reflection_resistance_rate", "mana", "mana_regeneration_rate",
    "damage_to_different_faction_rate", "resistance_to_different_faction_rate",
    "damage_to_same_faction_rate", "resistance_to_same_faction_rate",
    "normal_damage_rate", "normal_resistance_rate",
    "skill_damage_rate", "skill_resistance_rate",
    "percent_all_health", "percent_all_physical_attack", "percent_all_physical_defense",
    "percent_all_magical_attack", "percent_all_magical_defense",
    "percent_all_chemical_attack", "percent_all_chemical_defense",
    "percent_all_atomic_attack", "percent_all_atomic_defense",
    "percent_all_mental_attack", "percent_all_mental_defense"
]

# Mapping thuộc tính → vị trí trong list `columns`
attribute_to_column = {
    "Health": "health",
    "Physical Attack": "physical_attack",
    "Physical Defense": "physical_defense",
    "Magical Attack": "magical_attack",
    "Magical Defense": "magical_defense",
    "Chemical Attack": "chemical_attack",
    "Chemical Defense": "chemical_defense",
    "Atomic Attack": "atomic_attack",
    "Atomic Defense": "atomic_defense",
    "Mental Attack": "mental_attack",
    "Mental Defense": "mental_defense",
    "Speed": "speed",
    "Shield Strength": "shield_strength",
    "Damage To Different Faction Rate": "damage_to_different_faction_rate",
    "Resistance To Different Faction Rate": "resistance_to_different_faction_rate",
    "Damage To Same Faction Rate": "damage_to_same_faction_rate",
    "Resistance To Same Faction Rate": "resistance_to_same_faction_rate",
    "Percent All Health": "percent_all_health",
    "Percent All Physical Attack": "percent_all_physical_attack",
    "Percent All Physical Defense": "percent_all_physical_defense",
    "Percent All Magical Attack": "percent_all_magical_attack",
    "Percent All Magical Defense": "percent_all_magical_defense",
    "Percent All Chemical Attack": "percent_all_chemical_attack",
    "Percent All Chemical Defense": "percent_all_chemical_defense",
    "Percent All Atomic Attack": "percent_all_atomic_attack",
    "Percent All Atomic Defense": "percent_all_atomic_defense",
    "Percent All Mental Attack": "percent_all_mental_attack",
    "Percent All Mental Defense": "percent_all_mental_defense"
}

def generate_maze_positions(n=100):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # các hướng: trên, phải, dưới, trái
    visited = set()
    positions = [(0, 0)]
    visited.add((0, 0))

    while len(positions) < n:
        # chọn ngẫu nhiên 1 điểm đã có
        base = random.choice(positions)

        # trộn hướng để tạo sự ngẫu nhiên
        random.shuffle(directions)

        for dx, dy in directions:
            new_pos = (base[0] + dx, base[1] + dy)
            if new_pos not in visited:
                visited.add(new_pos)
                positions.append(new_pos)
                break  # chỉ thêm 1 điểm mỗi vòng lặp

    return positions

def generate_insert_statements_optimized(names: list[str], statements_per_name=100):
    values_rows = []

    for name in names:
        positions = generate_maze_positions(statements_per_name)
        current_node_id = 1

        for x, y in positions:
            attribute = random.choice(attribute_names)
            value = attribute_values[attribute]
            column = attribute_to_column[attribute]

            # Khởi tạo toàn bộ cột = 0
            stats = {col: 0 for col in columns}
            stats[column] = value

            # Tạo list theo thứ tự đúng của các cột
            stat_values_str = ", ".join(str(stats[col]) for col in columns)

            row = f"('{name}', '{current_node_id}', '{attribute}', 'LG', {x}, {y}, {stat_values_str})"
            values_rows.append(row)
            current_node_id += 1

    # Tạo phần đầu của câu lệnh INSERT như bạn đã có
    insert_header = """INSERT INTO master_board (
        name, node_id, type, rank_level,
        position_x, position_y, power, health, physical_attack, physical_defense,
        magical_attack, magical_defense, chemical_attack, chemical_defense,
        atomic_attack, atomic_defense, mental_attack, mental_defense,
        speed, critical_damage_rate, critical_rate, critical_resistance_rate, ignore_critical_rate,
        penetration_rate, penetration_resistance_rate,
        evasion_rate, damage_absorption_rate, ignore_damage_absorption_rate, absorbed_damage_rate, 
        vitality_regeneration_rate, vitality_regeneration_resistance_rate,
        accuracy_rate, lifesteal_rate, shield_strength, tenacity,
        resistance_rate, combo_rate, ignore_combo_rate, combo_damage_rate, combo_resistance_rate, stun_rate, ignore_stun_rate, 
        reflection_rate, ignore_reflection_rate, reflection_damage_rate, reflection_resistance_rate, mana, mana_regeneration_rate,
        damage_to_different_faction_rate, resistance_to_different_faction_rate,
        damage_to_same_faction_rate, resistance_to_same_faction_rate,
        normal_damage_rate, normal_resistance_rate,
        skill_damage_rate, skill_resistance_rate,
        percent_all_health, percent_all_physical_attack, percent_all_physical_defense,
        percent_all_magical_attack, percent_all_magical_defense,
        percent_all_chemical_attack, percent_all_chemical_defense,
        percent_all_atomic_attack, percent_all_atomic_defense,
        percent_all_mental_attack, percent_all_mental_defense
    )\nVALUES
    """.strip()

    full_sql = insert_header + "\n" + ",\n".join(values_rows) + ";"

    with open("master_board.txt", "w", encoding="utf-8") as f:
        f.write(full_sql)



# Chạy ví dụ
names = ["Adamas", "Avian", "Barbarian", "Cylloran", "Dreizen", "Etrigon", "Firimir", "Gennesis", "Hecarus", "Illonima", 
         "Jaguar", "Kryptonian", "Lamania", "Marverick", "Nemesis", "Onyx", "Palladian", "Quasar", "Riverven", "Starroian", 
         "Terac", "Urius", "Vril", "Wyvern", "Xanthera", "Yornath", "Zerath"]
generate_insert_statements_optimized(names, statements_per_name=100)
