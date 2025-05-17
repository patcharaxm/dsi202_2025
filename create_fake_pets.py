import os
import django
import random

# ตั้งค่า Django environment ก่อนใช้ model
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pawpal.settings')
django.setup()

from adopt.models import StrayAnimal

species_choices = ['dog', 'cat']
breed_dog = ['Golden Retriever', 'Labrador', 'Bulldog', 'Beagle', 'Poodle']
breed_cat = ['Siamese', 'Persian', 'Maine Coon', 'Ragdoll', 'Sphynx']
gender_choices = ['male', 'female']
size_choices = ['small', 'medium', 'large', 'extra large']
coat_length_choices = ['hairless', 'short', 'medium', 'long', 'wire', 'curly']
good_with_choices = ['kids', 'other dogs', 'cats']
color_choices = [
    'Apricot / Beige', 'Bicolor', 'Black', 'Brindle', 'Brown/Chocolate',
    'Golden', 'Gray/Blue/Silver', 'Harlequin', 'Merle (Blue)', 'Merle (Red)',
    'Red / Chestnut / Orange', 'Sable', 'Tricolor (Brown,Black, & White)',
    'White / Cream', 'Yellow / Tan / Blond / Fawn'
]
care_choices = ['House-trained', 'Special Needs']
behavior_choices = ['Anxiety', 'Barking and Howling', 'Biting', 'Chewing', 'Others']
age_unit_choices = ['day', 'week', 'month', 'year']
days_on_pawpal_choices = ['Any', '1', '7', '14', '30+']

def random_good_with():
    return random.sample(good_with_choices, k=random.randint(0, len(good_with_choices)))

def create_fake_pets(n=10):
    for i in range(n):
        sp = random.choice(species_choices)
        breed = random.choice(breed_dog) if sp == 'dog' else random.choice(breed_cat)
        name = f"{sp.capitalize()}_{i+1}"
        age_value = random.randint(1, 10)
        age_unit = random.choice(age_unit_choices)
        gender = random.choice(gender_choices)
        size = random.choice(size_choices)
        coat_length = random.choice(coat_length_choices)
        good_with = random_good_with()
        color = random.choice(color_choices)
        care = random.choice(care_choices)
        behavior = random.choice(behavior_choices)
        days = random.choice(days_on_pawpal_choices)
        location = "Bangkok"
        story = "This is a lovely pet looking for a new home."
        health_status = "Healthy"
        is_adopted = False

        pet = StrayAnimal(
            pet_id=f"{sp[0].upper()}{i+1:03d}",
            name=name,
            breed=breed,
            species=sp,
            age_value=age_value,
            age_unit=age_unit,
            gender=gender,
            size=size,
            coat_length=coat_length,
            good_with=good_with,
            color=color,
            care_and_behavior=care,
            days_on_pawpal=days,
            location=location,
            story_describe=story,
            behavior=behavior,
            health_status=health_status,
            is_adopted=is_adopted
        )
        pet.save()
        print(f"Created pet: {pet}")

if __name__ == "__main__":
    create_fake_pets(10)
