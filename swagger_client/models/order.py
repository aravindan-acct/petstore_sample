# coding: utf-8

"""
    Swagger Petstore

    This is a sample Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Order(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'pet_id': 'int',
        'quantity': 'int',
        'ship_date': 'datetime',
        'status': 'str',
        'complete': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'pet_id': 'petId',
        'quantity': 'quantity',
        'ship_date': 'shipDate',
        'status': 'status',
        'complete': 'complete'
    }

    def __init__(self, id=None, pet_id=None, quantity=None, ship_date=None, status=None, complete=False):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._pet_id = None
        self._quantity = None
        self._ship_date = None
        self._status = None
        self._complete = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if pet_id is not None:
            self.pet_id = pet_id
        if quantity is not None:
            self.quantity = quantity
        if ship_date is not None:
            self.ship_date = ship_date
        if status is not None:
            self.status = status
        if complete is not None:
            self.complete = complete

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501


        :return: The id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.


        :param id: The id of this Order.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pet_id(self):
        """Gets the pet_id of this Order.  # noqa: E501


        :return: The pet_id of this Order.  # noqa: E501
        :rtype: int
        """
        return self._pet_id

    @pet_id.setter
    def pet_id(self, pet_id):
        """Sets the pet_id of this Order.


        :param pet_id: The pet_id of this Order.  # noqa: E501
        :type: int
        """

        self._pet_id = pet_id

    @property
    def quantity(self):
        """Gets the quantity of this Order.  # noqa: E501


        :return: The quantity of this Order.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Order.


        :param quantity: The quantity of this Order.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def ship_date(self):
        """Gets the ship_date of this Order.  # noqa: E501


        :return: The ship_date of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this Order.


        :param ship_date: The ship_date of this Order.  # noqa: E501
        :type: datetime
        """

        self._ship_date = ship_date

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501

        Order Status  # noqa: E501

        :return: The status of this Order.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.

        Order Status  # noqa: E501

        :param status: The status of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["placed", "approved", "delivered"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def complete(self):
        """Gets the complete of this Order.  # noqa: E501


        :return: The complete of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this Order.


        :param complete: The complete of this Order.  # noqa: E501
        :type: bool
        """

        self._complete = complete

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Order, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
