"""
Model serializer for ToDo
"""
from django.utils import timezone
from rest_framework import serializers

from todo.models import Tag, Todo


class SlugRelatedGetOrCreateField(serializers.SlugRelatedField):
    """
    Class to add tags if
    it does not exist
    """

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get_or_create(**{self.slug_field: data})[0]
        except (TypeError, ValueError):
            self.fail("invalid tag")


class TodoSerializer(serializers.ModelSerializer):
    """
    Model Serializer
    """

    tags = SlugRelatedGetOrCreateField(
        slug_field="name", queryset=Tag.objects.all(), many=True
    )
    id = serializers.CharField(read_only=True)

    def validate(self, data):
        if hasattr(self, "initial_data"):
            unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
            if unknown_keys:
                raise serializers.ValidationError(
                    "Got unknown fields: {}".format(unknown_keys)
                )
        return data

    @staticmethod
    def validate_due_date(self, value):
        """
        Validate due dates
        """
        if value < timezone.localdate():
            raise serializers.ValidationError("Due date cannot be before current date.")

        return value

    class Meta:
        """
        Meta for Model Serializer
        """

        model = Todo
        fields = [
            "id",
            "title",
            "description",
            "status",
            "high_priority",
            "tags",
            "due_date",
        ]
