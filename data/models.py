from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    login = models.TextField(default=None, primary_key=True)
    name = models.TextField(default=None, null=True)
    bio = models.TextField(default=None, null=True)
    num_commits = models.IntegerField(default=None, null=True)
    reviews = models.IntegerField(default=None, null=True)
    issues_opened = models.IntegerField(default=None, null=True)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.login

    class Meta:
        ordering = ['login']


class Label(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Issue(models.Model):
    number = models.IntegerField()
    title = models.TextField()
    author = models.ForeignKey(Contributor,
                               on_delete=models.CASCADE,
                               related_name='issue_author')
    state = models.CharField(max_length=100)
    repo = models.CharField(max_length=200)
    labels = models.ManyToManyField(Label, blank=True)
    assignees = models.ManyToManyField(Contributor,
                                       related_name='issue_assignees',
                                       blank=True)
    hoster = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class IssueNumber(models.Model):
    number = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.number)


class MergeRequest(models.Model):
    number = models.IntegerField()
    title = models.TextField()
    repo = models.CharField(max_length=200)
    closes_issues = models.ManyToManyField(IssueNumber, blank=True)
    state = models.CharField(max_length=100)
    author = models.ForeignKey(Contributor,
                               on_delete=models.CASCADE,
                               related_name='mr_author')
    assignees = models.ManyToManyField(Contributor,
                                       related_name='mr_assignees',
                                       blank=True)
    ci_status = models.BooleanField()
    labels = models.ManyToManyField(Label, blank=True)
    hoster = models.CharField(max_length=100)

    def __str__(self):
        return self.title
