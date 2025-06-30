def calculate_power(
    health, physical_attack, physical_defense, magical_attack, magical_defense,
    chemical_attack, chemical_defense, atomic_attack, atomic_defense, mental_attack, mental_defense,
    speed, critical_damage_rate, critical_rate, critical_resistance_rate, ignore_critical_rate, 
    penetration_rate, penetration_resistance_rate, evasion_rate, 
    damage_absorption_rate, ignore_damage_absorption_rate, absorbed_damage_rate, 
    vitality_regeneration_rate, vitality_regeneration_resistance_rate, accuracy_rate, lifesteal_rate, 
    shield_strength, tenacity, resistance_rate, combo_rate, ignore_combo_rate, combo_damage_rate, combo_resistance_rate, 
    stun_rate, ignore_stun_rate, reflection_rate, ignore_reflection_rate, reflection_damage_rate, reflection_resistance_rate,
    mana, mana_regeneration_rate, 
    damage_to_different_faction_rate, resistance_to_different_faction_rate, 
    damage_to_same_faction_rate, resistance_to_same_faction_rate,
    normal_damage_rate, normal_resistance_rate,
    skill_damage_rate, skill_resistance_rate
):
    # Hệ số mặc định cho các chỉ số cơ bản
    weight = 0.5

    # Tổng sát thương và phòng thủ
    total_attack = (
        physical_attack + magical_attack + chemical_attack + atomic_attack + mental_attack
    ) * weight

    total_defense = (
        physical_defense + magical_defense + chemical_defense + atomic_defense + mental_defense
    ) * weight + shield_strength * weight

    # Điều chỉnh các chỉ số `rate` theo tổng attack, defense, và health
    adjusted_critical_rate = (critical_rate / 100) * total_attack /100 
    adjusted_critical_damage = (critical_damage_rate / 100) * total_attack /100
    adjusted_critical_resistance_rate = (critical_resistance_rate / 100) * total_defense /100
    adjusted_ignore_critical_rate = (ignore_critical_rate / 100) * total_attack /100
    adjusted_penetration = (penetration_rate / 100) * total_attack /100
    adjusted_penetration_resistance_rate = (penetration_resistance_rate / 100) * total_defense /100
    adjusted_evasion = (evasion_rate / 100) * total_defense /100
    adjusted_absorption = (damage_absorption_rate / 100) * total_defense /100
    adjusted_ignore_damage_absorption_rate = (ignore_damage_absorption_rate / 100) * total_defense /100
    adjusted_absorbed_damage_rate = (absorbed_damage_rate / 100) * total_defense /100
    adjusted_regeneration = (vitality_regeneration_rate / 100) * health /100
    adjusted_vitality_regeneration_resistance_rate = (vitality_regeneration_resistance_rate / 100) * health /100
    adjusted_accuracy = (accuracy_rate / 100) * total_attack /100
    adjusted_lifesteal = (lifesteal_rate / 100) * total_attack /100
    adjusted_tenacity = (tenacity / 100) * total_defense /100
    adjusted_resistance = (resistance_rate / 100) * (total_defense + health * 0.5) /100 
    adjusted_combo = (combo_rate / 100) * total_attack /100
    adjusted_ignore_combo_rate = (ignore_combo_rate / 100) * total_attack /100
    adjusted_combo_damage_rate = (combo_damage_rate / 100) * total_attack /100
    adjusted_combo_resistance_rate = (combo_resistance_rate / 100) * total_defense /100
    adjusted_stun_rate = (stun_rate / 100) * total_attack /100
    adjusted_ignore_stun_rate = (ignore_stun_rate / 100) * total_attack /100
    adjusted_reflection = (reflection_rate / 100) * (total_defense + health * 0.5) /100
    adjusted_ignore_reflection_rate = (ignore_reflection_rate / 100) * total_attack /100
    adjusted_reflection_damage_rate = (reflection_damage_rate / 100) * total_attack /100
    adjusted_reflection_resistance_rate = (reflection_resistance_rate / 100) * total_defense /100

    # Điều chỉnh thuộc tính về faction (chủng tộc)
    adjusted_damage_to_different_faction = (damage_to_different_faction_rate / 100) * total_attack /100
    adjusted_resistance_to_different_faction = (resistance_to_different_faction_rate / 100) * total_defense /100
    adjusted_damage_to_same_faction = (damage_to_same_faction_rate / 100) * total_attack /100
    adjusted_resistance_to_same_faction = (resistance_to_same_faction_rate / 100) * total_defense /100

    adjusted_normal_damage_rate = (normal_damage_rate / 100) * total_attack /100
    adjusted_normal_resistance_rate = (normal_resistance_rate / 100) * total_defense /100
    adjusted_skill_damage_rate = (skill_damage_rate / 100) * total_attack /100
    adjusted_skill_resistance_rate = (skill_resistance_rate / 100) * total_defense /100

    # Điều chỉnh mana và hồi mana
    adjusted_mana = mana * 0.5  
    adjusted_mana_regeneration = (mana_regeneration_rate / 100) * mana  

    # Tính tổng sức mạnh
    power = (
        health * weight + total_attack + total_defense + speed * weight +
        adjusted_critical_rate + adjusted_critical_damage + adjusted_critical_resistance_rate + adjusted_ignore_critical_rate + 
        adjusted_penetration + adjusted_penetration_resistance_rate +
        adjusted_evasion + adjusted_absorption + adjusted_ignore_damage_absorption_rate + adjusted_absorbed_damage_rate + 
        adjusted_regeneration + adjusted_vitality_regeneration_resistance_rate + adjusted_accuracy +
        adjusted_lifesteal + adjusted_tenacity + adjusted_resistance + 
        adjusted_combo + adjusted_ignore_combo_rate + adjusted_combo_damage_rate + adjusted_combo_resistance_rate + 
        adjusted_stun_rate + adjusted_ignore_stun_rate + 
        adjusted_reflection + adjusted_ignore_reflection_rate + adjusted_reflection_damage_rate + adjusted_reflection_resistance_rate +
        adjusted_damage_to_different_faction + adjusted_resistance_to_different_faction +
        adjusted_damage_to_same_faction + adjusted_resistance_to_same_faction +
        adjusted_mana + adjusted_mana_regeneration + 
        adjusted_normal_damage_rate + adjusted_normal_resistance_rate +
        adjusted_skill_damage_rate + adjusted_skill_resistance_rate
    )

    return power