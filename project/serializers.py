from rest_framework.serializers import ModelSerializer
from . import models


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username","password"]
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self,validated_data):
        user = models.User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username","id"]


class UserListSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id","username"]


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = models.Project
        fields = ["id","title","description","type"]


class ContributorSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = models.Contributor
        fields = ["id","user","role"]
    

class ContributorListSerializer(ModelSerializer):
    class Meta:
        model = models.Contributor
        fields = ["user","role"]
    
    def create(self,validated_data):
        if "role" not in validated_data:
            role = "PARTICIPANT"
        else:
            role = validated_data["role"]
    
        contributor = models.Contributor.objects.create(
            user = validated_data["user"],
            role = role,
            project = validated_data["project"]
        )
        contributor.save()
        return contributor


class ProjectSerializer(ModelSerializer):
    contributors = ContributorSerializer(source="contributor_set",many=True,required=False)
    class Meta:
        model = models.Project
        fields = ["title","description","type","contributors"]
    
    def create(self,validated_data):
        project = models.Project.objects.create(
            title =validated_data["title"],
            description =validated_data["description"],
            type = validated_data["type"]
        )
        project.save()
        return project

class ProjectListSerializer(ModelSerializer):
    contributors = ContributorSerializer(source="contributor_set",many=True,required=False)
    class Meta:
        model = models.Project
        fields = ["id","title","description","type","contributors"]

class IssueSerializer(ModelSerializer):
    class Meta:
        model = models.Issue
        fields = '__all__'


class IssueListSerializer(ModelSerializer):
    class Meta:
        model = models.Issue
        fields = ["id","status","tag","description","priority"]

    def create(self,validated_data):
        issue = models.Issue.objects.create(
            description = validated_data["description"],
            tag = validated_data["tag"],
            priority = validated_data["priority"],
            status = validated_data["status"],
            user = validated_data["user"],
            project = validated_data["project"]
        )
        issue.save()
        return issue


class CommentSerializer(ModelSerializer):
    issue = IssueListSerializer()
    class Meta:
        model = models.Comment
        fields = ["id","description","issue"]


class CommentListSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ["id","description"]

    def create(self,validated_data):
        comment = models.Comment.objects.create(
            description = validated_data["description"],
            user = validated_data["user"],
            issue = validated_data["issue"],
        )
        comment.save()
        return comment

