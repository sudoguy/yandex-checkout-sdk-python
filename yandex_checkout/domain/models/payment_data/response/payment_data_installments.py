from yandex_checkout.domain.common.payment_method_type import PaymentMethodType

from yandex_checkout.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataInstallments(ResponsePaymentData):
    def __init__(self, *args, **kwargs):
        super(PaymentDataInstallments, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.INSTALMENTS:
            self.type = PaymentMethodType.INSTALMENTS
