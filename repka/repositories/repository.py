from abc import ABC

from repka.repositories.base import GenericIdModel, AsyncBaseRepo, AsyncQueryExecutor


class Repository(AsyncBaseRepo[GenericIdModel], ABC):
    """A repository which allows to set a query executor in the initializer"""
    def __init__(self, query_executor: AsyncQueryExecutor):
        self._query_executor = query_executor

    @property
    def query_executor(self) -> AsyncQueryExecutor:
        """Returns a query executor"""
        return self._query_executor
