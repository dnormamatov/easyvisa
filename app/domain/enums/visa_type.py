from enum import StrEnum


class VisaTypeName(StrEnum):
    STUDENT = "Student Visa"
    TOURIST = "Tourist Visa"
    WORK = "Work Visa"


class VisaTypeSlug(StrEnum):
    STUDENT = "student"
    TOURIST = "tourist"
    WORK = "work"
