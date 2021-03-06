from typing import Union

from ..call_builder.base_call_builder import BaseCallBuilder
from ..client.base_async_client import BaseAsyncClient
from ..client.base_sync_client import BaseSyncClient


class TransactionsCallBuilder(BaseCallBuilder):
    """ Creates a new :class:`TransactionsCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`paydex_sdk.server.Server.transactions`.

    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(
        self, horizon_url: str, client: Union[BaseAsyncClient, BaseSyncClient]
    ) -> None:
        super().__init__(horizon_url, client)
        self.endpoint: str = "transactions"

    def transaction(self, transaction_hash: str) -> "TransactionsCallBuilder":
        """The transaction details endpoint provides information on a single transaction.
        The transaction hash provided in the hash argument specifies which transaction to load.


        :param transaction_hash: transaction hash
        :return: current TransactionsCallBuilder instance
        """
        self.endpoint = "transactions/{transaction_hash}".format(
            transaction_hash=transaction_hash
        )
        return self

    def for_account(self, account_id: str) -> "TransactionsCallBuilder":
        """This endpoint represents all transactions that affected a given account.

        :param account_id: account id
        :return: current TransactionsCallBuilder instance
        """
        self.endpoint = "accounts/{account_id}/transactions".format(
            account_id=account_id
        )
        return self

    def for_ledger(self, sequence: Union[str, int]) -> "TransactionsCallBuilder":
        """This endpoint represents all transactions in a given ledger.

        :param sequence: ledger sequence
        :return: current TransactionsCallBuilder instance
        """
        self.endpoint = "ledgers/{sequence}/transactions".format(sequence=sequence)
        return self

    def include_failed(self, include_failed: bool) -> "TransactionsCallBuilder":
        """Adds a parameter defining whether to include failed transactions. By default only
        transactions of successful transactions are returned.

        :param include_failed: Set to `True` to include failed transactions.
        :return: current TransactionsCallBuilder instance
        """
        self._add_query_param("include_failed", include_failed)
        return self
