# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from paymentprovider.models.base_model_ import Model
import re
from paymentprovider import util

import re  # noqa: E501

class PaymentData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, transaction_id=None, credit_cart_number=None, cvv=None, expiration_date=None, owner_name=None):  # noqa: E501
        """PaymentData - a model defined in OpenAPI

        :param transaction_id: The transaction_id of this PaymentData.  # noqa: E501
        :type transaction_id: str
        :param credit_cart_number: The credit_cart_number of this PaymentData.  # noqa: E501
        :type credit_cart_number: str
        :param cvv: The cvv of this PaymentData.  # noqa: E501
        :type cvv: str
        :param expiration_date: The expiration_date of this PaymentData.  # noqa: E501
        :type expiration_date: date
        :param owner_name: The owner_name of this PaymentData.  # noqa: E501
        :type owner_name: str
        """
        self.openapi_types = {
            'transaction_id': str,
            'credit_cart_number': str,
            'cvv': str,
            'expiration_date': date,
            'owner_name': str
        }

        self.attribute_map = {
            'transaction_id': 'transaction_id',
            'credit_cart_number': 'credit_cart_number',
            'cvv': 'cvv',
            'expiration_date': 'expiration_date',
            'owner_name': 'owner_name'
        }

        self._transaction_id = transaction_id
        self._credit_cart_number = credit_cart_number
        self._cvv = cvv
        self._expiration_date = expiration_date
        self._owner_name = owner_name

    @classmethod
    def from_dict(cls, dikt) -> 'PaymentData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PaymentData of this PaymentData.  # noqa: E501
        :rtype: PaymentData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transaction_id(self):
        """Gets the transaction_id of this PaymentData.


        :return: The transaction_id of this PaymentData.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this PaymentData.


        :param transaction_id: The transaction_id of this PaymentData.
        :type transaction_id: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def credit_cart_number(self):
        """Gets the credit_cart_number of this PaymentData.


        :return: The credit_cart_number of this PaymentData.
        :rtype: str
        """
        return self._credit_cart_number

    @credit_cart_number.setter
    def credit_cart_number(self, credit_cart_number):
        """Sets the credit_cart_number of this PaymentData.


        :param credit_cart_number: The credit_cart_number of this PaymentData.
        :type credit_cart_number: str
        """
        if credit_cart_number is None:
            raise ValueError("Invalid value for `credit_cart_number`, must not be `None`")  # noqa: E501
        if credit_cart_number is not None and not re.search(r'[0-9]{16,16}', credit_cart_number):  # noqa: E501
            raise ValueError("Invalid value for `credit_cart_number`, must be a follow pattern or equal to `/[0-9]{16,16}/`")  # noqa: E501

        self._credit_cart_number = credit_cart_number

    @property
    def cvv(self):
        """Gets the cvv of this PaymentData.


        :return: The cvv of this PaymentData.
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """Sets the cvv of this PaymentData.


        :param cvv: The cvv of this PaymentData.
        :type cvv: str
        """
        if cvv is None:
            raise ValueError("Invalid value for `cvv`, must not be `None`")  # noqa: E501
        if cvv is not None and not re.search(r'[0-9]{3,3}', cvv):  # noqa: E501
            raise ValueError("Invalid value for `cvv`, must be a follow pattern or equal to `/[0-9]{3,3}/`")  # noqa: E501

        self._cvv = cvv

    @property
    def expiration_date(self):
        """Gets the expiration_date of this PaymentData.


        :return: The expiration_date of this PaymentData.
        :rtype: date
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this PaymentData.


        :param expiration_date: The expiration_date of this PaymentData.
        :type expiration_date: date
        """
        if expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

    @property
    def owner_name(self):
        """Gets the owner_name of this PaymentData.


        :return: The owner_name of this PaymentData.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this PaymentData.


        :param owner_name: The owner_name of this PaymentData.
        :type owner_name: str
        """
        if owner_name is None:
            raise ValueError("Invalid value for `owner_name`, must not be `None`")  # noqa: E501

        self._owner_name = owner_name
