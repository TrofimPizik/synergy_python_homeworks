# Задание №1
print("Введите вид питомца")
kind_of_animal = input()
print("Введите имя питомца")
name_of_animal = input()
print("Введите возраст питомца")
age_of_animal = input()

print(f"Это {kind_of_animal} по кличке \"{name_of_animal}\". Возраст: {age_of_animal} года.")

# Задание номер №2
print("Введите этапы эвоолюции человека в правильном порядке")
print("Введите первый этап")
stage_of_human_evolution_hominoidea = input()
print("Введите второй этап")
stage_of_human_evolution_australopithecus = input()
print("Введите третий этап")
stage_of_human_evolution_homo_habilis = input()
print("Введите четвертый этап")
stage_of_human_evolution_homo_erectus = input()
print("Введите пятый этап")
stage_of_human_evolution_homo_neanderthalensis = input()
print("Введите шестой этап")
stage_of_human_evolution_homo_sapiens = input()
print(
    stage_of_human_evolution_hominoidea,
    stage_of_human_evolution_australopithecus,
    stage_of_human_evolution_homo_habilis,
    stage_of_human_evolution_homo_erectus,
    stage_of_human_evolution_homo_neanderthalensis,
    stage_of_human_evolution_homo_sapiens,
    sep=" => "
)