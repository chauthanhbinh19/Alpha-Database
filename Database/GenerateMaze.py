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

# Chọn ngẫu nhiên một mẫu
chosen_value = random.choice(sample_values)

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
        current_node_id = 1  # node_id duy nhất toàn cục

        for x, y in positions:
            template = random.choice(sample_values)
            filled = template.format(name=name, node_id=current_node_id, x=x, y=y)
            values_rows.append(filled)
            current_node_id += 1  # tăng node_id sau mỗi dòng

    insert_header = """
INSERT INTO master_board (
    name, node_id, type, rank_level,
    position_x, position_y, power, health, physical_attack, physical_defense,
    magical_attack, magical_defense, chemical_attack, chemical_defense,
    atomic_attack, atomic_defense, mental_attack, mental_defense,
    speed, critical_damage_rate, critical_rate, penetration_rate,
    evasion_rate, damage_absorption_rate, vitality_regeneration_rate,
    accuracy_rate, lifesteal_rate, shield_strength, tenacity,
    resistance_rate, combo_rate, reflection_rate, mana, mana_regeneration_rate,
    damage_to_different_faction_rate, resistance_to_different_faction_rate,
    damage_to_same_faction_rate, resistance_to_same_faction_rate,
    percent_all_health, percent_all_physical_attack, percent_all_physical_defense,
    percent_all_magical_attack, percent_all_magical_defense,
    percent_all_chemical_attack, percent_all_chemical_defense,
    percent_all_atomic_attack, percent_all_atomic_defense,
    percent_all_mental_attack, percent_all_mental_defense
)
VALUES
""".strip()

    full_sql = insert_header + "\n" + ",\n".join(values_rows) + ";"

    with open("master_board_optimized.txt", "w", encoding="utf-8") as f:
        f.write(full_sql)


# Chạy ví dụ
names = ["Adamas", "Avian", "Barbarian", "Cylloran", "Dreizen", "Etrigon", "Firimir", "Gennesis", "Hecarus", "Illonima", 
         "Jaguar", "Kryptonian", "Lamania", "Marverick", "Nemesis", "Onyx", "Palladian", "Quasar", "Riverven", "Starroian", 
         "Terac", "Urius", "Vril", "Wyvern", "Xanthera", "Yornath", "Zerath"]
generate_insert_statements_optimized(names, statements_per_name=100)
