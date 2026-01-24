from rest_framework import serializers
from .models import User, Post



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at']



class PostSerializer(serializers.ModelSerializer):
    # GET: Shows username string
    assigned_to = serializers.StringRelatedField(read_only=True)
    
    # POST: Accepts User ID
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='assigned_to', write_only=True
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'assigned_to', 'assigned_to_id', 'created_at']

    def validate_assigned_to(self, value):
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Assigned user does not exist.")
        return value
    