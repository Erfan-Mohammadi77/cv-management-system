from django.contrib import admin
from .models import Candidate, WorkExperience, Education, Skill


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "created_at",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "candidate",
        "company_name",
        "position",
        "start_date",
        "end_date",
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "candidate",
        "degree",
        "university",
        "graduation_year",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "candidate",
        "name",
        "level",
    )