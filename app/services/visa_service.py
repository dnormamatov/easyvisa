from app.infrastructure.database.models.country import CountryModel
from app.infrastructure.database.models.visa_requirement import VisaRequirementModel
from app.infrastructure.database.models.visa_type import VisaTypeModel
from app.infrastructure.repositories.visa_repository import VisaRepository


class VisaService:
    def __init__(self, visa_repository: VisaRepository) -> None:
        self._visa_repository = visa_repository

    async def get_countries(self) -> list[CountryModel]:
        return await self._visa_repository.get_all_countries()

    async def get_visa_types(self) -> list[VisaTypeModel]:
        return await self._visa_repository.get_all_visa_types()

    async def get_visa_requirement(
        self,
        country_id: int,
        visa_type_id: int,
    ) -> VisaRequirementModel | None:
        return await self._visa_repository.get_requirement_by_country_and_type(
            country_id=country_id,
            visa_type_id=visa_type_id,
        )

    async def get_country(self, country_id: int) -> CountryModel | None:
        return await self._visa_repository.get_country_by_id(country_id)

    async def get_visa_type(self, visa_type_id: int) -> VisaTypeModel | None:
        return await self._visa_repository.get_visa_type_by_id(visa_type_id)

    @staticmethod
    def format_requirement(requirement: VisaRequirementModel) -> str:
        country_name = requirement.country.name
        visa_type_name = requirement.visa_type.name

        return (
            f"🌍 <b>{country_name}</b> — {visa_type_name}\n\n"
            f"📄 <b>Required Documents:</b>\n{requirement.required_documents}\n\n"
            f"📋 <b>Application Process:</b>\n{requirement.application_process}\n\n"
            f"⏱ <b>Processing Time:</b>\n{requirement.processing_time}\n\n"
            f"💰 <b>Estimated Costs:</b>\n{requirement.estimated_costs}"
        )
