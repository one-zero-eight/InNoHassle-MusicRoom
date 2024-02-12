from abc import ABCMeta, abstractmethod


class AbstractAuthRepository(metaclass=ABCMeta):
    @abstractmethod
    async def is_user_registered(self, email: str | None = None, telegram_id: str | None = None) -> bool:
        ...

    @abstractmethod
    async def code_exists(self, email: str) -> bool:
        ...

    @abstractmethod
    async def save_code(self, email: str, code: str) -> None:
        ...

    @abstractmethod
    async def delete_code(self, email: str) -> None:
        ...

    @abstractmethod
    async def is_code_valid(self, email: str, code: str) -> bool:
        ...
