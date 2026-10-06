from django import forms

MAJOR_CHOICES = [
    ('', 'Select a Major'),
    ('CS', 'Computer Science'),
    ('ENG', 'Engineering'),
    ('BUS', 'Business'),
    ('ART', 'Arts'),
]

CLASS_STANDING_CHOICES = [
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior'),
]

LANGUAGE_CHOICES = [
    ('Python', 'Python'),
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('JavaScript', 'JavaScript'),
]

class StudentForm(forms.Form):
    student_name = forms.CharField(label='Student Name', required=True)
    student_id = forms.CharField(label='Student ID', required=True)
    major = forms.ChoiceField(choices=MAJOR_CHOICES, required=False)
    class_standing = forms.ChoiceField(
        choices=CLASS_STANDING_CHOICES, 
        widget=forms.RadioSelect, 
        required=False
    )
    languages = forms.MultipleChoiceField(
        choices=LANGUAGE_CHOICES, 
        widget=forms.CheckboxSelectMultiple, 
        required=False
    )
    expected_graduation = forms.IntegerField(
        label='Expected Graduation Year', 
        required=False,
        widget=forms.NumberInput(attrs={'min': 2024, 'max': 2035})
    )
    comments = forms.CharField(
        widget=forms.Textarea, 
        required=False
    )