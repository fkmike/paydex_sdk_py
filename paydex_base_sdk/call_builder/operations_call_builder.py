from typing import Union

from ..call_builder.base_call_builder import BaseCallBuilder
from ..client.base_async_client import BaseAsyncClient
from ..client.base_sync_client import BaseSyncClient


class OperationsCallBuilder(BaseCallBuilder):
    """ Creates a new :class:`OperationsCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`Paydex_sdk.server.Server.operations`.


    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(
        self, horizon_url, client: Union[BaseAsyncClient, BaseSyncClient]
    ) -> None:
        super().__init__(horizon_url, client)
        self.endpoint: str = "operations"

    def operation(self, operation_id: Union[int, str]) -> "OperationsCallBuilder":
        """The operation details endpoint provides information on a single operation. The operation ID provided
        in the id argument specifies which operation to load.


        :param operation_id: Operation ID
        :return: this OperationCallBuilder instance
        """
        self.endpoint = "operations/{operation_id}".format(operation_id=operation_id)
        return self

    def for_account(self, account_id: str) -> "OperationsCallBuilder":
        """This endpoint represents all operations that were included in valid transactions that
        affected a particular account.
_

        :param account_id: Account ID
        :return: this OperationCallBuilder instance
        """
        self.endpoint: str = "accounts/{account_id}/operations".format(
            account_id=account_id
        )
        return self

    def for_ledger(self, sequence: Union[int, str]) -> "OperationsCallBuilder":
        """This endpoint returns all operations that occurred in a given ledger.


        :param sequence: Sequence ID
        :return: this OperationCallBuilder instance
        """
        self.endpoint: str = "ledgers/{sequence}/operations".format(sequence=sequence)
        return self

    def for_transaction(self, transaction_hash: str) -> "OperationsCallBuilder":
        """This endpoint represents all operations that are part of a given transaction.

        :param transaction_hash:
        :return: this OperationCallBuilder instance
        """
        self.endpoint: str = "transactions/{transaction_hash}/operations".format(
            transaction_hash=transaction_hash
        )
        return self

    def include_failed(self, include_failed: bool) -> "OperationsCallBuilder":
        """Adds a parameter defining whether to include failed transactions. By default only
        operations of successful transactions are returned.

        :param include_failed: Set to `True` to include operations of failed transactions.
        :return: current OperationsCallBuilder instance
        """
        self._add_query_param("include_failed", include_failed)
        return self

    def join(self, join: str) -> "OperationsCallBuilder":
        """join represents `join` param in queries, currently only supports `transactions`

        :param join: join represents `join` param in queries, currently only supports `transactions`
        :return: current OperationsCallBuilder instance
        """
        self._add_query_param("join", join)
        return self
