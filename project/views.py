from xmlrpc.client import ResponseError
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action,api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny,DjangoModelPermissions
from project.permissions import IsContributor,IsAuthor, IsProjectAuthor
from . import serializers
from . import models
# Create your views here.

class signup(viewsets.ModelViewSet):
    permission_classes =[AllowAny]
    serializer_class = serializers.SignUpSerializer
    queryset = models.User.objects.all()


class projects(viewsets.ModelViewSet):

    serializer_class = serializers.ProjectSerializer
    permission_classes = [IsAuthenticated,IsProjectAuthor]

    def get_queryset(self):
        queryset = models.Project.objects.filter(contributors__id=self.request.user.id)
        return queryset
    
    def perform_create(self, serializer_class):
        project = serializer_class.save()
        contributor = models.Contributor.objects.create(project=project,role="AUTHOR",user=self.request.user)   

class contributors(viewsets.ModelViewSet):
    serializer_class = serializers.ContributorListSerializer
    permission_classes = [IsContributor,]

    def get_queryset(self):
        return models.Contributor.objects.filter(project=self.kwargs["project_pk"])

    def list(self,request,project_pk):
        queryset = models.Contributor.objects.filter(project__pk=project_pk)
        serializer = serializers.ContributorSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None,project_pk=None):
        contributor = models.Contributor.objects.get(project__pk=project_pk,user__pk=pk)
        serializer = serializers.ContributorSerializer(contributor)
        return Response(serializer.data)
    
    def perform_create(self,serializer_class):
        serializer_class.save(project=models.Project.objects.get(id=self.kwargs["project_pk"]))
    
    def destroy(self,request,pk=None,project_pk=None):
        instance = models.Contributor.objects.get(project__id=project_pk,user__id=pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class issues(viewsets.ModelViewSet):
    permission_classes = [IsContributor,IsAuthor]
    serializer_class = serializers.IssueListSerializer
    def get_queryset(self):
        return models.Issue.objects.filter(project=self.kwargs["project_pk"])
    
    def perform_create(self,serializer_class):
        serializer_class.save(
            project=models.Project.objects.get(id=self.kwargs["project_pk"]),
            user=models.User.objects.get(id=self.request.user.id)
        )
    

class comments(viewsets.ModelViewSet):
    permission_classes = [IsContributor,IsAuthor]
    serializer_class = serializers.CommentListSerializer
    def get_queryset(self):
        return models.Comment.objects.filter(issue=self.kwargs["issue_pk"])
    
    def perform_create(self,serializer_class):
        serializer_class.save(
            issue = models.Issue.objects.get(id=self.kwargs["issue_pk"]),
            user=models.User.objects.get(id=self.request.user.id),
        )
    def list(self,request,project_pk=None,issue_pk=None):
        queryset = models.Comment.objects.filter(issue_id=issue_pk)
        serializer = serializers.CommentSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,project_pk=None,issue_pk=None,pk=None):
        queryset = models.Comment.objects.filter(issue_id=issue_pk).filter(id=pk)
        serializer = serializers.CommentSerializer(queryset,many=True)
        return Response(serializer.data)


