from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class WorkExperience(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="work_experiences"
    )

    company_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company_name}"


class Education(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="educations"
    )

    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=150)
    university = models.CharField(max_length=150)
    graduation_year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} - {self.university}"


class Skill(models.Model):
    LEVELS = (
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
        ("Expert", "Expert"),
    )

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    name = models.CharField(max_length=100)
    level = models.CharField(
        max_length=20,
        choices=LEVELS,
        default="Intermediate"
    )

    def __str__(self):
        return self.name