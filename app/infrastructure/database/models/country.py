from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.base import Base


class CountryModel(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    code: Mapped[str] = mapped_column(String(5), unique=True, nullable=False)

    visa_requirements: Mapped[list["VisaRequirementModel"]] = relationship(
        back_populates="country",
        cascade="all, delete-orphan",
    )
