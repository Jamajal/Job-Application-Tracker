from django.db import models

class JobApplication(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    local = models.CharField(max_length=70)
    modality = models.CharField(max_length=10)
    link = models.CharField(max_length=300, null=True)
    observation = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # user

    def __str__(self):
        return self.role + ' - ' + self.company + ' (' + self.modality + ')'