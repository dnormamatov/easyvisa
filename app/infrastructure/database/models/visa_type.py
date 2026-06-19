from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.base import Base


class VisaTypeModel(Base):
    __tablename__ = "visa_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    visa_requirements: Mapped[list["VisaRequirementModel"]] = relationship(
        back_populates="visa_type",
        cascade="all, delete-orphan",
    )
