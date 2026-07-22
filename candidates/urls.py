from rest_framework.routers import DefaultRouter
from .views import (
    CandidateViewSet,
    WorkExperienceViewSet,
    EducationViewSet,
    SkillViewSet,
)

router = DefaultRouter()

router.register("candidates", CandidateViewSet)
router.register("work-experiences", WorkExperienceViewSet)
router.register("educations", EducationViewSet)
router.register("skills", SkillViewSet)


urlpatterns = router.urls