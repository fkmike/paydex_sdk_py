from typing import Union

from ..call_builder.base_call_builder import BaseCallBuilder
from ..client.base_async_client import BaseAsyncClient
from ..client.base_sync_client import BaseSyncClient


class PaymentsCallBuilder(BaseCallBuilder):
    """ Creates a new :class:`PaymentsCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`paydex_sdk.server.Server.payments`.

    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(
        self, horizon_url: str, client: Union[BaseAsyncClient, BaseSyncClient]
    ) -> None:
        super().__init__(horizon_url, client)
        self.endpoint: str = "payments"

    def for_account(self, account_id: str) -> "PaymentsCallBuilder":
        """This endpoint responds with a collection of Payment operations where the given account
        was either the sender or receiver.

        :param account_id: Account ID
        :return: current PaymentsCallBuilder instance
        """
        self.endpoint = "accounts/{account_id}/payments".format(account_id=account_id)
        return self

    def for_ledger(self, sequence: Union[int, str]) -> "PaymentsCallBuilder":
        """This endpoint represents all payment operations that are part of a valid transactions in a given ledger.

        :param sequence: Ledger sequence
        :return: current PaymentsCallBuilder instance
        """
        self.endpoint: str = "ledgers/{sequence}/payments".format(sequence=sequence)
        return self

    def for_transaction(self, transaction_hash: str) -> "PaymentsCallBuilder":
        """This endpoint represents all payment operations that are part of a given transaction.

        :param transaction_hash: Transaction hash
        :return: current PaymentsCallBuilder instance
        """
        self.endpoint: str = "transactions/{transaction_hash}/payments".format(
            transaction_hash=transaction_hash
        )
        return self

    def include_failed(self, include_failed: bool) -> "PaymentsCallBuilder":
        """Adds a parameter defining whether to include failed transactions. By default only
        payments of successful transactions are returned.

        :param include_failed: Set to ``True`` to include payments of failed transactions.
        :return: current PaymentsCallBuilder instance
        """
        self._add_query_param("include_failed", include_failed)
        return self
