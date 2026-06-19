from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.infrastructure.database.models.country import CountryModel
from app.infrastructure.database.models.visa_requirement import VisaRequirementModel
from app.infrastructure.database.models.visa_type import VisaTypeModel


class VisaRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_all_countries(self) -> list[CountryModel]:
        result = await self._session.execute(
            select(CountryModel).order_by(CountryModel.name)
        )
        return list(result.scalars().all())

    async def get_all_visa_types(self) -> list[VisaTypeModel]:
        result = await self._session.execute(
            select(VisaTypeModel).order_by(VisaTypeModel.name)
        )
        return list(result.scalars().all())

    async def get_requirement_by_country_and_type(
        self,
        country_id: int,
        visa_type_id: int,
    ) -> VisaRequirementModel | None:
        result = await self._session.execute(
            select(VisaRequirementModel)
            .options(
                selectinload(VisaRequirementModel.country),
                selectinload(VisaRequirementModel.visa_type),
            )
            .where(
                VisaRequirementModel.country_id == country_id,
                VisaRequirementModel.visa_type_id == visa_type_id,
            )
        )
        return result.scalar_one_or_none()

    async def get_country_by_id(self, country_id: int) -> CountryModel | None:
        result = await self._session.execute(
            select(CountryModel).where(CountryModel.id == country_id)
        )
        return result.scalar_one_or_none()

    async def get_visa_type_by_id(self, visa_type_id: int) -> VisaTypeModel | None:
        result = await self._session.execute(
            select(VisaTypeModel).where(VisaTypeModel.id == visa_type_id)
        )
        return result.scalar_one_or_none()

    async def seed_countries(self, countries: list[dict[str, str]]) -> None:
        for item in countries:
            existing = await self._session.execute(
                select(CountryModel).where(CountryModel.code == item["code"])
            )
            if existing.scalar_one_or_none() is None:
                self._session.add(CountryModel(name=item["name"], code=item["code"]))
        await self._session.commit()

    async def seed_visa_types(self, visa_types: list[dict[str, str]]) -> None:
        for item in visa_types:
            existing = await self._session.execute(
                select(VisaTypeModel).where(VisaTypeModel.slug == item["slug"])
            )
            if existing.scalar_one_or_none() is None:
                self._session.add(
                    VisaTypeModel(name=item["name"], slug=item["slug"])
                )
        await self._session.commit()

    async def seed_requirements(self, requirements: list[dict]) -> None:
        for item in requirements:
            country_result = await self._session.execute(
                select(CountryModel).where(CountryModel.code == item["country_code"])
            )
            country = country_result.scalar_one()
            type_result = await self._session.execute(
                select(VisaTypeModel).where(VisaTypeModel.slug == item["visa_type_slug"])
            )
            visa_type = type_result.scalar_one()

            existing = await self._session.execute(
                select(VisaRequirementModel).where(
                    VisaRequirementModel.country_id == country.id,
                    VisaRequirementModel.visa_type_id == visa_type.id,
                )
            )
            if existing.scalar_one_or_none() is None:
                self._session.add(
                    VisaRequirementModel(
                        country_id=country.id,
                        visa_type_id=visa_type.id,
                        required_documents=item["required_documents"],
                        application_process=item["application_process"],
                        processing_time=item["processing_time"],
                        estimated_costs=item["estimated_costs"],
                    )
                )
        await self._session.commit()
