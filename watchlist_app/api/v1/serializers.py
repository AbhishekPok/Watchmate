from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform, Review


# def no_special_characters(value):
#     if any(char in "!@#$%^&&*()" for char in value):
#         raise serializers.ValidationError("No special character")

def check_len(value):
    if len(value) < 3:
        raise serializers.ValidationError("Must be at least 3 characters long.")

class WatchListSerializer(serializers.ModelSerializer):
    name_length = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = ['title','storyline','active','created_at','name_length']

        # exclude = ['active']

    def get_name_length(self, obj):
        return len(obj.title)

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist_stream_platform = WatchListSerializer(read_only=True, many=True)
    # watchlist_stream_platform = serializers.StringRelatedField(read_only=True, many=True)
    # watchlist_stream_platform = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # watchlist_stream_platform = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='movie_detail')
    # watchlist_stream_platform = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')

    class Meta:
        model = StreamPlatform
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"






# Obj level Validation-many field, Field Validation-one field, validators
# class MovieSerializer(serializers.Serializer):
#       id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100, validators=[check_len])
#     description = serializers.CharField(max_length=100, validators=[check_len])
#     active = serializers.BooleanField(default=True)
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#         # print(validated_data)
#         # return Movie.objects.create(name = validated_data['name'],
#         #                             description = validated_data['description'],
#         #                             active = validated_data['active'])
#
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
#
#     def validate_name(self, value):
#         value = value.strip()
#         if not value[0].isupper():
#             raise serializers.ValidationError("Movie names must start with Upper")
#         return value
#
#     def validate(self,attrs):
#         if attrs['name'] == attrs['description']:
#             raise serializers.ValidationError("Movie and description cannot be the same")
#         return attrs


