# api/serializers/items.py

from collections.abc import Mapping
from collections import OrderedDict

from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework.exceptions import ValidationError
from rest_framework.settings import api_settings
from rest_framework import serializers
from rest_framework.fields import get_error_detail, SkipField, set_value, empty

from todo.models import Item, Address, Comment
from users.models import User


class AddressSerializer(serializers.ModelSerializer):
    # item = serializers.IntegerField(source='item.id')

    class Meta:
        model = Address
        fields = ('id', 'country', 'city', 'street', 'house_number',
                  'zip_code', 'created_at',)


class ItemSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Item
        fields = ('id', 'owner', 'house_type', 'description', 'status',
                  'address', 'photo', 'price', 'created_at', 'updated_at')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        validated_data['address'] = address
        instance = Item.objects.create(**validated_data)
        return instance

    def to_internal_value(self, data):

        """
        Dict of native values <- Dict of primitive datatypes.
        """
        if not isinstance(data, Mapping):
            message = self.error_messages['invalid'].format(
                datatype=type(data).__name__
            )
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='invalid')

        ret = OrderedDict()
        errors = OrderedDict()
        fields = self._writable_fields
        # print('---data ', data)
        for field in fields:
            # print('---field ', field.field_name)
            validate_method = getattr(self, 'validate_' + field.field_name,
                                      None)
            primitive_value = field.get_value(data)
            # print('primitive_value ', primitive_value)
            try:
                if field.field_name == 'owner' and primitive_value == empty:
                    validated_value = User.objects.get(is_admin=True)
                else:
                    validated_value = field.run_validation(primitive_value)
                    if validate_method is not None:
                        validated_value = validate_method(validated_value)
                # print('validated_value ', validated_value)
            except ValidationError as exc:
                # if field.field_name == 'address':
                    # pass
                # else:
                print('---ValidationError ', field.field_name)
                errors[field.field_name] = exc.detail
            except DjangoValidationError as exc:
                errors[field.field_name] = get_error_detail(exc)
            except SkipField:
                pass
            else:
                set_value(ret, field.source_attrs, validated_value)

        if errors:
            print('---errors ', errors)
            raise ValidationError(errors)

        return ret


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'text', 'owner', 'acted', 'created_at',)
