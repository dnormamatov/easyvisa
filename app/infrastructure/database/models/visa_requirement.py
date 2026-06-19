from sqlalchemy import ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.base import Base


class VisaRequirementModel(Base):
    __tablename__ = "visa_requirements"
    __table_args__ = (
        UniqueConstraint("country_id", "visa_type_id", name="uq_country_visa_type"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    country_id: Mapped[int] = mapped_column(
        ForeignKey("countries.id", ondelete="CASCADE"),
        nullable=False,
    )
    visa_type_id: Mapped[int] = mapped_column(
        ForeignKey("visa_types.id", ondelete="CASCADE"),
        nullable=False,
    )
    required_documents: Mapped[str] = mapped_column(Text, nullable=False)
    application_process: Mapped[str] = mapped_column(Text, nullable=False)
    processing_time: Mapped[str] = mapped_column(Text, nullable=False)
    estimated_costs: Mapped[str] = mapped_column(Text, nullable=False)

    country: Mapped["CountryModel"] = relationship(back_populates="visa_requirements")
    visa_type: Mapped["VisaTypeModel"] = relationship(back_populates="visa_requirements")
